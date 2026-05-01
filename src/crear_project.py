from pathlib import Path
import sys
import subprocess
import os
from dotenv import load_dotenv 


load_dotenv()

base_path = os.getenv('BASE_PATH')

if not base_path:
    print("Path doesn't exist")
    sys.exit(1)

base = Path(base_path)

if len(sys.argv) < 2:
    print("Need project name")
    sys.exit(1)

nombre = sys.argv[1]

ruta = base / nombre
ruta.mkdir(exist_ok=True)
print(f"Proyecto '{nombre}' Creado")

(ruta / "src").mkdir()
(ruta / "tests").mkdir()
(ruta / "src" / f"{nombre}.py").touch()

subprocess.run(["git","init"], cwd=ruta)
subprocess.run(["py","-m","venv","venv"], cwd=ruta)
subprocess.run(["code","."],cwd=ruta)

