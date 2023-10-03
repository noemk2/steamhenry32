# Proyecto de Machine Learning (MLOps) - Sistema de Recomendación de Juegos en Steam

## Introducción

Este proyecto se centra en el desarrollo de un sistema de recomendación de juegos para la plataforma Steam. El objetivo principal es predecir cinco juegos que podrían gustar a un usuario en función de su historial de juego y reseñas. 

+ [Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj) 
+ [Diccionario de datos](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link) 
<br/>


## Video 
Se incluye un video de 7min explicando el proyecto:
https://steamhenry.onrender.com


Para lograr esto, se ha creado un API web que proporciona diversas funcionalidades relacionadas con el análisis de datos y la generación de recomendaciones. El API está alojado en https://steamhenry.onrender.com y ofrece los siguientes endpoints:

### 1. `def PlayTimeGenre( genre : str )`: Debe devolver año con mas horas jugadas para dicho género.
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

### 2. `def UserForGenre( genre: str )`: Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

### 3. `def UsersRecommend( year: int )`: Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

### 4. `def UsersNotRecommend( year: int )`: Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

### 5. `def sentiment_analysis( year: int )`: Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}



## Exploración de Datos y Desarrollo del Modelo

El proceso de desarrollo de este sistema de recomendación se encuentra documentado en el archivo EDA_Steami.pynb (Jupyter Notebook) o EDA_Steami.pdf. En este documento se detalla la carga de los datos, la exploración de los mismos y el estudio de la variable "recommend". Además, se describen las etapas de preprocesamiento de datos, creación del modelo de recomendación y evaluación de errores.

El objetivo principal del modelo es generar recomendaciones precisas y personalizadas para los usuarios de Steam, lo que mejora la experiencia del usuario y puede aumentar la retención en la plataforma.

El proyecto combina elementos de Machine Learning y MLOps para garantizar un flujo de trabajo eficiente y la implementación de un modelo de recomendación en producción a través del API web mencionado anteriormente.

El código y los detalles técnicos específicos se encuentran en el repositorio del proyecto, que está disponible en [URL del repositorio](https://github.com/noemk2/steamhenry/src).

Este README.md proporciona una descripción general del proyecto y su funcionalidad, mientras que el archivo EDA_Steami.pynb o EDA_Steami.pdf contiene los detalles técnicos y los resultados obtenidos en el proceso de desarrollo.

¡Esperamos que este sistema de recomendación de juegos en Steam sea útil y proporcione recomendaciones emocionantes a los usuarios de la plataforma!