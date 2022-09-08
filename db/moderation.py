from pymongo import MongoClient
from utils.configs import configData

cluster = MongoClient(configData['mongokey'])

db = cluster[configData['database']]

mod = db['MOD']

advdb = db['ADV']

async def lang(opt,oq,guild):

    if opt is not None:

        if mod.count_documents({"_id":guild.id}) == 0:

            mod.insert_one({"_id":guild.id, "Nome":guild.name})

        mod.update_one({"_id": guild.id}, {"$set": {f"{opt}": oq}}, upsert = True)

async def autorole(opt,oq,guild,id):

    if opt is not None:

        if mod.count_documents({"_id":guild.id}) == 0:

            mod.insert_one({"_id":guild.id, "Nome":guild.name})

        mod.update_one({"_id": guild.id}, {'$set': {opt: {'True?':oq,'id':id}}}, upsert = True)

async def logs(opt,oq,guild,id, webhook):

    if opt is not None:

        if mod.count_documents({"_id":guild.id}) == 0:

            mod.insert_one({"_id":guild.id, "Nome":guild.name})

        mod.update_one({"_id": guild.id}, {'$set': {opt: {'True?': oq,'id': id, 'webhook': webhook}}},upsert = True)

async def adcadvdb(guild, author, member, qnt, motivo):

    advdb.update_one( { "_id":f'{guild.id}_{member.id}'}, {'$set':{qnt:[author.id,member.id,motivo]}}, upsert = True )

async def rmvadvdb(guild,author,member, qnt, motivo):

    advdb.update_one( { "_id":f'{guild.id}_{member.id}'}, {'$unset':{qnt:[author,member.id,motivo]}})