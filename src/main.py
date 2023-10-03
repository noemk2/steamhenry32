from typing import Union
from fastapi import FastAPI
# from src.utils import userdata, countre_views, gen_re, user_forgenre, dev_eloper, sentimentanalysis
from src.utils import playtimegenre, userforgenre, userrecommend, usernotrecommend, sentiment, recomendacionusuario

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# API : steam


@app.get("/PlayTimeGenre/{genre}")
def PlayTimeGenre(genre):
    return playtimegenre(genre)


@app.get("/UserForGenre/{genre}")
def UserForGenre(genre):
    return userforgenre(genre)


@app.get("/UsersRecommend/{year}")
def UsersRecommend(year):
    return userrecommend(year)


@app.get("/UsersNotRecommend/{year}")
def UsersNotRecommend(year):
    return usernotrecommend(year)


@app.get("/sentiment_analysis/{year}")
def sentiment_analysis(year):
    return sentiment(year)

@app.get("/recomendacion_usuario/{user_id}")
def recomendacion_usuario(user_id):
    return recomendacionusuario(user_id)
