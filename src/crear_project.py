from pathlib import Path
import sys
import subprocess
import os
from dotenv import load_dotenv 


load_dotenv()

base_path = os.getenv('BASE_PATH')

if not base_path:
    print("No se encontro la direccion deseada")
    sys.exit(1)

base = Path(base_path)

nombre = sys.argv[1]

ruta = base / nombre
ruta.mkdir()
print(f"Proyecto '{nombre}' Creado")

(ruta / "src").mkdir()
(ruta / "tests").mkdir()
(ruta / "src" / f"{nombre}.py").touch()

subprocess.run(["git","init"], cwd=ruta)
subprocess.run(["py","-m","venv","venv"], cwd=ruta)
subprocess.run(["code","."],cwd=ruta)


