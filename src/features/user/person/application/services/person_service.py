import uuid
import logging

from fastapi import UploadFile, Depends
from sqlalchemy.exc import IntegrityError
from uuid import UUID, uuid4

from core.minio.minio_client import MinioClient
from features.user.person.adapters.repository.person_repository_impl import PersonRepositoryImpl
from features.user.person.domain.entities.person import Person
from features.user.person.domain.exceptions.person_exceptions import PersonAlreadyExistsException, PhoneAlreadyExistsException, PersonNotFoundException
from features.user.person.domain.utils.person_filter import PersonFilter
from features.user.person.schemas.person_schema import PersonCreateSchema, PersonResponseSchema, PersonUpdateSchema
from utils.pagination.pagination_utils import paginate_query

logger = logging.getLogger(__name__)

class PersonService:
    def __init__(self, person_repository: PersonRepositoryImpl, minio_client: MinioClient):
        self.person_repository = person_repository
        self.minio_client = minio_client
        
    async def get_persons(self, page: int, filters: dict):
        base_query = await self.person_repository.query()
        query = PersonFilter(**filters.dict()).apply(base_query)
        return await paginate_query(self.person_repository.db, query, page)
    
    async def get_person_by_id(self, person_id: UUID) -> PersonResponseSchema:
        person = await self.person_repository.get_by_id(person_id)
        if not person:
            raise PersonNotFoundException(person_id)
        return PersonResponseSchema.from_orm(person)

    async def create_person(self, person_data: PersonCreateSchema, avatar: UploadFile = None) -> PersonResponseSchema:
        try:
            avatar_filename = None
            if avatar:
                avatar_data = await avatar.read()
                avatar_filename = self.minio_client.upload_file(
                    avatar_data, file_name=f"avatar_{uuid4()}.jpg", content_type=avatar.content_type
                )
            person_data_dict = person_data.dict()
            person_data_dict["avatar"] = avatar_filename
            person = await self.person_repository.create(person_data_dict)
        except IntegrityError as e:
            if "email" in str(e.orig).lower():
                raise PersonAlreadyExistsException(person_data.email)
            elif "phone" in str(e.orig).lower():
                raise PhoneAlreadyExistsException(person_data.phone)
            else:
                raise
        return PersonResponseSchema.from_orm(person)
    
    async def update_person(self, person_id: UUID, person_data: PersonUpdateSchema) -> PersonResponseSchema:
        person = await self.person_repository.get_by_id(person_id)
        if not person:
            raise PersonNotFoundException(person_id)
        try:
            updated_person = await self.person_repository.update(person, person_data)
        except IntegrityError as e:
            if "email" in str(e.orig).lower():
                raise PersonAlreadyExistsException(person_data.email)
            elif "phone" in str(e.orig).lower():
                raise PhoneAlreadyExistsException(person_data.phone)
            else:
                raise
        return PersonResponseSchema.from_orm(updated_person)

    async def delete_person(self, person_id: UUID):
        person = await self.person_repository.get_by_id(person_id)
        if not person:
            raise PersonNotFoundException(person_id)
        return await self.person_repository.delete(person)