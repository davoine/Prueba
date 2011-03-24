#!/usr/bin/env python
# -*- coding: utf-8 -*-
# whiledemo.py: demo de while

'''Copia caracteres desde una cadena a otra hasta hallar un caracter \
determinado.
'''
    
copiaDesde = "Copiar de esta cadena hasta hallar 'l'"
copiaHacia = ""   # una cadena vacía, o el "string nulo"
    
i = 0;
c = copiaDesde[i] # el caracter en posición i

while c != 'l':
  # mientras el carácter no sea una letra 'l'
  # toma un caracter de copiaDesde y lo agrega en copiaHacia
  copiaHacia += c
  i += 1
  c = copiaDesde[i]   # siguiente caracter

print "Desde:", copiaDesde
print "Hacia:", copiaHacia
