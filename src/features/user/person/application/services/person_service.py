from fastapi import UploadFile
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from uuid import UUID

from core.minio.minio_client import MinioClient
from features.user.person.application.use_cases.create_person import CreatePerson
from features.user.person.application.use_cases.delete_person import DeletePerson
from features.user.person.application.use_cases.get_person_by_id import GetPersonById
from features.user.person.application.use_cases.get_persons import GetPersons
from features.user.person.application.use_cases.update_person import UpdatePerson
from features.user.person.domain.exceptions.person_exceptions import PersonAlreadyExistsException, PhoneAlreadyExistsException, PersonNotFoundException
from features.user.person.schemas.person_schema import PersonCreateSchema, PersonResponseSchema, PersonUpdateSchema


class PersonService:
    def __init__(
            self, 
            minio_client: MinioClient,
            get_persons_use_case: GetPersons,
            get_person_by_id_use_case: GetPersonById,
            create_person_use_case: CreatePerson,
            update_person_use_case: UpdatePerson,
            delete_person_use_case: DeletePerson
        ):
        self.minio_client = minio_client
        self.get_persons_use_case = get_persons_use_case
        self.get_person_by_id_use_case = get_person_by_id_use_case
        self.create_person_use_case = create_person_use_case
        self.update_person_use_case = update_person_use_case
        self.delete_person_use_case = delete_person_use_case
        
    async def get_persons(self, page: int, filters: dict):
        result = await self.get_persons_use_case.execute(page, filters)
        for person in result["rows"]:
            if person.avatar:
                person.avatar = self.minio_client.get_presigned_url(person.avatar)
            else:
                person.avatar = None
        return result
    
    async def get_person_by_id(self, person_id: UUID) -> PersonResponseSchema:
        person = await self.get_person_by_id_use_case.execute(person_id)
        if not person:
            raise PersonNotFoundException(person_id)
        person.avatar = self.minio_client.get_presigned_url(person.avatar) if person.avatar else None
        return PersonResponseSchema.from_orm(person)

    async def create_person(self, person_data: PersonCreateSchema, avatar: UploadFile = None) -> PersonResponseSchema:
        avatar_filename = None
        if avatar:
            avatar_filename = await self.minio_client.upload_file(avatar)
        try:
            person = await self.create_person_use_case.execute(person_data, avatar_filename)
        except IntegrityError as e:
            if "email" in str(e.orig).lower():
                raise PersonAlreadyExistsException(person_data.email)
            elif "phone" in str(e.orig).lower():
                raise PhoneAlreadyExistsException(person_data.phone)
            raise
        return PersonResponseSchema.from_orm(person)
    
    async def update_person(self, person_id: UUID, person_data: PersonUpdateSchema, avatar: UploadFile = None) -> PersonResponseSchema:
        person = await self.get_person_by_id_use_case.execute(person_id)
        if not person: raise PersonNotFoundException(person_id)
        try:
            if avatar:
                if person.avatar: self.minio_client.delete_file(person.avatar)
                avatar_filename = await self.minio_client.upload_file(avatar)
            updated_person = await self.update_person_use_case.execute(person, person_data, avatar_filename)
        except IntegrityError as e:
            if "email" in str(e.orig).lower():
                raise PersonAlreadyExistsException(person_data.email)
            elif "phone" in str(e.orig).lower():
                raise PhoneAlreadyExistsException(person_data.phone)
            raise
        return PersonResponseSchema.from_orm(updated_person)

    async def delete_person(self, person_id: UUID):
        person = await self.get_person_by_id_use_case.execute(person_id)
        if not person:
            raise PersonNotFoundException(person_id)
        return await self.delete_person_use_case.execute(person)