from fastapi import FastAPI #IMPORTAMOS LAS LIBERIAS/DEPENDENCIAS QUE VAMOS A UTILIZAR 
import pandas as pd
from pandasql import sqldf

df_unificado=pd.read_csv(r'series_peliculas_completo_2') #IMPORTAMOS EL ARCHIVO A PANDAS DEL CUAL LA INFORMACION SERA SUSTRAIDA
pysqldf = lambda q: sqldf(q, globals())
app=FastAPI()                #CREAMOS UNA INSTANCIA DE  FASTAPI

#Bienvenida a la api

@app.get("/")
def bienvenida():
    return "Te doy la binvenida a mi api!, para las consultas coloca /docs en la barra de direcciones"

#Consigna 1: Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

@app.get('/get_word_count/{plataforma},{titulo}') # DEFINIMOS LA RUTA DE ACCESO 
async def get_word_count(plataforma:str, titulo:str): #CREAMOS LA FUNCION PARA REALIZAR LA CONSIGNA
    if plataforma == 'amazon':                        
        veces_a=pysqldf(f'''select sum(length(title)-length(replace(title, '{titulo}','')))/length('{titulo}')
        as cantidad from df_unificado where id like 'A%' ''').to_string()
        return  veces_a, ' En la plataforma, Amazon'

    if plataforma == 'disney':
        veces_d=pysqldf(f'''select sum(length(title)-length(replace(title, '{titulo}','')))/length('{titulo}')
        as cantidad from df_unificado where id like 'D%' ''').to_string()
        return veces_d, 'En la plataforma, Disney'
    if plataforma== 'hulu':
        veces_h=pysqldf(f'''select sum(length(title)-length(replace(title, '{titulo}','')))/length('{titulo}')
        as cantidad from df_unificado where id like 'H%' ''').to_string()
        return veces_h, 'En la plataforma, Hulu'
    if plataforma== 'netflix':
        veces_n=pysqldf(f'''select sum(length(title)-length(replace(title, '{titulo}','')))/length('{titulo}')
        as cantidad from df_unificado where id like 'N%' ''').to_string()
        return veces_n,'En la plataforma, Netflix'
    else:
        return 'La plataforma ingresada es incorrecta, ingrese entre las opciones: netflix, hulu, disney, amazon'
    
#Consigna 2: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.

@app.get('/get_score_count/{plataforma}, {puntaje}, {ano}') # DEFINIMOS LA RUTA DE ACCESO 
async def get_score_count(plataforma:str,puntaje:int,ano:int):#CREAMOS LA FUNCION PARA REALIZAR LA CONSIGNA


    if plataforma == 'amazon':
        puntaje_a=pysqldf(f'''select count(*) as cantidad from df_unificado 
        where id like 'A%' and type == 'movie' and score >'{puntaje}' and release_year=='{ano}' ''' ).to_string()
        return  puntaje_a, 'en Amazon'
    if plataforma == 'disney':
        puntaje_d=pysqldf(f'''select count(*) as cantidad from df_unificado 
        where id like 'D%' and type == 'movie' and score >'{puntaje}' and release_year=='{ano}' ''' ).to_string()
        return puntaje_d, 'en Disney'
    if plataforma== 'hulu':
        puntaje_h=pysqldf(f'''select count(*) as cantidad from df_unificado 
        where id like 'H%' and type == 'movie' and score >'{puntaje}' and release_year=='{ano}' ''' ).to_string()
        return puntaje_h,'en Hulu'
    if plataforma== 'netflix':
        puntaje_n=pysqldf(f'''select count(*) as cantidad from df_unificado 
        where id like 'N%' and type == 'movie' and score >'{puntaje}' and release_year=='{ano}' ''' ).to_string()
        return puntaje_n, ' en Netflix'
    else:
        return 'La plataforma ingresada es incorrecta, ingrese entre las opciones: netflix, hulu, disney, amazon'

#Consigna 3: La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

@app.get('/get_second_score/{plataforma}') # DEFINIMOS LA RUTA DE ACCESO 
async def get_second_score(plataforma:str):#CREAMOS LA FUNCION PARA REALIZAR LA CONSIGNA
    if plataforma == 'amazon':             
        seg_pel_a=pysqldf(f'''select title as titulo from df_unificado where type=='movie' 
        and id like 'A%' order by score desc, title limit 1 offset 1''').to_string()
        return seg_pel_a, 'en Amazon'
    if plataforma == 'hulu':
        seg_pel_h=pysqldf(f'''select title as titulo from df_unificado where type=='movie' 
        and id like 'H%' order by score desc, title limit 1 offset 1''').to_string()
        return seg_pel_h, 'en Hulu'
    if plataforma == 'disney':
        seg_pel_d=pysqldf(f'''select title as titulo from df_unificado where type=='movie' 
        and id like 'D%' order by score desc, title limit 1 offset 1''').to_string()
        return seg_pel_d, 'en Disney'
    if plataforma == 'netflix':
        seg_pel_n=pysqldf(f'''select title as titulo from df_unificado where type=='movie' 
        and id like 'N%' order by score desc, title limit 1 offset 1''').to_string()
        return seg_pel_n, 'en Netflix'
    else:
        return 'La plataforma ingresada es incorrecta, ingrese entre las opciones: netflix, hulu, disney, amazon'

#Consigna 4: Película que más duró según año, plataforma y tipo de duración

@app.get('/get_longest/{plataforma}, {tipo_duracion}, {ano}') # DEFINIMOS LA RUTA DE ACCESO 
async def get_longest(plataforma:str, tipo_duracion:str, ano:int):#CREAMOS LA FUNCION PARA REALIZAR LA CONSIGNA
    if plataforma== 'amazon':
        pel_mas_duro=pysqldf(f''' select title as titulo from df_unificado
        where release_year=='{ano}' and duration_type=='{tipo_duracion}' and id like 'A%' order by duration_int desc limit 1''').to_string()
        return pel_mas_duro, 'en amazon'
        
    if plataforma== 'netflix':
        pel_mas_duro=pysqldf(f''' select title as titulo from df_unificado
        where release_year=='{ano}' and duration_type=='{tipo_duracion}' and id like 'N%' order by duration_int desc limit 1''').to_string()
        return pel_mas_duro, tipo_duracion, ano, 'en Netflix'
    
    if plataforma== 'hulu':
        pel_mas_duro=pysqldf(f''' select title as titulo from df_unificado
        where release_year=='{ano}' and duration_type=='{tipo_duracion}' and id like 'H%' order by duration_int desc limit 1''').to_string()
        return pel_mas_duro, 'en Hulu'
    if plataforma== 'Disney':
        pel_mas_duro=pysqldf(f''' select title as titulo from df_unificado
        where release_year=='{ano}' and duration_type=='{tipo_duracion}' and id like 'D%' order by duration_int desc limit 1''').to_string()
        return pel_mas_duro, 'en Disney'
    else:
        return 'La plataforma ingresada es incorrecta, ingrese entre las opciones: netflix, hulu, disney, amazon'

#Consigna 5: Cantidad de series y películas por rating

@app.get('/get_rating_count/{rating}') # DEFINIMOS LA RUTA DE ACCESO 
async def get_rating_count(rating:str):#CREAMOS LA FUNCION PARA REALIZAR LA CONSIGNA
    query5=pysqldf(f'''select count(*) as count from df_unificado where rating=='{rating}' ''').to_string()
    return query5