#!/usr/bin/env python
import odroid_wiringpi as wpi
import time


class tfmini:

	def __init__(self):
		self.serial = wpi.serialOpen('/dev/ttySAC0', 115200)

	def __del__(self):				
		wpi.serialClose(self.serial)	

	def medir(self):
		cont = 0
		cont2 = 0
		cont3 = 0
		distancia = -1
		strenght = -1
		bit3 = 0
		bit4 = 0
		bit5 = 0
		bit6 = 0
		wpi.serialFlush(self.serial)
		while cont < 9:
			output = wpi.serialGetchar(self.serial)
			cont += 1
			if cont == 3 or cont == 4:
				#print(output)
				cont2 += 1

				#Leitura de bits ( 3 e 4 distance, 5 e 6 strenght )
				if cont == 3:
					bit3 = output
				if cont == 4:
					bit4 = output

				# Calcular distance
				if cont2 == 2:
					cont2 = 0
					distancia = bit3 + ( bit4 * 256 )

			if cont == 5 or cont == 6:
				#print(output)
				cont2 += 1

				#Leitura de bits ( 5 e 6 strenght )
				if cont == 5:
					bit5 = output
				if cont == 6:
					bit6 = output
				# Calcular distance e strenght
				if cont2 == 2:
					cont2 = 0
					strenght = bit5 + ( bit6 * 256 )

		#print('Distance = ' + str(distancia) + ' || Strenght = ' + str(strenght))
		return [distancia, strenght]				

if __name__ == '__main__':
	tfmini = tfmini()
	medidas = tfmini.medir()
	print('Distance = ' + str(medidas[0]) + ' || Strenght = ' + str(medidas[1]))
	#print(medidas)
