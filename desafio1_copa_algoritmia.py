# Generar un conjunto de datos simulando los eventos de pases entre jugadoras de Argentina y Australia de hockey

# MODULOS
import random 

# PROGRAMA PRINCIPAL
contador = 0
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

while contador < 5: 
    print(f'----------EJEMPLO N{contador}----------')
    jugadora = random.choice(jugadores)
    print('Jugadora:', jugadora)

    pase = random.randint(0, 1)
    print('Pase:', pase)

    minuto = random.randint(0, 60)
    print('Minuto:', minuto)
    contador +=  1
    
# CREAR TXT
# f = open('pases.txt', 'x')