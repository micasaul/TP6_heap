# Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:

from Cola import Queue

cola = Queue()

personajes = [
    {'nombre': 'Luke Skywalker', 'planeta': 'Tatooine'},
    {'nombre': 'Han Solo', 'planeta': 'Corellia'},
    {'nombre': 'Yoda', 'planeta': 'Dagobah'},
    {'nombre': 'Leia Organa', 'planeta': 'Alderaan'},
    {'nombre': 'Darth Vader', 'planeta': 'Tatooine'},
    {'nombre': 'Obi-Wan Kenobi', 'planeta': 'Stewjon'},
    {'nombre': 'Chewbacca', 'planeta': 'Kashyyyk'},
    {'nombre': 'Jar Jar Binks', 'planeta': 'Naboo'},
    {'nombre': 'Palpatine', 'planeta': 'Naboo'},
]

for personaje in personajes:
    cola.arrive(personaje)

# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
def planetas (cola, planeta):
    for i in range(cola.size()):
        personaje= cola.on_front()
        if personaje['planeta'] == planeta:
            print(f"{personaje['nombre']} del planeta {planeta}")
        cola.move_to_end()
planetas(cola, "Alderaan")
planetas(cola, "Endor")
planetas(cola, "Tatooine")
print()

# b. indicar el plantea natal de Luke Skywalker y Han Solo
def nombres (cola, nombre):
    for i in range(cola.size()):
        personaje= cola.on_front()
        if personaje['nombre'] == nombre:
            print(f"{nombre} del planeta {personaje['planeta']}")
        cola.move_to_end()
nombres(cola, "Luke Skywalker")
nombres(cola, "Han Solo")
print()

# c. insertar un nuevo personaje antes del maestro Yoda
def new (cola, nuevo, key):
    for i in range(cola.size()):
        personaje= cola.on_front()
        if personaje['nombre'] == key:
            cola.arrive(nuevo)
        cola.move_to_end()
new(cola, {'nombre': 'Lando Calrissian', 'planeta': 'Socorro'}, "Yoda")

# d. eliminar el personaje ubicado después de Jar Jar Binks
def eliminar (cola, key):
    for i in range(cola.size()):
        personaje= cola.on_front()
        if personaje['nombre'] == key:
            cola.move_to_end()
            cola.attention()
        cola.move_to_end()    
eliminar(cola, "Jar Jar Binks")

for i in range(cola.size()):
    personaje= cola.on_front()
    print(personaje)
    cola.move_to_end()