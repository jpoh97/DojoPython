class dojo: #clase

	def __init__(self, x, y, s): #constructor
		self.menor = x #self = this
		self.mayor = y
		self.salto = s
		self.rango = range(menor, mayor, salto)

	def sum(self): #funcion
		suma = 0
		for i in self.rango:
			suma = suma + i
		print(suma)
		return suma

print("ingrese menor");
menor = int(input());

print("ingrese mayor");
mayor = int(input());

print("ingrese un salto");
salto = int(input());

calcular = dojo(menor, mayor, salto)

calcular.sum()

#rango = range(menor, mayor)