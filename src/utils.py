import pandas as pd
import numpy as np
import os
from numpy import nan
from sklearn import linear_model
from sklearn.metrics.pairwise import cosine_similarity

# from datetime import datetime


def playtimegenre(genre):
    df = pd.read_csv(file_direct("tarea1.csv"))
    df.set_index('genres', inplace=True)
    # print(df)
    response = df.loc[genre].idxmax()
    print(response)
    return response


def userforgenre(genre):
    #no lo hice
    pass


def userrecommend(year):
#    print(type(year))
    df = pd.read_csv(file_direct("tarea3.csv"))
    df.set_index('release_date', inplace=True)
    # print(df)
    year_data = df.loc[int(year)]
    sorted_values = year_data.sort_values(ascending=False)
    X = sorted_values.index[0]
    Y = sorted_values.index[1]
    Z = sorted_values.index[2]

    return [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]


def usernotrecommend(year):
    #print(type(year))
    df = pd.read_csv(file_direct("tarea4.csv"))
    df.set_index('release_date', inplace=True)
    # print(df)
    year_data = df.loc[int(year)]
    sorted_values = year_data.sort_values(ascending=False)
    X = sorted_values.index[0]
    Y = sorted_values.index[1]
    Z = sorted_values.index[2]

    return [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]


def sentiment(year):
    df = pd.read_csv(file_direct("tarea5.csv"))
    df.set_index('release_date', inplace=True)
    # print(df)
    tab = df.loc[int(year)]

    negative = str(tab["count_0"].max())
    neutro = str(tab["count_2"].max())
    positive= str(tab["count_1"].max())

    return  { "Negative = " + negative , "Neutral =" + neutro, "Positive = " +positive}


# Función para recomendar elementos a un usuario
def recomendacionusuario(user_id):
    users_pivot = pd.read_csv(file_direct("tarea6.csv"))
    users_pivot.set_index('user_id', inplace=True)

    usuario_objetivo = users_pivot.loc[user_id]
    similarities = cosine_similarity([usuario_objetivo], users_pivot )
    usuario_similar = similarities[0]
    user_index = users_pivot.index.get_loc(user_id)
    usuario_similar[user_index] = -1  # Excluir al propio usuari
    mejores_usuarios = usuario_similar.argsort()[::-1]
    elementos_vistos = usuario_objetivo[usuario_objetivo > 0].index

    recomendaciones = []
    for usuario_sim in mejores_usuarios:
        elementos_recomendados = users_pivot.iloc[usuario_sim]
        elementos_recomendados = elementos_recomendados[elementos_recomendados > 0].index
        elementos_recomendados = [e for e in elementos_recomendados if e not in elementos_vistos]
        recomendaciones.extend(elementos_recomendados)
        if len(recomendaciones) >= 5:
            break

    print(recomendaciones[:5] )
    pass
#    return recomendaciones[:5]  # Limitar a 5 recomendaciones




# usuario_objetivo = '--ace--'
# recomendaciones = recomendacion_usuario(usuario_objetivo, users_pivot)

# print(f"Recomendaciones para {usuario_objetivo}:")
# for i, elemento in enumerate(recomendaciones, 1):
#     print(f"{i}. {elemento}")





# utils
# def file_path(dir_name, file_name):
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     return os.path.join(script_dir, "dataset", dir_name, file_name)


def file_direct(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "dataset", file_name)
