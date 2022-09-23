from pymongo import MongoClient
from utils.configs import configData

cluster = MongoClient(configData['mongokey'])

db = cluster[configData['database']]

perf = db['PROFILE']

async def upPerfil(member, oq, name, value):

    perf.update_one( { "_id": member.id}, {'$set':{oq:{'name': name,'value':value}}}, upsert = True )