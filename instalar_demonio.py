import os
import shutil
import subprocess
from pathlib import Path

usuario = os.getenv("USER")
directorio_destino = Path("/opt/monitor_comandos/")
archivo_fuente = Path("monitor.py").resolve()
ruta_destino = directorio_destino / "monitor.py"
ruta_servicio = "/etc/systemd/system/monitor-comandos.service"

def crear_directorio_destino():
    if not directorio_destino.exists():
        os.makedirs(directorio_destino)
        print(f"📁 Carpeta creada: {directorio_destino}")
    shutil.copy(archivo_fuente, ruta_destino)
    os.chmod(ruta_destino, 0o755)
    print(f"✅ Script copiado como monitor.py en: {ruta_destino}")

def crear_archivo_servicio():
    contenido = f"""[Unit]
Description=Daemon que detecta escaneos y manda alertas a Discord
After=network.target

[Service]
ExecStart=/usr/bin/python3 {ruta_destino}
Restart=always
RestartSec=5
User=root
WorkingDirectory={directorio_destino}
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
"""
    with open(ruta_servicio, "w") as f:
        f.write(contenido)
    print(f"✅ Archivo de servicio creado: {ruta_servicio}")

def habilitar_servicio():
    subprocess.run(["systemctl", "daemon-reload"])
    subprocess.run(["systemctl", "enable", "monitor-comandos"])
    subprocess.run(["systemctl", "start", "monitor-comandos"])
    print("🚀 Servicio activado y ejecutándose.")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("❌ Debes ejecutar este script como root: sudo python3 instalar_demonio.py")
        exit(1)
    crear_directorio_destino()
    crear_archivo_servicio()
    habilitar_servicio()
    print("\n🎉 ¡Todo listo! El demonio se ejecutará automáticamente al arrancar el sistema.")
