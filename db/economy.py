from pymongo import MongoClient
from utils.configs import configData

cluster = MongoClient(configData['mongokey'])

db = cluster[configData['database']]

bank = db['BANK']

inv = db['INV']

async def update_bank(id, LOTHCOINS: int):

    if id is not None:

        if bank.count_documents({"_id":id.id}) == 0:

            bank.insert_one({"_id":id.id, "Nome":id.name, "LOTHCOINS": LOTHCOINS})

        bank.update_one({"_id": id.id}, {"$inc": {"LOTHCOINS": LOTHCOINS}}, upsert = True)