#print('Hola Mundo')
#print('Hola especialmente al Mundo ISTEA')

class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

lista_libros = []

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficcion", 4.5)
libro2 = Libro("1984", "George Orwell", "Ciencia Ficcion", 4.3)
libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasia", 4.7)
libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)
libro5 = Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clasico", 4.4)
libro6 = Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)
libro7 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clasico", 4.6)
libro8 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasia", 4.8)
libro9 = Libro("Los Pilares de la Tierra", "Ken Follett", "Historica", 4.4)
libro10 = Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasia", 4.0)



lista_libros.extend([libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10])


while True:
    print("\n¡Bienvenido a la biblioteca!")
    print("1. Agregar Libro")
    print("2. Buscar Libros por Género")
    print("3. Recomendar Libro")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Agregar Libro
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        puntuacion = float(input("Ingrese la puntuación del libro: "))
        nuevo_libro = Libro(titulo, autor, genero, puntuacion)
        lista_libros.append(nuevo_libro)
        print("¡Libro agregado correctamente!")
    elif opcion == "2":
        # Buscar Libros por Género
        genero_busqueda = input("Ingrese el género que desea buscar: ")
        libros_en_genero = [libro.titulo for libro in lista_libros if libro.genero.lower() == genero_busqueda.lower()]
        if libros_en_genero:
            print("Libros en el género", genero_busqueda + ":")
            for titulo_libro in libros_en_genero:
                print("-", titulo_libro)
        else:
            print("No se encontraron libros en el género", genero_busqueda)
    elif opcion == "3":
        # Recomendar Libro
        genero_interes = input("Ingrese su género de interés: ")
        libros_en_genero = [libro for libro in lista_libros if libro.genero.lower() == genero_interes.lower()]
        if libros_en_genero:
            libro_recomendado = max(libros_en_genero, key=lambda libro: libro.puntuacion)
            print("¡Recomendación para usted!")
            print("Título:", libro_recomendado.titulo)
            print("Autor:", libro_recomendado.autor)
            print("Puntuación:", libro_recomendado.puntuacion)
        else:
            print("No hay libros disponibles en el género", genero_interes)
    elif opcion == "4":
        # Salir
        print("¡Gracias por visitar la biblioteca!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
