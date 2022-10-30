import sys, datetime, os

if len(sys.argv) != 4:
    print("ERROR: Se esperan tres (3) argumentos para funcionar")
    print("SOLUCIÓN: Introduce los argumentos correctamente")
    print('Ejemplo: clase09_ej1.py <temperatura> <humedad> <True o False>')
else:
    temperatura = sys.argv[1] 
    humedad     = sys.argv[2] 
    lluvia      = sys.argv[3] 

    # Import datetime nos ayuda para obtener las fechas 
    marca_de_tiempo = datetime.datetime.now() # recolecta el instante
    marca_de_tiempo = int(datetime.datetime.timestamp(marca_de_tiempo)) #  lo pasa a numero entero 

    # Se crea la linea a insertar en el archivo
    linea = str(marca_de_tiempo) + ',' + temperatura + ',' + humedad + ',' + lluvia

    # comandos para escribir 
    logs_lluvia = open('clase09_ej2_oct.csv', 'a') #con a crea el archivo si no existe y puede escribir
    logs_lluvia.write(linea+'\n')
    logs_lluvia.close()