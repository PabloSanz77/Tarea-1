import random
import timeit

from bisect import bisect_left
#DEFINICION DE LA CLASE
class Usuario:
    def __init__(self, user_id, nombre, edad): #init ASIGNA VALORES AL USUARIO (CONSTRUCTOR)
        self.id = user_id
        self.nombre = nombre
        self.edad = edad

    def __repr__(self): #repr DEFINE LA REPRESENTACION DE UN OBJETO (METODO)
        return f"Usuario(ID={self.id}, Nombre={self.nombre}, Edad={self.edad})"

nombres = ["PABLO", "LUIS", "MAYRO", "JOSE", "ALBERTO", "DANIEL", "EMILIO", "MARIA", "PEDRO", "MISAEL"]
usuarios = [Usuario(i, random.choice(nombres), random.randint(18, 80)) for i in range(100000)]

def busqueda_lineal(lista, user_id):
    for usuario in lista:
        if usuario.id == user_id:
            return usuario
    return None


def busqueda_binaria(lista, user_id):
    indices = [usuario.id for usuario in lista]  # Extraer los IDs
    idx = bisect_left(indices, user_id)
    if idx != len(lista) and lista[idx].id == user_id:
        return lista[idx]
    return None


id_a_buscar = random.randint(0, 99999)

#TIEMPOS DE LA EJECUCION
lineal_tiempo = timeit.timeit(lambda: busqueda_lineal(usuarios, id_a_buscar), number=1)
binaria_tiempo = timeit.timeit(lambda: busqueda_binaria(usuarios, id_a_buscar), number=1)

print(f"Tiempo búsqueda lineal: {lineal_tiempo:.6f} segundos")
print(f"Tiempo búsqueda binaria: {binaria_tiempo:.6f} segundos")
