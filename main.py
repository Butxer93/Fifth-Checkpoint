# Cree un bucle For de Python.

for i in range(1, 11):
    print(i)

'''
1
2
3
4
5
6
7
8
9
10
'''

# Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(num1, num2, num3):
    return num1 + num2 + num3

print(suma(2,3,4)) # Resultado: 9

# Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

suma2 = lambda x, y, z: x + y + z
print(suma2(2,3,4)) # Resultado: 9

# Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

lista_nombre.index(nombre)

'''
# con for e in:

for nom in lista_nombre:
    if nom == nombre:
        print(f'{nombre} existe en la lista, en la posición {lista_nombre.index(nom)}')
    else:
        print(f'{nombre} no existe en la lista')
'''
