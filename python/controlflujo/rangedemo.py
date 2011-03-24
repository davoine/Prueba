#!/usr/bin/env python
# -*- coding: utf-8 -*-
# rangedemo.py: demo de for con range()

'''Recorre los elementos de una lista y devuelve la posición de cada elemento.
'''

print "==> Numerar los días de la semana"
semana = ['lunes','martes','miércoles','jueves','viernes','sábado','domingo']

for pos in range(0,len(semana)):
  print "Día " + str(pos) + ":   " + semana[pos]
  
print

print "==> Muestras de la función range():"
print "range(10):      ", range(10)
print "range(3,10);    ", range(3,10)
print "range(0,10,2):  ", range(0,10,2)
print "range(10,0,-1): ", range(10,0,-1)



