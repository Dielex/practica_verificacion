# coding=utf-8
from pymongo import MongoClient

#class Controller:
   # def get_mcds(self):
       # print "hola"
        #Accede a base de datos y recupera la información

class MCD:
    URL_MONGO = 'mongodb://localhost:27017/'
    DATABASE_NAME = 'verificacion'

    def __init__(self):
        self.client = MongoClient(self.URL_MONGO)
        self.db = self.client[self.DATABASE_NAME]
        self.mcd = None

    def calcular_mcd(self, a, b):
        resto = 0
        while(b > 0):
            resto = b
            b = a % b
            a = resto

        self.mcd = a
        return self.mcd


    def save(self):
        self.db.mcds.save({"mcd":self.mcd})

    def get_mcds(self):
        cursor = self.db.mcds.find()
        for documents in cursor:
            print(documents)

print 'Introduce el primer numero: '
num1 = input()
print 'Introduce el segundo numero: '
num2 = input()

print 'El máximo común divisor de  num1  y num2 es: '
resultado = MCD()
print resultado.calcular_mcd(num1, num2)
resultado.save()
resultado.get_mcds()





