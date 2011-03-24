#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tablas.py: muestra la tabla del número que se le pida

def tabla():
  '''Muestra la tabla del número que se le pida.
  '''
  
  # el ingreso interactivo con raw_input devuelve una cadena
  snro = raw_input('Ingrese un número (0 para terminar):')
  # convierte la cadena a entero
  nro = int(snro)
  
  print "Tabla del " + snro + ":"
  for i in range(0,11):    # muestra la tabla hasta el 10
    print i, "x", snro, "=", i * nro
  return nro

if __name__ == "__main__":
  # si el módulo fue invocado directamente su nombre es __main__
  print "Tablas de multiplicar"
  while tabla() != 0:
    pass
