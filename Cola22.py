# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el 
# nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) 
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, 
# Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

from Cola import Queue

cola = Queue()

MCU = [
    {'super': "Black Widow", 'nombre': "Natasha Romanoff", 'genero': "F"},
    {'super': "Thor", 'nombre': "Thor Odinson", 'genero': "M"},
    {'super': "Iron Man", 'nombre': "Tony Stark", 'genero': "M"},
    {'super': "Captain America", 'nombre': "Steve Rogers", 'genero': "M"},
    {'super': "Hulk", 'nombre': "Bruce Banners", 'genero': "M"},
    {'super': None, 'nombre': "Scott Lang", 'genero': "M"},
    {'super': "Capitana Marvel", 'nombre': None, 'genero': "F"},
]

for heroe in MCU:
    cola.arrive(heroe)

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
def actualizar_nom (cola, nombre, super):
    for i in range(cola.size()):
        personaje= cola.on_front()
        if personaje['super'] == super:
            personaje['nombre'] = nombre
        cola.move_to_end()
actualizar_nom(cola, "Carol Danvers", "Capitana Marvel")

# b. mostrar los nombres de los superhéroes femeninos;
def fem (cola):
    print("Los personajes femeninos son: ")
    for i in range(cola.size()):
        personaje= cola.on_front()
        if personaje['genero'] == "F":
            print(personaje['super'])
        cola.move_to_end()
fem(cola)
print()

# c. mostrar los nombres de los personajes masculinos;
def masc (cola):
    print("Los personajes masculinos son: ")
    for i in range(cola.size()):
        personaje= cola.on_front()
        if personaje['genero'] == "M":
            print(personaje['nombre'])
        cola.move_to_end()
masc(cola)
print()

# d. determinar el nombre del superhéroe del personaje Scott Lang;
def actualizar_super (cola, nombre, super):
    for i in range(cola.size()):
        personaje= cola.on_front()
        if personaje['nombre'] == nombre:
            personaje['super'] = super
        cola.move_to_end()
actualizar_super(cola, "Scott Lang", "Ant Man")

# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
def nombre_letra (cola, letra):
    print(f"Los personajes cuyos nombres comienzan con {letra} son: ")
    for i in range(cola.size()):
        personaje= cola.on_front()
        if personaje['nombre'].startswith(letra) or personaje['super'].startswith(letra):
            print(personaje)
        cola.move_to_end()
nombre_letra(cola, "S")
print()

# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.
def search (cola, nombre):
    for i in range(cola.size()):
        personaje= cola.on_front()
        if personaje['nombre'] == nombre:
            print(personaje['super'])
        cola.move_to_end()
search(cola, "Carol Danvers")