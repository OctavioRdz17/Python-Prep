class hexatools:
    def __init__(self, lista_numeros_entrada):
        if(type(lista_numeros_entrada) != list):
            self.lista_numeros = [0]
            raise ValueError('Se ha creado un con elemento 0. Se esperaba una lista de numeros enteros')
        else:
            self.lista_numeros = lista_numeros_entrada

    
    def ex_primo(self):
        lista_primos = []
        for a in self.lista_numeros:
            lip = self.__ex_primo(a)
            lista_primos.append(lip)
            
        return lista_primos

    def __ex_primo(self,a):
        es_primo = True
        if a == 1: return es_primo
        for n in range(2,a):
            if(a % n == 0):es_primo = False
        return es_primo
    
    def valor_modal(self):
        lista_P = self.lista_numeros
        dicc_conteo = {}
        for n in lista_P:
            if (len(dicc_conteo) == 0):
                dicc_conteo[n] = 1
                continue
            if n in dicc_conteo:
                dicc_conteo[n] += 1 
            else:
                dicc_conteo[n] = 1
        moda = None 
        maximo = 0
        for element in dicc_conteo:
            if dicc_conteo[element] > maximo:
                moda = element
                maximo = dicc_conteo[element]
        return moda, maximo

    def __valor_modal(self,lista_P):
        dicc_conteo = {}
        for n in lista_P:
            if (len(dicc_conteo) == 0):
                dicc_conteo[n] = 1
                continue
            if n in dicc_conteo:
                dicc_conteo[n] += 1 
            else:
                dicc_conteo[n] = 1
        moda = None 
        maximo = 0
        for element in dicc_conteo:
            if dicc_conteo[element] > maximo:
                moda = element
                maximo = dicc_conteo[element]
        return moda, maximo
    
    def temperatura(self,origen,destino):
        lista_temp = []
        valor_esperados = ['celsius','kelvin','farenheit']
        for valor in self.lista_numeros:
            if(not(origen in valor_esperados)):
                return print(f"El valor de origen esperado en los parametros debe ser {valor_esperados}")
            if(not(destino in valor_esperados)):
                return print(f"El valor de destino esperado en los parametros debe ser {valor_esperados}")
            
            lista_temp.append(self.__temperatura(valor,origen,destino))
        return lista_temp

    def __temperatura(self,valor,origen,destino):
        valor_destino = 0
        if(origen == "celsius"):
            if destino == "celsius":
                valor_destino = valor
            elif destino == "farenheit":
                valor_destino = (valor *(9/5))+32
            elif destino == "kelvin":
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif(origen == "farenheit"):
            if destino == "farenheit":
                valor_destino = valor
            elif destino == "celsius":
                valor_destino = (valor - 32) * 5 / 9
            elif destino == "kelvin":
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino

    def factorial(self):
        '''
        Devuelve el factorial
        '''
        lis_factorial = []
        for i in self.lista_numeros:
            lis_factorial.append(self.__factorial(i))
        return lis_factorial


    def __factorial(self,numero):
        '''
        Devuelve el factorial
        '''
        if(type(numero) != int):
            return "Debe ser un numero entero"
        if(numero < 0):
            return "Debe ser un numero positivo"
        if (numero > 1):
            numero = numero * self.__factorial(numero - 1)
        return numero