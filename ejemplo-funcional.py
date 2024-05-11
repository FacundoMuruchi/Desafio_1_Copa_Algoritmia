import random 

# Abre el archivo en modo escritura ('w')
with open('pases_hockey.txt', 'w') as archivo:
    contador = 0
    jugadores = [
        ("Argentina", "11", "Agustina Gorzelany"),
        ("Argentina", "9", "Maria Jose Granatto"),
        ("Argentina", "20", "Sofia Toccalino"),
        ("Argentina", "10", "Agostina Alonso"),
        ("Argentina", "8", "Valentina Raposo"),
        ("Argentina", "5", "Clara Barberi"),
        ("Argentina", "4", "Delfina Thome"),
        ("Argentina", "7", "Sofia Cairo"),
        ("Argentina", "16", "Pilar Campoy"),
        ("Australia", "1", "Alyson Annan"),
        ("Australia", "2", "Katrina Powell"),
        ("Australia", "3", "Stephanie Kershaw"),
        ("Australia", "4", "Jane Claxton"),
        ("Australia", "5", "Claire Colwill"),
        ("Australia", "6", "Rebecca Greiner"),
        ("Australia", "7", "Louise Dobson"),
        ("Australia", "8", "Jodie Schulz"),
        ("Australia", "9", "Mariah Williams")
        ]

    while contador < 5: 
        evento = random.choice(jugadores)
        pais = evento[0]
        numero_jugador = evento[1]
        nombre_jugador = evento[2]
        pase = random.randint(0, 1)
        minuto = random.randint(0, 60)
        
        # Escribe los datos en el archivo
        archivo.write(f'{pais};{numero_jugador};{nombre_jugador};{pase};{minuto}\n')

        contador += 1
