#!/usr/bin/env python
# -*- coding: utf-8 -*-
# params.py: recibe y muestra parámetros

'''Módulo que muestra distintos tipos de formas para pasar parámetros a funciones.
'''

def f1(nombre, genero, premio='ninguno'):
  '''Función con parámetro opcional y valor por defecto.
  
  @param nombre: un nombre
  @param genero: un género musical o literario
  @param premio: el nombre de un premio
  '''
  
  print "  Nombre: " + nombre
  print "  Género: " + str(genero)
  print "  Premio: " + premio
  
def f2(par1, par2="nada", *args, **kwargs):
  '''Función con diversos tipos de parámetros.
  
  Admite todos los tipos de parámetros posibles: obligatorios, opcionales con valor por defecto, lista de parámetros innominados, y lista de parámetros nominados en parejas clave:valor, donde clave es el nombre del parámetro. El orden es el mostrado en la definición de la función.
  @param par1: un parámetro obligatorio
  @param par2: un parámetro opcional con valor por defecto
  @param args: una lista de valores de parámetros
  @param kwargs: una lista de clave:valor pasada como parámetros nominados
  '''
  print "  parámetros recibidos:"
  print "    obligatorio, par1: " + par1
  print "    opcional, par2=nada: " + par2
  print "    tupla de opcionales, args:\n      ",
  print args
  print "    diccionario de parámetros con nombre, kwargs:\n      ",
  print kwargs

def f3(*args):
  '''Función que retorna varios valores en una tupla.
  
  La función recibe varios argumentos y los devuelve todos en una tupla.
  @param args: la lista de argumentos.
  '''
  return args 

if __name__ == '__main__':
  '''Ejecuta funciones que reciben parámetros, con diferentes listas de parámetros, para mostrar la forma en que se los recibe en la función.'''

  print "==> Función f1"
  print "--> f1('Diego el Cigala', 'flamenco', premio='Grammy')"
  f1('Diego el Cigala', 'flamenco', premio='Grammy')
  print "--> f1('Pirulo', 'perruno')"
  f1('Pirulo', 'perruno')
  
  print "==> Función f2"  
  print '--> f2("9")'
  f2("9")
  print '--> f2("9","cuarenta")'
  f2("9","cuarenta")
  print '--> f2("9","cuarenta","a","b")'
  f2("9","cuarenta","a","b")
  print '--> f2("9","cuarenta","a","b",par3="el tres", par4="el cuatro")'
  f2("9","cuarenta","a","b",par3="el tres", par4="el cuatro")
  print '--> f2("9","","a","b",par3="el tres", par5="el cinco")'
  f2("9","","a","b",par3="el tres", par5="el cinco")
  print '--> f2("9","",par7="el siete", par8="el ocho")'
  f2("9","",par7="el siete", par8="el ocho")
  print "--> print f3('uno','dos','tres')"
  print "  ", f3('uno','dos','tres')
  print "--> print type(f3('uno','dos','tres'))"
  print "  ", type(f3('uno','dos','tres'))

