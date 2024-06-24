from pymongo import MongoClient
import json
import os
from bson import ObjectId

def quantidade_animes_por_genero():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['MyAnimeList']
    pipeline = [
        { '$unwind': "$genre" },
        { '$group': { '_id': "$genre", 'quantidadeAnimes': { '$sum': 1 } } },
        { '$sort': { 'quantidadeAnimes': -1 } }
    ]
    result = list(db.get_collection('ANIME').aggregate(pipeline))
    client.close()
    
    for doc in result:
        if isinstance(doc['_id'], ObjectId):
            doc['_id'] = str(doc['_id'])
    
    output_dir = 'C:/Users/mateu/OneDrive/Faculdade/2024.1/Sistemas de Banco de Dados II/trabalhos/TF/MyAnimeList-DB-Lab/MongoDB/aggregations-result'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'quantidade_animes_por_genero.json')
    
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=4)
    
    return result
