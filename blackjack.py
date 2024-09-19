import random
import time

class Carta:
    def __init__(self,numero,palo):
        self.numero = numero
        self.palo = palo
        
    def __str__(self):
        return f"{self.numero} de {self.palo}"

def crear_baraja():
    baraja = []
    palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
    for palo in palos:
        for numero in range(1, 11):
            baraja.append(Carta(numero, palo))
    random.shuffle(baraja)
    return baraja

def cartas_iniciales():
    #INICIALIZAMOS CARTAS INICIALES
    jprimera = baraja[0]
    baraja.pop(0)
    jsegunda =  baraja[0]
    baraja.pop(0)
    jcartas = [jprimera, jsegunda]
    cprimera = baraja[0]
    baraja.pop(0)
    ccartas = [cprimera]
    return jcartas, ccartas

def mostrar_cartas(tipo):
    print()
    print("-----------TUS CARTAS--------------")
    for carta in jcartas:
        print(carta)
        time.sleep(0.5)
    print("---------CARTAS CRUPIER------------")
    for carta in ccartas:
        print(carta)
        time.sleep(0.5)
    print("-----------------------------------")
    n = 0
    for carta in jcartas:
        n += carta.numero
    if n > 21:
            print("TE HAS PASADO DE 21, HAS PERDIDO JAJA")
            exit()
    elif tipo == 1:
        j = 0
        for carta in jcartas:
            j += carta.numero
        c = 0
        for carta in ccartas:
            c += carta.numero
        if c > 21:
            print("HAS GANADO")
            print("Total del jugador: ",j)
            print("Total del crupier: ",c)
            exit()
        if j > c:
            print("HAS GANADO")
            print("Total del jugador: ",j)
            print("Total del crupier: ",c)
            exit()
        elif j == c:
            print("NO HAY GANADOR ")
            print("Total del jugador: ",j)
            print("Total del crupier: ",c)
            exit()    
        elif j < c:
            print("HAS PERDIDO JAJA")
            print("Total del jugador: ",j)
            print("Total del crupier: ",c)
            exit()
    else:
        print(" 1->COJER CARTA || 2->NO COJER")
        print
        decision =  int(input("->"))
        print()
        print("----------------------------------")
        print("----------------------------------")
        if decision == 1:
            x = baraja[0]
            baraja.pop(0)
            jcartas.append(x)
            mostrar_cartas(tipo = 0)
        else:
            n = 0
            for carta in ccartas:
                n = 0 + carta.numero
            while n <= 16:
                x = baraja[0]
                baraja.pop(0)
                ccartas.append(x)
                n += x.numero
            mostrar_cartas(tipo=1)
        
baraja = crear_baraja()
jcartas,ccartas = cartas_iniciales()
mostrar_cartas(tipo=0)
