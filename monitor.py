from scapy.all import sniff, IP, TCP
import time
import requests
from collections import defaultdict

WEBHOOK_URL = "https://discord.com/api/webhooks/xxxxxxxx/xxxxxxxx" # Reemplaza con tu URL de webhook de Discord

conexiones = defaultdict(list)
TIEMPO_LIMPIEZA = 60
ULTIMA_LIMPIEZA = time.time()
UMBRAL_PUERTOS = 20

def enviar_alerta(ip, puertos):
    mensaje = f"""
🚨 **Alerta: Escaneo de Puertos Detectado** 🚨

**IP del atacante:** `{ip}`
**Puertos escaneados:** `{sorted(set(puertos))}`
**Hora:** {time.strftime('%Y-%m-%d %H:%M:%S')}
"""
    try:
        requests.post(WEBHOOK_URL, json={"content": mensaje})
        print(f"✅ Alerta enviada para IP {ip}")
    except Exception as e:
        print(f"❌ Error al enviar alerta: {e}")

def detectar_paquete(pkt):
    global ULTIMA_LIMPIEZA

    if IP in pkt and TCP in pkt:
        ip_origen = pkt[IP].src
        puerto_destino = pkt[TCP].dport

        conexiones[ip_origen].append(puerto_destino)

        if len(set(conexiones[ip_origen])) > UMBRAL_PUERTOS:
            enviar_alerta(ip_origen, conexiones[ip_origen])
            conexiones[ip_origen] = []

    if time.time() - ULTIMA_LIMPIEZA > TIEMPO_LIMPIEZA:
        conexiones.clear()
        ULTIMA_LIMPIEZA = time.time()

if __name__ == "__main__":
    print("🔍 Monitoreando tráfico en busca de escaneos...")
    sniff(filter="tcp", prn=detectar_paquete, store=0)
