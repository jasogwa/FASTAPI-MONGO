from beanie import Document
from pydantic import Field


class Test(Document):
    test: str = Field(max_length=400)

    class Settings:
        name = "test_database"

    class Config:
        schema_extra = {
            "test": "A sample test"
        }
