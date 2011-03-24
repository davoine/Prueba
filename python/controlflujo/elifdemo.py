#!/usr/bin/env python
# -*- coding: utf-8 -*-
# elifdemo.py: demo de if..elif..else

'''Devuelve el nombre del mes recibiendo el número de mes
'''

# importa la biblioteca sys para poder usar sys.exit() y abortar
import sys

# pide número de mes al operador; el dato recibido es siempre una cadena
strmes = raw_input("Número de mes:")

# valida si la cadena es convertible a entero:
try:                    # intenta la conversión
  mes = int(strmes)     # conversión
except:                 # si falla la conversión, surge una "excepción"
  print "Error: debe digitar un número entero."
  sys.exit()            # sale del programa
# si no hubo excepciones sigue el curso normal del programa

# valida que el número esté entre 1 y 12
if mes < 1 or mes > 12:
  print "Error: el número de mes debe estar entre 1 y 12"

if mes == 1:
  print "Enero"
elif mes == 2:
  print "Febrero"
elif mes == 3:
  print "Marzo"
elif mes == 4:
  print "Abril"
elif mes == 5:
  print "Mayo"
elif mes == 6:
  print "Junio"
elif mes == 7:
  print "Julio"
elif mes == 8:
  print "Agosto"
elif mes == 9:
  print "Setiembre"
elif mes == 10:
  print "Octubre"
elif mes == 11:
  print "Noviembre"
elif mes == 12:
  print "Diciembre"
else:
  print "Error: el número de mes debe estar entre 1 y 12"

