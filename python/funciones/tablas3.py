#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tablas3.py: muestra la tabla del número que se le pida, trata errores

def tabla():
  '''Muestra la tabla del número que se le pida.
  
  @return: el número pedido.
  @rtype: str
  '''
  
  # el ingreso interactivo con raw_input devuelve una cadena
  snro = raw_input('Ingrese un número (0 para terminar):')
  # convierte la cadena a entero
  
  # captura y trata el error si el usuario no digita un número
  try:
    nro = int(snro)
  except ValueError:
    print "Error: " + snro + " no es un número."
    snro = raw_input('Ingrese un número (0 para terminar):')
    nro = int(snro)
  
  print "Tabla del " + snro + ":"
  for i in range(0,11):    # muestra la tabla hasta el 10
    print i, "x", snro, "=", i * nro
  return nro

if __name__ == "__main__":
  print "Tablas de multiplicar"
  while tabla() != 0:
    pass
