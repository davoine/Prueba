#!/usr/bin/env python
# -*- coding: utf-8 -*-
# continuedemo.py: demo de continue

'''Muestra el uso de for...else y while...else. Muestra también un uso sencillo de break, continue y pass. Notar uso de , en print, y \n para cambio de línea.
'''

print "Demo simple de control de flujo\n"
print "==> for...else"
for i in range(0,10):
  print i,
else:
  print "\nfor...else: fin\n"

print "==> while...else"
i = 0
while i < 10:
  print i,
  i = i + 1
else:
  print "\nwhile..else: fin\n"

print "==> for...else con continue y pass, muestra sólo pares"
for i in range(0,10):
  if i % 2 != 0:
    continue
  else:
    pass
  print i,
else:
  print "\nfor...else, sólo pares: fin\n"

print "==> for...else con break: fin de repetición al hallar un cierto valor"
valor = 7
for i in range(0,10):
  if i == valor:
    print "\ncorte en valor buscado: ", valor
    break
  else:
    print i,
    
