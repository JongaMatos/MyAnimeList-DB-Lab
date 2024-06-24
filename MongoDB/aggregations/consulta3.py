from pymongo import MongoClient
import json
import os
from bson import ObjectId

def nota_media_por_anime():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['MyAnimeList']
    pipeline = [
        {
            '$lookup': {
                'from': 'ANIME',
                'localField': 'animeId',
                'foreignField': 'animeId',
                'as': 'anime'
            }
        },
        { '$unwind': "$anime" },
        {
            '$group': {
                '_id': "$animeId",
                'Title': { '$first': "$anime.title" },
                'QuantidadeReviews': { '$sum': 1 },
                'NotaMediaAnime': { '$avg': "$score" }
            }
        },
        { '$sort': { 'QuantidadeReviews': -1 } }
    ]
    result = list(db.get_collection('REVIEW').aggregate(pipeline))
    client.close()
    
    # Converte ObjectId para string
    for doc in result:
        if isinstance(doc['_id'], ObjectId):
            doc['_id'] = str(doc['_id'])
    
    # Salva os resultados em um arquivo JSON na pasta 'aggregations-result'
    output_dir = 'C:/Users/mateu/OneDrive/Faculdade/2024.1/Sistemas de Banco de Dados II/trabalhos/TF/MyAnimeList-DB-Lab/MongoDB/aggregations-result'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'nota_media_por_anime.json')
    
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=4)
    
    return result
