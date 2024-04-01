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
    results = []
    async for document in collection.find({'meta.request.domain': url}):
        document['_id'] = str(document['_id'])
        results.append(document)
    
    return results

async def get_rank_from_mongodb():
    client = AsyncIOMotorClient('mongodb://localhost:27017')
    db = client['similarweb']
    collection = db['website_data']
    results = []
    async for document in collection.find({'top_sites.rank': 1}):
        document['_id'] = str(document['_id'])
        results.append(document)
    
    return results