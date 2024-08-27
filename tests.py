from fastapi import APIRouter
from models import Test
from typing import List
from beanie import PydanticObjectId
from bson import ObjectId
from fastapi import HTTPException

test_router = APIRouter()


@test_router.get('/', status_code=200)
async def getalltests() -> List[Test]:
    tests = await Test.find_all().to_list()

    return tests


@test_router.post('/', status_code=201)
async def createTest(test: Test):
    await test.create()

    return {"message": "Test has been saved!"}


@test_router.delete('/{test_id}', status_code=204)
async def deleteTest(test_id: PydanticObjectId):
    test = await Test.get(test_id)

    if test is None:
        raise HTTPException(status_code=404, detail="Test not found")

    await test.delete()

    return {"message": "Deleted!"}
