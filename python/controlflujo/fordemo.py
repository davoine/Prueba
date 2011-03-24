#!/usr/bin/env python
# -*- coding: utf-8 -*-
# fordemo.py: demo de for

'''Define una lista de elementos de diferentes tipos.
Recorre la lista mostrando valor y tipo de cada elemento.
Muestra el largo de la lista.
'''

ls = [ 'martes', "dos palabras", True, False, 32, 87.98, 3/2**3, 12., 12l, \
  2000, 8, 622, 127 ]
print "==> Lista:", ls
print "Valor y tipo:"

for nr in ls:
  print " ", nr, " :  ", type(nr)

print "  Largo de la lista:", len(ls)


