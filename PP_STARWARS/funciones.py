import json

##lista_personajes
data_json = (r"C:\Users\Frank\Desktop\Programación & Laboratorio I\EXAMEN\PP_STARWARS\PP_STARWARS\data.json")

def cargar_json(dicc:list):
    with open(data_json, "r") as file:
        lista_personajes = json.load(file) 
        lista_personajes = lista_personajes["results"]  
        return lista_personajes

cargar_json(data_json)

def lista_personajes_por_altura(lista_personajes:list):
    
