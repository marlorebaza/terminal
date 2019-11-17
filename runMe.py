import sys, time

'''
    Nota Importante sobre Flush:
    - flush: escribe el contenido del búfer en el destino y deja el búfer vacío para almacenar más datos, 
    pero no cierra la secuencia de forma permanente. Eso significa que aún puede escribir más datos en la secuencia.
    - Enviando "flush = True" en print (x defecto es False), se logra lo comentado arriba.
    De esta forma logramos que la data enviada a print se vaya almacenando en el destino cada vez que se ejecuta este 
    método, ya que si lo dejamos como False la data se almacenará cuando el proceso se finalice. Y si el proceso
    es matado (kill -9) la data no será almacenada. 
'''

if __name__ == '__main__': 
    #multiple = int(input('Número:')) 
    multiple = int(sys.argv[1]) # Permite obtener el segundo argumento. El primero es el nombre del comando en sí
    number = 0;
    while True:
        number += 1
        if number % multiple == 0:
            print('\'%s\' Sí es múltiplo de %s!' % (number, multiple), file = sys.stdout, flush = True)
        else:
            print('\'%s\' No es múltiplo de %s!' % (number, multiple), file = sys.stderr, flush = True)
        time.sleep(1)