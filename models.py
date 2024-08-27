from datetime import datetime
from beanie import Document
from pydantic import Field


class Test(Document):
    test_content: str = Field(max_length=400)
    date_created: datetime = datetime.now()

    class Settings:
        name = "test_database"

    class Config:
        schema_extra = {
            "test_content": "A sample test",
            "date_created": datetime.now()
        }
