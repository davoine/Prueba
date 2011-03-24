#!/usr/bin/python
# -*- coding: utf_8 -*-
# paramsmod.py: parámetros recibidos por un módulo

'''Muestra un mensaje, nombre del módulo y lista de argumentos recibidos.
Sugerencias de invocación:
  - C{python paramsmod}
  - C{python paramsmod "uno" "dos" "tres cuatro"}
  - C{python paramsmod.py "uno" 2 2.55 True False, None}
'''

import sys

print "==> paramsmod.py, parámetros recibidos por un módulo"
print "Muestra nombre de módulo y lista de argumentos"

# muestra nombre del módulo
print "  Nombre módulo, sys.argv[0]:", sys.argv[0]

# muestra los argumentos pasados
print "Argumentos, sys.argv[1:]:"

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        print "  ", arg, "\t", type(arg)
else:
    print "  no se pasaron argumentos."


