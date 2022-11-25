from pymongo import MongoClient
from main import configData

cluster = MongoClient(configData['mongokey'])
db = cluster[configData['database']]
mod = db['MOD']
advdb = db['ADV']

class dbmoderation:

    def lang(opt,oq,guild):

        if opt is not None:
            if mod.count_documents({"_id":guild.id}) == 0:
                mod.insert_one({"_id":guild.id, "Nome":guild.name})
            mod.update_one({"_id": guild.id}, {"$set": {f"{opt}": oq}}, upsert = True)

    def autorole(opt,oq,guild,id):

        if opt is not None:
            if mod.count_documents({"_id":guild.id}) == 0:
                mod.insert_one({"_id":guild.id, "Nome":guild.name})
            mod.update_one({"_id": guild.id}, {'$set': {opt: {'True?':oq,'id':id}}}, upsert = True)

    def logs(opt,oq,guild,id, webhook):

        if opt is not None:
            if mod.count_documents({"_id":guild.id}) == 0:
                mod.insert_one({"_id":guild.id, "Nome":guild.name})
            mod.update_one({"_id": guild.id}, {'$set': {opt: {'True?': oq,'id': id, 'webhook': webhook}}},upsert = True)

    def adcadvdb(guild, author, member, qnt, motivo):
        advdb.update_one( { "_id":f'{guild.id}_{member.id}'}, {'$set':{qnt:[author.id,member.id,motivo]}}, upsert = True )

    def rmvadvdb(guild,author,member, qnt, motivo):
        advdb.update_one( { "_id":f'{guild.id}_{member.id}'}, {'$unset':{qnt:[author,member.id,motivo]}})

    def msgtckid(id, guild):

        if id is not None:
            if mod.count_documents({"_id":guild.id}) == 0:
                mod.insert_one({"_id":guild.id, "Nome":guild.name})
            mod.update_one({"_id": guild.id}, {"$set": {"msgtck": id}}, upsert = True)