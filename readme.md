# 🚨 DiscoScan - Sistema de Detección de Escaneos de Puertos con Alerta vía Discord

**DiscoScan** es una herramienta de detección de escaneos de puertos en tiempo real diseñada para sistemas **Linux**. Al identificar patrones sospechosos de escaneo, **DiscoScan** envía automáticamente alertas detalladas a un canal de **Discord** a través de un **Webhook**, permitiéndote actuar de forma inmediata.

La detección se realiza utilizando **`Scapy`**, una potente librería de análisis de tráfico, y el script principal **(`monitor.py`)** se ejecuta como un servicio **(`systemd`)** en segundo plano, garantizando una vigilancia constante sin intervención manual.

✅ Ideal para:
- Laboratorios de prácticas de ciberseguridad 🧪
- Proyectos de hacking ético 🛡️
- Centros educativos 👨‍🏫
- Redes domésticas o empresariales 🏠🏢

---

## 🛠️ Paso 1: Crear un Webhook de Discord

Para que el script pueda **enviar alertas**, necesitas crear un **Webhook** en un canal de tu servidor de Discord. Este Webhook es el que recibe los mensajes de alerta.

### 1.1 Accede a tu servidor de Discord
- Abre la app de **Discord** (versión escritorio o web).
- Dirígete a un servidor donde tengas permisos de administrador.
- En cualquier **canal de texto** donde quieras recibir las alertas, haz clic en el **icono del engranaje** (Editar Canal).

<p align="center">
  <img src="https://i.imgur.com/LQodstA.png" alt="Botón de editar canal">
</p>

### 1.2 Crear un Webhook
- Dentro de la configuración del canal, entra en la sección **"Integraciones"**.
- Haz clic en **"Crear Webhooks"** y se **creara uno automaticamente**.

<p align="center">
  <img src="https://i.imgur.com/dwPsay6.png" alt="Personalizar Webhook">
</p>

- Haz clic en **Webhooks** para expandirlo, ponle un **nombre** y selecciona el canal donde se publicarán las alertas **(si realizaste el paso anterior correctamente, el canal ya estará predefinido).** Además, puedes modificar la **imagen del bot** que aparecerá en los mensajes, aunque esto se puede hacer en cualquier momento más adelante.

<p align="center">
  <img src="https://i.imgur.com/I3IY1Vq.png" alt="Botón de editar canal">
</p>
<a name="paso1.3"></a>

### 1.3 Copiar la URL del Webhook

- Una vez creado, haz clic en **"Copiar URL del Webhook"**.
- Guarda esta URL, ya que deberás pegarla en el archivo `monitor.py` dentro de esta línea ([punto 5](#webhook-linea)):

```python
WEBHOOK_URL = "https://discord.com/api/webhooks/xxxxxxxx/xxxxxxxx"
```

- Por ultimo **guardamos los cambios**. 

<p align="center">
  <img src="https://i.imgur.com/muWofW7.png" alt="Botón de editar canal">
</p>

## 📦 2. Pasos previos antes de descargar y ejecutar el script

Antes de poder lanzar el script de detección de escaneos, es necesario asegurarnos de que el entorno tenga instalados los componentes fundamentales. A continuación te explico cómo hacerlo paso a paso:

- ###  2.1 Instalar Python 3 (por si no lo tienes)

```bash
sudo apt update
sudo apt install python3 -y
```
Para comprobar que se ha instalado correctamente ejecuta el siguiente comando: 

```
python3 --version
```

- ### 2.2 Instalar pip para Python 3

```
sudo apt install python3-pip -y
```
Para comprobar que se ha instalado correctamente ejecuta el siguiente comando: 

``` 
pip3 --version
````

## 📥 3. Clonado del Repositorio y Preparación del Entorno

Para obtener el proyecto puedes hacerlo de dos maneras:

- **Opción 1: Clonar el repositorio con Git**

  Si tienes **Git** instalado en tu sistema, puedes clonarlo directamente con el siguiente comando:
  
  ```bash
  git clone https://github.com/Cu3nz/DiscoScan.git
  
    ```
- **Opción 2: Descargar el proyecto en formato ZIP**
    
    También puedes descargar este repositorio en formato **ZIP** desde la parte superior de esta       página. Solo tienes que hacer clic en el botón **"Code"** y luego seleccionar **"Download          ZIP"**. Una vez descargado, simplemente descomprímelo en la carpeta que prefieras.

    Una vez **descargado** o **clonado** el repositorio, entra a la carpeta del proyecto con el siguiente comando:
    
    ```bash
    cd DiscoScan
    
    ```
    A continuación, abre el proyecto en con tu editor de **código favorito**.
    
## 📚 4. Instalación de dependencias necesarias

 Una vez abierto el proyecto en tu editor de código favorito, es el momento de **instalar las      dependencias** que necesita el **script para ejecutarse correctamente**.

 Estas dependencias están listadas en el archivo **`requirements.txt`**.

- ### 4.1 Ejecutar el comando de instalación (Importante ejecutar con **sudo**)

```bash
sudo pip3 install -r requirements.txt

```
> [!WARNING]
> **Posible error en Ubuntu 24.04**

<p align="center">
  <img src="https://i.imgur.com/Nllwf6X.png" alt="Botón de editar canal">
</p>

Este error aparece en versiones recientes de **Ubuntu (23.04 o superior)** debido a una nueva medida de seguridad llamada **[PEP 668](https://peps.python.org/pep-0668/)**. Esta política impide que se puedan instalar paquetes con `pip` directamente en el entorno global del sistema, para evitar romper dependencias críticas de Python en el sistema operativo.


> ✅  **Soluciones segun tu version de Ubuntu**

- Si usas **Ubuntu 22.04 o inferior**:

```
pip3 install -r requirements.txt
``` 

- Si usas **Ubuntu 23.04 o superior**: 

``` 
sudo pip3 install --break-system-packages -r requirements.txt
```

O tambien puedes crear un **entorno virtual** ejecutando los siguientes comandos: 

```
python3 -m venv venv
source venv/bin/activate
sudo pip3 install -r requirements.txt
```

## 5. 🚀 Poner en funcionamiento el sistema de detección

<a name="webhook-linea"></a>

Antes de continuar, **abre el archivo `monitor.py`** y localiza la siguiente línea:

```python
WEBHOOK_URL = "https://discord.com/api/webhooks/xxxxxxxx/xxxxxxxx"
```

Aquí deberás **pegar la URL del Webhook que copiaste anteriormente en el paso** [1.3](#paso1.3). Este enlace es fundamental, ya que es el canal donde se enviarán las alertas generadas por el script.

Una vez que ya tienes **todas las dependencias instaladas** y has **configurado** correctamente el **Webhook** en el archivo **`monitor.py`**, es momento de **ejecutar el script de instalación** que pondrá todo en marcha:

```
sudo python3 instalar_demonio.py
```

Este comando se encarga de **configurar automáticamente el demonio del sistema (systemd) que ejecutará en segundo plano el script monitor.py**. A partir de este momento, el sistema comenzará a monitorear en tiempo real los paquetes TCP entrantes. Si detecta **más de 20 puertos escaneados desde una misma IP**, se enviará una alerta automática al canal de Discord que configuraste.Esto significa que el **sistema** estará **monitoreando continuamente** en **busca de escaneos** de **puertos** y **enviará una alerta** a tu servidor de **Discord** si detecta una **actividad sospechosa**.


## ⚙️ 6. Comandos útiles para gestionar el servicio

Una vez el demonio está instalado, puedes gestionarlo fácilmente con los siguientes comandos:

| Acción                             | Comando                                                             |
|------------------------------------|----------------------------------------------------------------------|
| 🔄 Reiniciar el servicio           | `sudo systemctl restart monitor-comandos`                           |
| ⏹️ Detener el servicio             | `sudo systemctl stop monitor-comandos`                              |
| ▶️ Iniciar el servicio             | `sudo systemctl start monitor-comandos`                             |
| 🧩 Habilitar el servicio al inicio | `sudo systemctl enable monitor-comandos`                            |
| 🚫 Deshabilitar el inicio automático | `sudo systemctl disable monitor-comandos`                        |
| 📋 Ver estado del servicio         | `sudo systemctl status monitor-comandos`                            |
| 📜 Ver logs recientes del servicio | `sudo journalctl -u monitor-comandos -n 30 --no-pager`              |

> [!NOTE]
>  ℹ️ Si haces cambios en el script **`monitor.py`**, asegúrate de reiniciar el servicio con **`restart`** para aplicar los cambios.


## 💬 7. Ejemplo de una alerta enviada a Discord

Cuando el sistema detecta un escaneo de puertos sospechoso, se enviará automáticamente un mensaje al canal de Discord configurado. A continuación puedes ver un ejemplo real de cómo se visualizaría:
> [!TIP]
> **Comando ejecutado**

```
nmap -Pn -p 21,22,23,25,53,80,110,111,135,139,143,161,389,443,445,512,513,514,3306,3389,4444 <IP_MAQUINA_VICTIMA>
```

<p align="center">
  <img src="https://i.imgur.com/lqJ7H1T.png" alt="Ejemplo de alerta enviada a Discord">
</p>

## 🧩 Tecnologías utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<img src="https://img.shields.io/badge/SO-Linux%2FDebian-green?style=for-the-badge&logo=linux" alt="Sistema operativo badge"/>

## 📄 Licencia

Este proyecto ha sido desarrollado con fines **educativos y personales**. Puedes **utilizar**, **modificar** y **compartir** el código siempre y cuando se otorgue el **crédito correspondiente** al autor original.

¿Quieres aportar mejoras, nuevas ideas o funcionalidades?  

**¡Eres bienvenido a contribuir!** Puedes abrir un **issue** o enviar un **pull request** en cualquier momento.


