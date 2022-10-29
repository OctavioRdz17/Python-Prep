class hexatools:
    def __init__(self, lista_numeros):
        self.lista_numeros = lista_numeros
    
    def ex_primo(self):
        for a in self.lista_numeros:
            es_primo = True
            if a == 1: 
                print ("El numero 1 es primo")
            for n in range(2,a):
                if(a % n == 0):es_primo = False
            if es_primo == True:
                print (f"El numero {a} es primo")
            else:
                print (f"El numero {a} no es primo")

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
        for valor in self.lista_numeros:
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
            print(f"{valor} grados {origen}, en {destino} son {valor_destino}")

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
        for i in self.lista_numeros:
            print (f'El factrorial de {i} es {self.__factorial(i)}')


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