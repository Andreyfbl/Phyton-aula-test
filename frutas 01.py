# Listas de frutas
frutas = ['pêra', 'uva', 'limão', 'kiwi']
frutas[1] = 'abacate'
print(frutas)

frutas.insert(2, 'uva')
print(frutas)
frutas.insert(4, 'cebola') # não é fruta
print(frutas)
del frutas[4]
print(frutas)
frutas.insert(4, 'Melancia')
print(frutas)
print(f'0 que é o frutas.index {frutas.index("Melancia")}')
del frutas[frutas.index('Melancia')]
print(frutas)
frutas.remove("kiwi")
print(frutas)
frutas.insert(10, 'Ameixa')
print(frutas)
frutas.pop(frutas.index('Ameixa'))
print(f'pop Fruta - {Pop_frutas}')
print(frutas)