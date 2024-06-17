from csv_json_utils import *


def clear_file(file_path):
    file = open(file_path, 'w')
    file.write('')
    file.close()


def gera_sql_ANIME(file):
    animes = get_json_data('animes')

    file.write(
        "INSERT INTO ANIME (animeId, title, synopsis, aired, episodes, members, score, img_url, link ) VALUES\n")

    for i in range(len(animes)):
        anime = animes[i]
        
        if (i >= len(animes)-1):
            file.write(f"({int(anime['animeId'])}, {repr(anime['title'])}, {repr(anime['synopsis'])}, {repr(anime['aired'])}, {int_or_null(anime['episodes'])}, {int(anime['members'])}, {float_or_null(anime['score'])}, {repr(anime['img_url'])}, {repr(anime['link'])});")
        else:
            file.write(f"({int(anime['animeId'])}, {repr(anime['title'])}, {repr(anime['synopsis'])}, {repr(anime['aired'])}, {int_or_null(anime['episodes'])}, {int(anime['members'])}, {float_or_null(anime['score'])}, {repr(anime['img_url'])}, {repr(anime['link'])}),")
        file.write("\n")


def gera_sql_GENRE(file, genres):

    file.write(
        "INSERT INTO GENRE (genreId, name ) VALUES\n")
    
    for i in range(len(genres)):
        genre = genres[i]
        
        if (i >= len(genres)-1):
            file.write(f"({genre['id']}, \"{genre['name']}\");")
        else:
            file.write(f"({genre['id']}, \"{genre['name']}\"),")

        file.write("\n")


def gera_sql_anime_genre(file, anime_genres):

    file.write(
        "INSERT INTO anime_genre (animeId, genreId ) VALUES\n")
    for i in range(len(anime_genres)):
        anime_genre = anime_genres[i]
        if (i >= len(anime_genres)-1):
            file.write(
                f"({anime_genre['animeId']}, {anime_genre['genreId']});")
        else:
            file.write(
                f"({anime_genre['animeId']}, {anime_genre['genreId']}),")

        file.write("\n")


def get_gender(gender):
    if (gender == "Male"):
        return 1
    if (gender == "Female"):
        return 2
    return "Null"


def gera_sql_PROFILE(file):
    profiles = get_json_data('profiles')

    file.write(
        "INSERT INTO PROFILE (profile, gender, birthday, link ) VALUES\n")
    for i in range(len(profiles)):
        profile = profiles[i]
        if (i >= len(profiles)-1):
            file.write(
                f"(\"{profile['profile']}\", {get_gender(profile['gender'])}, \"{profile['birthday']}\", \"{profile['link']}\");")
        else:
            file.write(
                f"(\"{profile['profile']}\", {get_gender(profile['gender'])}, \"{profile['birthday']}\", \"{profile['link']}\"),")

        file.write("\n")


def gera_sql_favorites(file, favorites):

    file.write(
        "INSERT INTO favorite (profile, animeId ) VALUES\n")
    for i in range(len(favorites)):
        favorite = favorites[i]
        if (i >= len(favorites)-1):
            file.write(
                f"(\"{favorite['profile']}\", {int(favorite['animeId'])});")
        else:
            file.write(
                f"(\"{favorite['profile']}\", {int(favorite['animeId'])}),")

        file.write("\n")


def gera_sql_REVIEW(file):
    reviews = get_json_data('reviews')

    file.write(
        "INSERT INTO REVIEW (reviewId, profile, animeId, score) VALUES\n")
    for i in range(len(reviews)):
        review = reviews[i]
        if (i >= len(reviews)-1):
            file.write(
                f"({int(review['reviewId'])},\"{review['profile']}\", {int(review['animeId'])}, {float(review['score'])});")
        else:
            file.write(
                f"({int(review['reviewId'])},\"{review['profile']}\", {int(review['animeId'])}, {float(review['score'])}),")

        file.write("\n")
