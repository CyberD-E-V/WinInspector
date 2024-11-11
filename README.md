# WinInspector
<p align="center">
  <p align="center">
    <img src="https://github.com/user-attachments/assets/5ba1c7cb-9b0a-405b-a1ec-c898bbaf4cb6" alt="WinInspector Logo" />
  </p>
</p>

## Descripción
`WinInspector` es una herramienta de consola hecha con `Python` para `Windows`, diseñada para facilitar la inspección de información del sistema. Proporciona detalles importantes sobre la máquina, como:

- 🖥 `Información del sistema operativo`
- 🧠 `Detalles sobre la memoria RAM y almacenamiento`
- 🌐 `Información de la red y redes Wi-Fi guardadas`
- 👤 `Datos sobre el usuario actual`

Aunque no es una herramienta avanzada, `WinInspector` puede ser útil tanto para análisis rápidos como para obtener información útil sobre un dispositivo Windows.

---

## Características
<div style="margin-left: 20px;">
  <ul>
    <li><b>🖥 Información básica del sistema</b>: Datos sobre el sistema operativo, arquitectura y más.</li>
    <li><b>🧠 Memoria</b>: Detalles de la memoria RAM disponible y en uso.</li>
    <li><b>💾 Almacenamiento</b>: Información sobre los dispositivos de almacenamiento y su uso.</li>
    <li><b>🌐 Red</b>: Información sobre las interfaces de red disponibles.</li>
    <li><b>📶 Wi-Fi</b>: Muestra información sobre la red Wi-Fi conectada y redes Wi-Fi guardadas, incluyendo contraseñas (si están disponibles).</li>
    <li><b>🖱 Interfaz de usuario amigable</b>: Menú interactivo con opciones fáciles de navegar.</li>
  </ul>
</div>

---

## Requisitos
Para ejecutar `WinInspector`, necesitas tener `Python 3.x` y las siguientes librerías instaladas:

<div style="margin-left: 20px;">
  <ul>
    <li><b>psutil</b></li>
    <li><b>platform</b></li>
    <li><b>os</b></li>
    <li><b>subprocess</b></li>
    <li><b>re</b></li>
    <li><b>socket</b></li>
    <li><b>pyfiglet</b></li>
    <li><b>colorama</b></li>
  </ul>
</div>

---

## Instalación

Sigue estos pasos para instalar y ejecutar `WinInspector` en tu máquina local:

<details>
  <summary><b>1. Clona este repositorio en tu máquina:</b></summary>
  <pre><code>git clone https://github.com/CyberD-E-V/WinInspector.git
cd WinInspector</code></pre>
</details>

<details>
  <summary><b>2. Crea un entorno virtual (opcional pero recomendado):</b></summary>
  <pre><code>python -m venv env</code></pre>
</details>

<details>
  <summary><b>3. Activa el entorno virtual:</b></summary>
  <pre><code>.\env\Scripts\activate</code></pre>
</details>

<details>
  <summary><b>4. Instala las dependencias:</b></summary>
  <pre><code>pip install -r requirements.txt</code></pre>
</details>

<details>
  <summary><b>5. Ejecuta el script principal:</b></summary>
  <pre><code>python wininspector.py</code></pre>
</details>

---

## Uso

Una vez que hayas seguido los pasos de instalación, el menú interactivo te permitirá acceder a diferentes opciones para inspeccionar la información de tu sistema. Las opciones disponibles son:

<div style="margin-left: 20px;">
  <ul>
    <li>🖥 Información básica del sistema</li>
    <li>👤 Información sobre el usuario actual</li>
    <li>🧠 Información sobre la memoria</li>
    <li>💾 Información sobre el almacenamiento</li>
    <li>🌐 Información sobre la red</li>
    <li>📶 Información de la red Wi-Fi conectada</li>
    <li>🔒 Listar redes Wi-Fi guardadas</li>
    <li>❌ Salir</li>
  </ul>
</div>

Selecciona una opción e ingresa para obtener los detalles relevantes.

---

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un error o tienes alguna sugerencia, abre un **Issue** o un **Pull Request**.

---

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 📝 Nota Importante

> **Este es un proyecto en desarrollo.**  
> Actualmente, **WinInspector** está en sus primeras etapas y es un proyecto pequeño enfocado en el aprendizaje y la práctica del manejo de scripts en Python.  
> Aunque en el futuro planeo agregar nuevas actualizaciones y mejoras, por el momento está destinado principalmente para uso educativo y para quienes deseen aprender sobre la inspección de sistemas en Windows.  
>  
> Este proyecto lo llevo a cabo como un **hobby** y para divertirme, pero también con el objetivo de contribuir de alguna forma a la comunidad.  

---

**Creado por**: *Cyber-Dev*  
*Fecha*: 11/11/2024
