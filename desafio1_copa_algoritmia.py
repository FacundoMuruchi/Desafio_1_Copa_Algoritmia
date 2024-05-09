#Generar un conjunto de datos simulando los eventos de pases entre jugadoras de Argentina y Australia de hockey

contador = 0
import random 

jugadores = [
    ("Argentina", "Agustina Gorzelany", 11),
    ("Argentina", "Maria Jose Granatto", 9),
    ("Argentina", "Sofia Toccalino", 20),
    ("Argentina", "Agostina Alonso", 10),
    ("Argentina", "Valentina Raposo", 8),
    ("Argentina", "Clara Barberi", 5),
    ("Argentina", "Delfina Thome", 4),
    ("Argentina", "Sofia Cairo", 7),
    ("Argentina", "Pilar Campoy", 16),
    ("Australia", "Alyson Annan", 1),
    ("Australia", "Katrina Powell", 2),
    ("Australia", "Stephanie Kershaw", 3),
    ("Australia", "Jane Claxton", 4),
    ("Australia", "Claire Colwill", 5),
    ("Australia", "Rebecca Greiner", 6),
    ("Australia", "Louise Dobson", 7),
    ("Australia", "Jodie Schulz", 8),
    ("Australia", "Mariah Williams", 9)
    ]

while contador != 10: 
    print(f'----------EJEMPLO N{contador}----------')
    alguna = random.choice(jugadores)
    print('jugadora', alguna)

    xd = random.randint(0, 1)
    print('pase si o no:', xd)

    minuto = random.randint(0, 60)
    print('minuto:', minuto)
    contador +=  1
    
# CREAR TXT

#f = open('pases.txt', 'x')