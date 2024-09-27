# Crear el diccionario con información
informacion_personal = {
    "nombre": "Cisne",
    'apellido': 'Macas',
    "edad": 30,
    "ciudad": "Loja",
    "profesion": "Ingeniera"
}

# Obtener valores del diccionario
print('nombre :', informacion_personal['nombre'])
print('apellido :', informacion_personal['apellido'])
print('edad :', informacion_personal['edad'])
print('ciudad :', informacion_personal['ciudad'])  # Corregido de "cuidad" a "ciudad"
print('profesion:', informacion_personal['profesion'])

# Modificar la clave "edad"
informacion_personal['edad'] = 32  # Corregido acceso a clave
print("\nDespués de modificar 'edad':")
print('nombre :', informacion_personal['nombre'])
print('apellido :', informacion_personal['apellido'])
print('edad :', informacion_personal['edad'])
print('ciudad :', informacion_personal['ciudad'])
print('profesion:', informacion_personal['profesion'])

# Agregar un nuevo par clave-valor (modificar "profesion")
informacion_personal['profesion'] = 'Ingeniera en Sistemas'
print('\nDespués de modificar "profesion":', informacion_personal)

# Eliminar la clave "edad"
del informacion_personal['edad']
print('\nDespués de eliminar "edad":', informacion_personal)

# Imprimir todas las claves
claves = informacion_personal.keys()
print('\nClaves del diccionario:', claves)

# Imprimir todos los valores
valores = informacion_personal.values()
print('Valores del diccionario:', valores)

# Recorrer con un for
print('\nRecorrer diccionario con un for:')
for clave, valor in informacion_personal.items():
    print(f'{clave}: {valor}')

