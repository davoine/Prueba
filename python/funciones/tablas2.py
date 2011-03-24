#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tablas2.py: devuelve una lista de valores de la tabla del número que se le pida

def tabla():
  '''Devuelve una lista de números con la tabla del número que se le pida.
  '''
  
  # el ingreso interactivo con raw_input devuelve una cadena
  snro = raw_input('Ingrese un número (0 para terminar):')
  # convierte la cadena a entero
  nro = int(snro)
  
  lstabla = []    # lista de números de la tabla pedida
  
  for i in range(0,11):    # muestra la tabla hasta el 10
    lstabla.append(nro*i)
    
  return lstabla

if __name__ == "__main__":
  print tabla()

