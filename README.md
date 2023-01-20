En este repositorio presentamos documentación así como orientaciones para el desarrollo de una API, tarea  que se requiere como proyecto dentro de la formación profesional, como parte del área de Data Engineering. 
Desde el área de análisis de datos,se nos solicitan ciertos requerimientos para el desarrollo de las actividades. Estos comprenden  elaborar las transformaciones requeridas a los Data Sets provistos y  disponibilizar los datos mediante la elaboración y ejecución de una API.

DATA SETS PROVISTOS
Ubicados en la carpeta CSV_PLATAFORMAS

TRANSFORMACIÓN DE DATOS
proceso_etl.ipynb (transformación de datos ETL)

En el archivo 'proceso_etl.ipynb', encontraremos secuenciados los pasos para realizar el proceso de transformación de los datos. Las transformaciones de datos que se nos solicitan son las siguientes:

1_Generar campo ID: Cada ID se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya   presente en los datasets (ejemplo para títulos de Amazon = as123).

2_Reemplazar Los valores nulos del campo rating  por el string “G” (corresponde al maturity rating: “general for all audiences”).

3_De haber fechas, habrán de seguir el formato AAAA-mm-dd.

4_Los campos de texto tendrán que estar en minúsculas, sin excepción.

5_El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string. En el string, debe indicarse la unidad de medición de duración: min (minutos) o season (temporadas)

RESTO DE LOS ARCHIVOS Y CARPETAS DISPONIBLES EN EL REPOSITORIO

ycache - Es una carpeta necesaria para que funcione API.
README - Archivo en el que se lee la información que necesitamos para utilizar el repositorio y sus formas.
main.py - el código de la API
movies_completo.csv - el csv que se utiliza para las consultas.
requirements.txt - dependencias necesarias para que funcione la API.
main.py - código que crea la API


CONSULTAS QUE SE REQUIERE QUE LA API RESPONDA (ubicadas en el archivo main.py) Y CÓMO EJECUTARLAS

1_Cantidad de veces que aparece una keyword en el título de películas/series, por plataforma:
Para poder ejecutar esta consulta se debe optar entre las plataformas, 'amazon', 'disney','hulu' y 'netflix', las mismas han de ingresarse con letras minúsculas y luego colocar el título a buscar, también en minuscula.

2_Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año:
Para poder ejecutar esta consulta debemos escoger entre las plataformas, 'amazon', 'disney','hulu' y 'netflix', las mismas deben ingresarse con letras minúsculas, luego colocar cuál sería- mediante un número entero- el puntaje mayor solicitado al mismo y también el año que se desea buscar,en número entero.

3_La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos:
Para poder ejecutar esta consulta  se necesita preferir entre las plataformas, 'amazon', 'disney','hulu' y 'netflix', las que recordamos deben ingresarse con letras minúsculas.

4_Película que más duró, según año, plataforma y tipo de duración:
Para poder ejecutar esta consulta es preciso optar entre las plataformas, 'amazon', 'disney','hulu' y 'netflix'. Las mismas deben ingresarse con letras minúsculas; luego colocar cuál sería, mediante un número entero, el año y también el el tipo de duración que es de dos tipos, 'min' o 'season', registrados también en letras minúsculas

5_Cantidad de series y películas por rating:
Para ejecutar esta consulta se debe consignar el rating con el que se quiere filtrar la serie o film. Para ello, se coloca un número de rating y el código de la API filtra la cantidad de series y películas que poseen un valor mayor rating que el número indicado.

Para ejecutar las consultas utilizaMOS la nube DETA. El siguiente link nos muestra paso a paso cómo implementar FasApi en esta nube: https://fastapi.tiangolo.com/deployment/deta/#__tabbed_1_2 

Para entrar a la nube y ejecutar FasApi en DETA, como está realizado en este README, debemos ingresar en el buscador la dirección: https://1em2op.deta.dev donde se nos ofreceuna guía acerca de  cómo ejecutar las consultas.

Si se quieren realizar las consultas desde el navegador, debemos recurrir a  las siguientes direciones:

◽ https://twj1kq.deta.dev/get_word_count/{plataforma}/{titulo}
◽ https://twj1kq.deta.dev/get_score_count/{plataforma}/{puntaje}/{ano}
◽ https://twj1kq.deta.dev/get_second_score/{plataforma}
◽ https://twj1kq.deta.dev/get_longest/{plataforma}/{tipo_duracion}/{ano}
◽ https://twj1kq.deta.dev/get_rating_count/{rating}


En el siguiente enlace de YouTube encontraran el video explicativo: https://youtu.be/hi5ab4o1-a4