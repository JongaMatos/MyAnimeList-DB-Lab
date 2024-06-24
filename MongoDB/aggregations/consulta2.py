from pymongo import MongoClient
import json
import os
from bson import ObjectId

def quantidade_avaliacoes_por_perfil():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['MyAnimeList']
    db.get_collection('PROFILE').create_index([('profile', 1)])
    db.get_collection('REVIEW').create_index([('profile', 1)])
    pipeline = [
        {
            '$lookup': {
                'from': 'REVIEW',
                'localField': 'profile',
                'foreignField': 'profile',
                'as': 'reviews'
            }
        },
        {
            '$project': {
                'profile': 1,
                'quantidadeAvaliacoes': { '$size': "$reviews" },
                'NotaMediaAtribuida': { '$avg': "$reviews.score" }
            }
        },
        { '$limit': 1000 },
        { '$sort': { 'quantidadeAvaliacoes': -1 } }
    ]
    result = list(db.get_collection('PROFILE').aggregate(pipeline))
    client.close()
    
    for doc in result:
        if isinstance(doc['_id'], ObjectId):
            doc['_id'] = str(doc['_id'])
    
    output_dir = 'C:/Users/mateu/OneDrive/Faculdade/2024.1/Sistemas de Banco de Dados II/trabalhos/TF/MyAnimeList-DB-Lab/MongoDB/aggregations-result'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'quantidade_avaliacoes_por_perfil.json')
    
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=4)
    
    return result
