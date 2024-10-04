# Escritura de archivo de texto

with open('my_notes.txt', 'w') as file:

    # Notas personales
    file.write('Nota 1: Recuerda comprar leche. Es esencial para el desayuno y hay que asegurarse de tener suficiente en la nevera.\n')
    file.write('Nota 2: Estudiar para el examen de matemáticas. Dedica tiempo cada día para repasar conceptos y practicar ejercicios, '
               'especialmente problemas de álgebra y geometría.\n')
    file.write('Nota 3: Llamar a mamá. Pregunta cómo ha estado y si necesita algo, es importante mantener el contacto con la familia.\n')

# Lectura de archivo de texto

with open('my_notes.txt', 'r') as file:
    # Leer el contenido del archivo línea por línea
    for line in file:
        # Mostramos cada línea leida
        # strip() elimina los espacios en blanco y saltos de línea al principio y al final
        print(line.strip())


