# 15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
# nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);

# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;

# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;

# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;

# e. determinar si algún país tiene más de una maravilla del mismo tipo;

# f. deberá utilizar un grafo no dirigido.
from grafo import Graph
grafo = Graph(dirigido=False) 

# Lista con las maravillas segun los requisitos
maravillas = [
    {"nombre": "Machu Picchu", "pais": ["Perú"], "tipo": "arquitectonica"},
    {"nombre": "Chichén Itzá", "pais": ["México"], "tipo": "arquitectonica"},
    {"nombre": "Cristo Redentor", "pais": ["Brasil"], "tipo": "arquitectonica"},
    {"nombre": "Coliseo de Roma", "pais": ["Italia"], "tipo": "arquitectonica"},
    {"nombre": "Taj Mahal", "pais": ["India"], "tipo": "arquitectonica"},
    {"nombre": "Gran Muralla China", "pais": ["China"], "tipo": "arquitectonica"},
    {"nombre": "Petra", "pais": ["Jordania"], "tipo": "arquitectonica"},
    {"nombre": "Gran Cañón", "pais": ["Estados Unidos"], "tipo": "natural"},
    {"nombre": "Aurora Boreal", "pais": ["Canadá", "Noruega", "Finlandia"], "tipo": "natural"},
    {"nombre": "Parque Nacional de Komodo", "pais": ["Indonesia"], "tipo": "natural"},
    {"nombre": "Monte Everest", "pais": ["Nepal", "China"], "tipo": "natural"},
    {"nombre": "Cataratas del Iguazú", "pais": ["Argentina", "Brasil"], "tipo": "natural"},
    {"nombre": "Isla Jeju", "pais": ["Corea del Sur"], "tipo": "natural"},
    {"nombre": "Montaña de la Mesa", "pais": ["Sudáfrica"], "tipo": "natural"},
    # Otra maravilla arquitectónica en Brasil para el ultimo punto
    {"nombre": "Otro Monumento", "pais": ["Brasil"], "tipo": "arquitectonica"}
]

# Insertamos cada maravilla como vertices
for maravilla in maravillas:
    grafo.insert_vertice(maravilla["nombre"])

# Ahora declaramos la relaciones entre maravillas (aristas) donde esta el inicio-destino-distancia
relaciones = [
    ("Machu Picchu", "Chichén Itzá", 4190), ("Machu Picchu", "Cristo Redentor", 3320),
    ("Machu Picchu", "Coliseo de Roma", 10570), ("Machu Picchu", "Taj Mahal", 17240),
    ("Machu Picchu", "Gran Muralla China", 17980), ("Machu Picchu", "Petra", 12890),
    ("Chichén Itzá", "Cristo Redentor", 6610), ("Chichén Itzá", "Coliseo de Roma", 9320),
    ("Chichén Itzá", "Taj Mahal", 14440), ("Chichén Itzá", "Gran Muralla China", 12300),
    ("Chichén Itzá", "Petra", 11720), ("Cristo Redentor", "Coliseo de Roma", 9160),
    ("Cristo Redentor", "Taj Mahal", 14050), ("Cristo Redentor", "Gran Muralla China", 17590),
    ("Cristo Redentor", "Petra", 12150), ("Coliseo de Roma", "Taj Mahal", 5960),
    ("Coliseo de Roma", "Gran Muralla China", 8180), ("Coliseo de Roma", "Petra", 2320),
    ("Taj Mahal", "Gran Muralla China", 3210), ("Taj Mahal", "Petra", 4310),
    ("Gran Muralla China", "Petra", 6840), ("Gran Cañón", "Aurora Boreal", 3500),
    ("Gran Cañón", "Parque Nacional de Komodo", 13800), ("Gran Cañón", "Monte Everest", 12400),
    ("Gran Cañón", "Cataratas del Iguazú", 8230), ("Gran Cañón", "Isla Jeju", 10390),
    ("Gran Cañón", "Montaña de la Mesa", 16130), ("Aurora Boreal", "Parque Nacional de Komodo", 10120),
    ("Aurora Boreal", "Monte Everest", 6170), ("Aurora Boreal", "Cataratas del Iguazú", 10920),
    ("Aurora Boreal", "Isla Jeju", 6980), ("Aurora Boreal", "Montaña de la Mesa", 13440),
    ("Parque Nacional de Komodo", "Monte Everest", 5470), ("Parque Nacional de Komodo", "Cataratas del Iguazú", 16900),
    ("Parque Nacional de Komodo", "Isla Jeju", 3980), ("Parque Nacional de Komodo", "Montaña de la Mesa", 11070),
    ("Monte Everest", "Cataratas del Iguazú", 16350), ("Monte Everest", "Isla Jeju", 4750),
    ("Monte Everest", "Montaña de la Mesa", 9430), ("Cataratas del Iguazú", "Isla Jeju", 18560),
    ("Cataratas del Iguazú", "Montaña de la Mesa", 8420), ("Isla Jeju", "Montaña de la Mesa", 13220)
]

# Insertamos las aristas
for origen, destino, distancia in relaciones:
    grafo.insert_arista(origen, destino, distancia)

# # Ahora encontramos el arbol de expansion minima para los 2 tipos de maravillas
# print("Árbol de expansión mínima para maravillas arquitectónicas:")
# arbol_arquitectonico = grafo.kruskal("Machu Picchu")  
# print(arbol_arquitectonico)

# print("\nÁrbol de expansión mínima para maravillas naturales:")
# arbol_natural = grafo.kruskal("Gran Cañón")  
# print(arbol_natural)

# subgrafos para cada tipo de maravilla
grafo_arquitectonico = Graph(dirigido=False)
grafo_natural = Graph(dirigido=False)

# funcion para obtener el tipo en las maravillas
def obtener_tipo(nombre, maravillas):
    for m in maravillas:
        if m["nombre"] == nombre:
            return m["tipo"]
    return None 

# insertamos las maravillas(vertices)
for maravilla in maravillas:
    nombre = maravilla["nombre"]
    tipo = maravilla["tipo"]
    if tipo == "arquitectonica":
        grafo_arquitectonico.insert_vertice(nombre)
    elif tipo == "natural":
        grafo_natural.insert_vertice(nombre)

# insertamos las aristas(caminos)
for origen, destino, distancia in relaciones:
    tipo_origen = obtener_tipo(origen, maravillas)
    tipo_destino = obtener_tipo(destino, maravillas)
    if tipo_origen == "arquitectonica" and tipo_destino == "arquitectonica":
        grafo_arquitectonico.insert_arista(origen, destino, distancia)
    elif tipo_origen == "natural" and tipo_destino == "natural":
        grafo_natural.insert_arista(origen, destino, distancia)

# kruskal en cada arbol
print("Árbol de expansión mínima para maravillas arquitectónicas:")
arbol_arquitectonico = grafo_arquitectonico.kruskal("Machu Picchu")
print(arbol_arquitectonico)

print("\nÁrbol de expansión mínima para maravillas naturales:")
arbol_natural = grafo_natural.kruskal("Gran Cañón")
print(arbol_natural)


# paises con los 2 tipos de maravillas simultaneamente
paises_con_tipos = {}
for maravilla in maravillas:
    for pais in maravilla["pais"]:
        if pais not in paises_con_tipos:
            paises_con_tipos[pais] = set()
        paises_con_tipos[pais].add(maravilla["tipo"])


paises_ambos_tipos = [pais for pais, tipos in paises_con_tipos.items() if len(tipos) > 1]
print("\nPaíses con maravillas arquitectónicas y naturales:", paises_ambos_tipos)

# cantidad de maravillas por tipo y pais
maravillas_por_pais_y_tipo = {}
for maravilla in maravillas:
    for pais in maravilla["pais"]:
        if pais not in maravillas_por_pais_y_tipo:
            maravillas_por_pais_y_tipo[pais] = {"arquitectonica": 0, "natural": 0}
        maravillas_por_pais_y_tipo[pais][maravilla["tipo"]] += 1

# se imprime el pais con mas de una maravilla de cada tipo
paises_con_multiples_maravillas = {
    pais: tipos for pais, tipos in maravillas_por_pais_y_tipo.items() if any(cant > 1 for cant in tipos.values())
}

print("\nPaíses con más de una maravilla del mismo tipo:", paises_con_multiples_maravillas)

