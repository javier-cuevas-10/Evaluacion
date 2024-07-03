import json
import os


archivo_libros = "biblioteca.json"


def cargar_libros():
    libros = []
    if os.path.exists(archivo_libros):
        with open(archivo_libros, "r") as archivo:
            libros = json.load(archivo)
    return libros




def guardar_libros(libros):
    with open(archivo_libros, "w") as archivo:
        json.dump(libros, archivo, indent=4)



def registrar_libro():
    libros = cargar_libros()
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    genero = input("Ingrese el género del libro: ")
    libro = {"titulo": titulo, "autor": autor, "genero": genero}
    libros.append(libro)
    guardar_libros(libros)
    print(f"Libro '{titulo}' registrado correctamente.")




def buscar_por_autor():
    libros = cargar_libros()
    autor_buscar = input("Ingrese el nombre del autor para buscar libros: ")
    encontrados = []
    for libro in libros:
        if libro["autor"].lower() == autor_buscar.lower():
            encontrados.append(libro)
    if encontrados:
        print(f"Libros encontrados para el autor '{autor_buscar}':")
        for libro in encontrados:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}")
    else:
        print(f"No se encontraron libros del autor '{autor_buscar}'.")