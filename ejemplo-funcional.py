import random 

# Abre el archivo en modo escritura ('w')
with open('pases_hockey.txt', 'w') as archivo:
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
        evento = random.choice(jugadores)
        pais = evento[0]
        numero_jugador = evento[2]
        nombre_jugador = evento[1]
        pase = random.randint(0, 1)
        minuto = random.randint(0, 60)
        
        # Escribe los datos en el archivo
        archivo.write(f'{pais};{numero_jugador};{nombre_jugador};{pase};{minuto}\n')

        contador += 1
