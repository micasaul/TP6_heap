# El general Hux es la persona encargada de administrar todas las operaciones de la base Starkiller,
# para lo cual nos solicita desarrollar un algoritmo que permita controlar las actividades que
# se realizan, contemplando lo siguiente:
# d. opcionalmente se podrán agregar operaciones luego de atender una;

from Heap import HeapMax

operaciones= HeapMax()

# b. de cada actividad se conoce quien es el encargado, una descripción, la hora y opcionalmente 
# la cantidad de Stormtroopers requeridos;
actividades = [
    {'encargado': "Phasma", 'descripcion': "Planificación de la ofensiva contra la Resistencia", 'hora': "23:43", 'stormtroopers': "15"},
    {'encargado': "Kylo Ren", 'descripcion': "Inspección de la base Starkiller", 'hora': "02:28", 'stormtroopers': "15"},
    {'encargado': "Snoke", 'descripcion': "Reunión estratégica con los líderes", 'hora': "10:00", 'stormtroopers': "20"},
    {'encargado': "Phasma", 'descripcion': "Entrenamiento de combate", 'hora': "14:30", 'stormtroopers': "25"},
    {'encargado': "General Hux", 'descripcion': "Supervisión de la construcción de la base", 'hora': "16:00", 'stormtroopers': "10"},
    {'encargado': "Kylo Ren", 'descripcion': "Interrogatorio de prisioneros", 'hora': "18:45", 'stormtroopers': "5"},
    {'encargado': "Snoke", 'descripcion': "Meditación en la Fuerza", 'hora': "20:00", 'stormtroopers': "0"},
    {'encargado': "Phasma", 'descripcion': "Patrullaje de seguridad", 'hora': "22:00", 'stormtroopers': "12"},
    {'encargado': "Phasma", 'descripcion': "Inspección de armamento", 'hora': "09:00", 'stormtroopers': "18"},
    {'encargado': "General Hux", 'descripcion': "Revisión de estrategias de defensa", 'hora': "11:30", 'stormtroopers': "22"}
]

# a. debe contemplar distintas prioridades para el control de operaciones de acuerdo al siguiente 
# criterio: pedidos de líder supremo Snoke y de Kylo Ren nivel tres, de capitán Phasma
# nivel dos y el resto de las operaciones nivel a cargo de los generales de la base de nivel uno;
# c. utilizar una cola de prioridad para administrar las distintas operaciones, debe cargar al
# menos ocho: dos de nivel tres, cuatro de nivel dos y cuatro de nivel uno;
for act in actividades:
    if act['encargado'] == "Kylo Ren" or act['encargado'] == "Snoke":
        operaciones.arrive(act, 3)
    elif act['encargado'] == "Phasma":
        operaciones.arrive(act, 2)
    else:
        operaciones.arrive(act, 1)

# e. realizar la atención de las operaciones de la cola;
# f. luego de atender la quinta operación, agregar una operación solicitada por capitán Phasma
# para revisión de intrusos en el hangar B7 que requiere 25 Stormstroopers;
f= {'encargado': "Phasma", 'descripcion': "Revision de intrusos en el hangar B7", 'hora': "11:23", 'stormtroopers': "25"}
# g. luego de atender la sexta operación, agregar una operación solicitada por el líder supremo
# Snoke para destruir el planeta Takodana.
g= {'encargado': "Snoke", 'descripcion': "Destruir al planeta Takodana", 'hora': "03:20", 'stormtroopers': "50"}

c=0
while c<12:
    c+=1
    if c==5:
        operaciones.atention_mas(f, 2)
    elif c==6:
        operaciones.atention_mas(g, 3)
    else: 
        operaciones.atention()
