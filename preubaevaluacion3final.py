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




def mostrar_libros():
    libros = cargar_libros()
    if libros:
        print("\nLista completa de libros:")
        for libro in libros:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}")
    else:
        print("No hay libros registrados.")
def main():
    while True:
        print("\nBienvenido a la Biblioteca")
        print("1. Registrar libro")
        print("2. Buscar libros por autor")
        print("3. Mostrar lista de libros")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            buscar_por_autor()
        elif opcion == "3":
            mostrar_libros()
        elif opcion == "4":
            print("Gracias por usar la Biblioteca ¡Hasta luego!")
            break
        else:
            print("Opción incorrecta. Intente nuevamente.")
if __name__ == "__main__":
    main()