# Generar un conjunto de datos simulando los eventos de pases entre jugadoras de Argentina y Australia de hockey

# MODULOS
import random 

# PROGRAMA PRINCIPAL
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
    
#Dentro de la variable "Jugadores" colocamos el nombre de todas las jugadoras junto al pais que representan y su numero

    
while contador < 5: 
    print(f'----------EJEMPLO N{contador}----------')
    jugadora = random.choice(jugadores)
    print('Jugadora:', jugadora)

    pase = random.randint(0, 1)
    pase = str(pase)
    print('Pase:', pase)

    minuto = random.randint(0, 60)
    minuto = str(minuto)
    print('Minuto:', minuto)

    file = open('Pases.txt', 'w')
    file.write(jugadora)
    file.write(pase)
    file.write(minuto)
    contador +=  1

#Dentro del while, el contador va a controlar que las iteraciones no sean mayores a las pedidas y luego de cada valor entero se declara la variable como string
#ya que los archivos de texto no admiten valores enteros.
    

