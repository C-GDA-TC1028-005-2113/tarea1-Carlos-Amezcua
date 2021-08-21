def main():
    sumaCalifs = 0
    
    sumaCalifs += float(input("Calificación de la materia: "))
    sumaCalifs += float(input("Calificación de la materia: "))
    sumaCalifs += float(input("Calificación de la materia: "))
    sumaCalifs += float(input("Calificación de la materia: "))

    promedio = sumaCalifs / 4

    print(f"El promedio es: {promedio}")

if __name__ == '__main__':
    main()
