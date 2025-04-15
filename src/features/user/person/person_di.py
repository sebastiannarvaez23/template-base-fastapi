from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.session import get_db
from core.minio.minio_client import MinioClient
from features.user.person.adapters.repository.person_repository_impl import PersonRepositoryImpl
from features.user.person.application.use_cases.create_person import CreatePerson
from features.user.person.application.use_cases.delete_person import DeletePerson
from features.user.person.application.use_cases.get_person_by_id import GetPersonById
from features.user.person.application.use_cases.get_persons import GetPersons
from features.user.person.application.use_cases.update_person import UpdatePerson


def get_minio_client() -> MinioClient:
    return MinioClient()

def get_person_repository(db: AsyncSession = Depends(get_db)) -> PersonRepositoryImpl:
    return PersonRepositoryImpl(db)

# uses cases

def get_get_persons_use_case(
    person_repository: PersonRepositoryImpl = Depends(get_person_repository)
) -> GetPersons:
    return GetPersons(person_repository)

def get_get_person_by_id_use_case(
    person_repository: PersonRepositoryImpl = Depends(get_person_repository)
) -> GetPersonById:
    return GetPersonById(person_repository)

def get_create_person_use_case(
    person_repository: PersonRepositoryImpl = Depends(get_person_repository)
) -> CreatePerson:
    return CreatePerson(person_repository)


def get_update_person_use_case(
    person_repository: PersonRepositoryImpl = Depends(get_person_repository)
) -> UpdatePerson:
    return UpdatePerson(person_repository)


def get_delete_person_use_case(
    person_repository: PersonRepositoryImpl = Depends(get_person_repository)
) -> DeletePerson:
    return DeletePerson(person_repository)

# ---

def get_person_service(
    minio_client: MinioClient = Depends(get_minio_client),
    create_person_use_case: CreatePerson = Depends(get_create_person_use_case),
    get_person_by_id_use_case: GetPersonById = Depends(get_get_person_by_id_use_case),
    get_persons_use_case: GetPersons = Depends(get_get_persons_use_case),
    update_person_use_case: UpdatePerson = Depends(get_update_person_use_case),
    delete_person_use_case: DeletePerson = Depends(get_delete_person_use_case),
):
    from features.user.person.application.services.person_service import PersonService
    return PersonService(
        minio_client=minio_client,
        get_persons_use_case=get_persons_use_case,
        get_person_by_id_use_case=get_person_by_id_use_case,
        create_person_use_case=create_person_use_case,
        update_person_use_case=update_person_use_case,
        delete_person_use_case=delete_person_use_case
    )