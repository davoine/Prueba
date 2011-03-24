#!/usr/bin/env python
# -*- coding: utf-8 -*-
# continuedemo.py: demo de continue

'''Cuenta la cantidad de letras 'p' o 'P' en un texto.
'''

pals1 = "Pedro Picapiedra padre picado pePino malpaso paPa paleta tapado"
cant = 0

for lt in pals1:
  if lt != 'p' and lt != 'P':
    continue
  # aquí sigue usualmente un proceso largo, que se saltea con el continue
  # cuando se da la condición del if
  cant += 1

print "Hay " + str(cant) + " letras 'p' o 'P' en el texto:"
print "   '" + pals1 + "'"

  
  

