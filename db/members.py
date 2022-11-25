from pymongo import MongoClient
from main import configData

cluster = MongoClient(configData['mongokey'])
db = cluster[configData['database']]
perf = db['PROFILE']

class dbmember:

    def upPerfil(member, oq, name, value):
        perf.update_one( { "_id": member.id}, {'$set':{oq:{'name': name,'value':value}}}, upsert = True )