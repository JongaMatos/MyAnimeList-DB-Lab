import json
import csv


def csv_to_json_review(csv_file_path, json_file_name):

    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []

        for row in reader:

            row['reviewId'] = int(row.pop('uid'))
            row['animeId'] = int(row.pop('anime_uid'))
            row["score"] = float(row["score"])
            row['text'] = row["text"].strip()

            scores = eval(row["scores"])

            for key, value in scores.items():
                scores[key] = float_or_null(value)

            row["scores"] = scores
            data.append(row)

    data = remove_duplicate_reviewIds(data)
    animes = get_json_data("animes")
    profiles = get_json_data("profiles")
    data = clean_reviews_data(animes, profiles, data)

    write_to_json(json_file_name, data)


def csv_to_json_anime(csv_file_path, json_file_name):

    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        animeIds = []

        for row in reader:

            row['animeId'] = int(row.pop('uid'))
            if (row['animeId'] not in animeIds):

                row['episodes'] = int_or_null(row['episodes'])
                row['members'] = int(row["members"])
                row['score'] = float_or_null(row["score"])
                row['genre'] = row['genre'].strip(
                    "[]").replace("'", "").split(',')
                genreNew = []

                for genre in row["genre"]:
                    genreNew.append(genre.strip())
                row['genre'] = genreNew

                data.append(row)
                animeIds.append(row['animeId'])

    write_to_json(json_file_name, data)


def csv_to_json_profile(csv_file_path, json_file_name):

    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        profile = []
        for row in reader:
            if (row['profile'] not in profile):

                row['favorites_anime'] = row['favorites_anime'].strip(
                    "[]").replace("'", "").split(',')

                favoriteNew = []

                for favorite in row["favorites_anime"]:
                    if (favorite.strip() != ""):
                        favoriteNew.append(int(favorite.strip()))

                row['favorites_anime'] = favoriteNew
                data.append(row)
                profile.append(row['profile'])

    write_to_json(json_file_name, data)


def write_to_json(filename, data):

    with open(f"json/{filename}.json", 'w') as jsonfile:
        print(f"    Extraindo arquivo {filename}.csv para {filename}.json")
        json.dump(data, jsonfile, indent=4)


def extract_data():
    csv_to_json_anime("csv/animes.csv", "animes")
    csv_to_json_profile("csv/profiles.csv", "profiles")
    csv_to_json_review("csv/reviews.csv", "reviews")

    print(f"Extração dos arquivos CSV concluida\n")


def get_json_data(filename):
    file = open(f"json/{filename}.json")
    return json.load(file)


def remove_duplicate_reviewIds(reviews):

    seen_ids = set()
    unique_data = []
    for review in reviews:
        if review["reviewId"] not in seen_ids:
            unique_data.append(review)
            seen_ids.add(review["reviewId"])
    reviews = unique_data
    return unique_data


def remove_duplicates_set(data):

    unique_dicts = set(tuple(d.items())
                       for d in data)
    data = [dict(item) for item in unique_dicts]

    return data


def remove_non_matching_animeId(dict_array1, dict_array2):

    anime_ids_set = set(
        dict1["animeId"] for dict1 in dict_array1)
    dict_array2[:] = [dict2 for dict2 in dict_array2 if dict2["animeId"]
                      in anime_ids_set]


def clean_reviews_data(animes, profiles, reviews):

    profiles_set = set(
        profile["profile"] for profile in profiles)
    anime_ids_set = set(
        anime["animeId"] for anime in animes)
    reviews[:] = [review for review in reviews if review["animeId"]
                  in anime_ids_set]
    reviews[:] = [review for review in reviews if review["profile"]
                  in profiles_set]
    return reviews


def get_favorite_anime_by_profile():

    array = []
    profiles = get_json_data("profiles")

    for profile in profiles:

        for favorite in profile["favorites_anime"]:
            if favorite != "":
                array.append(
                    {"profile": profile['profile'], "animeId": favorite})

    array = remove_duplicates_set(array)
    animes = get_json_data("animes")
    remove_non_matching_animeId(animes, array)

    return array


def get_genres():
    array1 = []
    array2 = []
    animes = get_json_data("animes")

    for anime in animes:
        genres = anime["genre"]

        for genre in genres:
            genre = genre

            if genre not in array1 and genre != '':
                array1.append(genre)
                array2.append({'id': len(array2)+1, 'name': genre})

    return array2


def get_genre_id_by_name(genres, name):
    for item in genres:
        if item["name"] == name:
            return item["id"]
    return None


def get_anime_genres(genres):
    animes = get_json_data("animes")
    array = []
    for anime in animes:
        anime_genres = anime["genre"]
        for anime_genre in anime_genres:
            genreId = get_genre_id_by_name(genres, anime_genre)
            if (genreId != None):
                if ({"animeId": anime['animeId'], 'genreId': genreId} not in array):
                    array.append(
                        {"animeId": anime['animeId'], 'genreId': genreId})
    return array


def int_or_null(item):
    if (item and item != "Null"):
        return int(float(item))
    return "Null"


def float_or_null(item):
    if (item and item != "Null"):
        return float(item)
    return "Null"
