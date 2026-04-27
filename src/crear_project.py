from pathlib import Path
import sys

nombre = sys.argv[1]

ruta = Path.nombre

ruta.mkdir()
print(f"Proyecto '{nombre}' Creado")

#(ruta/"src").mkdir()
#(ruta/"tests").mkdir()
