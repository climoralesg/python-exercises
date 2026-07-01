'''
En el taller de Santa hay un elfo becario que está aprendiendo a envolver regalos 🎁.

Le han pedido que envuelva cajas usando solo texto… y lo hace más o menos bien.

Le pasan dos parámetros:

size: el tamaño del regalo cuadrado
symbol: el carácter que el elfo usa para hacer el borde (cuando no se equivoca 😅)
El regalo debe cumplir:

Debe ser un cuadrado de size x size.
El interior siempre está vacío (lleno de espacios), porque el elfo "aún no sabe dibujar el relleno".
Si size < 2, devuelve una cadena vacía: el elfo lo intentó, pero se le perdió el regalo.
El resultado final debe ser un string con saltos de línea \n.
Sí, es un reto fácil… pero no queremos que despidan al becario. ¿Verdad?

'''

def draw_gift(size, symbol):
    default_gift = ''
    initialFinal =''
    result = ''
    lines = []
    if size < 2:
        return default_gift
    for row in range (0,size):
        if row == 0 or row == (size-1):
            lines.append(symbol * size)
            initialFinal = symbol * size + "\n"
            result = result + initialFinal 
        else:
            for col in range(0,size):
                if col == 0 or col == (size - 1):
                    if col == 0:
                        initialFinal = symbol
                        result = result + initialFinal
                    else:
                        initialFinal = symbol + '\n'
                        result = result + initialFinal
                else:
                    result = result + ' '
    return result

print(f"\n{draw_gift(9,'#')}")

if __name__=="__main__":
    draw_gift(3,'#')