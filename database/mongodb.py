from motor.motor_asyncio import AsyncIOMotorClient

async def save_to_mongodb(data):
  client = AsyncIOMotorClient('mongodb://localhost:27017')
  db = client['similarweb']
  collection = db['website_data']
  await collection.insert_one(data)

async def get_from_mongodb(url):
    client = AsyncIOMotorClient('mongodb://localhost:27017')
    db = client['similarweb']
    collection = db['website_data']
    result = await collection.find_one({'url': url})
    return result