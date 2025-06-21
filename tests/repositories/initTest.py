from motor.motor_asyncio import AsyncIOMotorClient

@pytest.fixture(scope="session")
def client():
    return AsyncIOMotorClient("mongodb://localhost:27017")