from csv_json_utils import *
from sql_utils import *


def data_from_csv():

    print(f"\nIniciando extração dos dados dos arquivos CSV")
    extract_data()

    # print(f"Iniciando tratamento de dados\n")

    # print(f"    Extraindo associações entre anime e profile (favorites)")
    # get_favorite_anime_by_profile()

    # print(f"\n    Extraindo genres de animes")
    # get_genres()

    # print(f"\n    Extraindo associações entre genres e animes")
    # get_anime_genre()



def gera_sql_popula():

    clear_file('MySQL/popula.sql')

    file = open('MySQL/popula.sql', 'a')

    file.write('USE MyAnimeList;\n\n')

    print(f"Iniciando geração do script popula.sql")

    print(f"    Adicionando dados de 'ANIME'")
    gera_sql_ANIME(file)

    file.write("\n")

    genres = get_genres()
    print(f"    Adicionando dados de 'GENRE'")
    gera_sql_GENRE(file, genres)

    file.write("\n")

    anime_genres = get_anime_genres(genres)
    print(f"    Adicionando dados de 'anime_genre'")
    gera_sql_anime_genre(file, anime_genres)

    file.write("\n")

    print(f"    Adicionando dados de 'PROFILE'")
    gera_sql_PROFILE(file)

    file.write("\n")
    
    favorites=get_favorite_anime_by_profile()
    print(f"    Adicionando dados de 'favorite'")
    gera_sql_favorites(file,favorites)

    file.write("\n")
    print(f"    Adicionando dados de 'review'")
    gera_sql_REVIEW(file)

    file.close()
    print(f"Geração do script popula.sql concluida'")
    


if __name__ == '__main__':

    data_from_csv()

    gera_sql_popula()
