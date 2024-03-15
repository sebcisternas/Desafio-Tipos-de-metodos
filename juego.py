from personaje import CrearPersonaje
import random

print("!!Bienvenido temerario jugador, a Gran Fantasía!! ")
nombre = str(input("Ingrese Nombre de su personaje : "))

# crea una instancia de la clase CrearPersonaje para el jugador con el nombre ingresado
p_jugador = CrearPersonaje(nombre)

# muestra el estado inicial del jugador
print(p_jugador.estado)

# crea una instancia de la clase CrearPersonaje para crear el personaje orco
p_orco = CrearPersonaje("Orco")

probabilidad = p_jugador.probabilidad(p_orco)
print("-------------CUIDADO!!! HA APARECIDO UN ORCO-------------\n")
p_jugador.dialogo_batalla(probabilidad)

print("¿Deseas Atacar o Huir?")
opcion=int(input("Ingresar 1 para Atacar o 2 para huir : "))


# bucle principal del juego para ver si queire atacar o no
while opcion == 1:
    
    num_aleatorio= round(random.uniform(0, 1), 2)
    
    
    # verifica si el número aleatorio es menor o igual a la probabilidad de ganar, y dependiendo de este se ve si gana o no la batalla
    if num_aleatorio <= probabilidad:
        print("------------------------------------")
        print("\nLe has ganado al orco, felicidades")
        print(f"{p_jugador.nombre} a ganado 50 puntos de experiencia\n")
        p_jugador.estado = 50
        p_orco.estado = -30
    else:
        print("------------------------------------")
        print("\n\n¡Oh no! ¡El orco te ha ganado!")    
        print(f"{p_jugador.nombre} a perdido 30 puntos de experiencia\n")
        p_jugador.estado = -30
        p_orco.estado = 50
    
    print(f"Estado actual de personajes :")
    print(p_jugador.estado)
    print(p_orco.estado)
    print("------------------------------------")
    probabilidad = p_jugador.probabilidad(p_orco)
    p_jugador.dialogo_batalla(probabilidad)
    print("¿Deseas Atacar o Huir?")
    opcion=int(input("Ingresar 1 para Atacar o 2 para huir : \n"))



