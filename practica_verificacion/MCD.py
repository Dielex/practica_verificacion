# coding=utf-8
def mcd(a, b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a

print 'Introduce el primer numero: '
num1 = input()
print 'Introduce el segundo numero: '
num2 = input()

print 'El máximo común divisor de  num1  y num2 es: '
resultado = mcd(num1, num2)
print resultado
