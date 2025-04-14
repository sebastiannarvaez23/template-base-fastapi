from fastapi import UploadFile
from sqlalchemy.exc import IntegrityError
from uuid import UUID, uuid4

from core.minio.minio_client import MinioClient
from features.user.person.adapters.repository.person_repository_impl import PersonRepositoryImpl
from features.user.person.domain.entities.person import Person
from features.user.person.domain.exceptions.person_exceptions import PersonAlreadyExistsException, PhoneAlreadyExistsException, PersonNotFoundException
from features.user.person.domain.utils.person_filter import PersonFilter
from features.user.person.schemas.person_schema import PersonCreateSchema, PersonResponseSchema, PersonUpdateSchema
from utils.pagination.pagination_utils import paginate_query


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
    
    async def update_person(
        self,
        person_id: UUID,
        person_data: PersonUpdateSchema,
        avatar: UploadFile = None
    ) -> PersonResponseSchema:
        person = await self.person_repository.get_by_id(person_id)
        if not person:
            raise PersonNotFoundException(person_id)
        try:
            avatar_filename = person.avatar
            if avatar:
                if person.avatar:
                    self.minio_client.delete_file(person.avatar)
                avatar_data = await avatar.read()
                avatar_filename = self.minio_client.upload_file(
                    avatar_data,
                    file_name=f"avatar_{uuid4()}.jpg",
                    content_type=avatar.content_type
                )
            person_data_dict = person_data.dict(exclude_unset=True)
            person_data_dict["avatar"] = avatar_filename
            updated_person = await self.person_repository.update(person, person_data_dict)
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