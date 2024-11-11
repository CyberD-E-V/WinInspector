import psutil
import platform
import os
import subprocess
import re
import socket
import pyfiglet
from colorama import init, Fore

# Inicializar colorama
init(autoreset=True)

# Función para imprimir el logo con pyfiglet
def print_logo():
    logo = pyfiglet.figlet_format("WinInspector", font="slant")
    print(Fore.GREEN + logo)
    print(Fore.CYAN + "#" * 60)
    print(Fore.CYAN + "#    By: Cyber-Dev                Date: 11/11/2024         #")
    print(Fore.CYAN + "#" * 60)
    print(Fore.CYAN + "#    ¡Bienvenidos! a WinInspector                          #")
    print(Fore.CYAN + "#    Herramienta para facilitar inspección de informacion  #")
    print(Fore.CYAN + "#    de maquinas Windows!.                                 #")
    print(Fore.CYAN + "#" * 60)

# Función para limpiar la pantalla y mostrar el logo
def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print_logo()

# Función para obtener la dirección IP local
def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        return f"Error al obtener la IP: {e}"

# Información básica del sistema
def print_system_info():
    print(Fore.MAGENTA + "\n--- Información Básica del Sistema ---")
    print(Fore.CYAN + f"Sistema Operativo:"+ Fore.GREEN + f" {platform.system()} {platform.version()}")
    print(Fore.CYAN + f"Plataforma:" + Fore.GREEN + f" {platform.platform()}")
    print(Fore.CYAN + f"Arquitectura:" + Fore.GREEN + f" {platform.architecture()[0]}")
    print(Fore.CYAN + f"Nombre de la máquina:" + Fore.GREEN + f" {platform.node()}")
    print(Fore.CYAN + f"Dirección IP local:" + Fore.GREEN + f" {get_ip_address()}\n")

# Información del usuario actual
def print_user_info():
    print(Fore.MAGENTA + "\n--- Información del Usuario Actual ---")
    print(Fore.CYAN + f"Usuario Actual:" + Fore.GREEN + f" {os.getlogin()}\n")

# Información de la memoria
def print_memory_info():
    memory = psutil.virtual_memory()
    print(Fore.MAGENTA + "\n--- Información de la Memoria ---")
    print(Fore.CYAN + f"Memoria Total:" + Fore.GREEN + f" {memory.total / (1024 ** 3):.2f} GB")
    print(Fore.CYAN + f"Memoria Disponible:" + Fore.GREEN + f" {memory.available / (1024 ** 3):.2f} GB")
    print(Fore.CYAN + f"Uso de Memoria:" + Fore.GREEN + f" {memory.percent}%\n")

# Información del almacenamiento
def print_storage_info():
    print(Fore.MAGENTA + "\n--- Información del Almacenamiento ---")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(Fore.YELLOW + f"\nDispositivo: {partition.device} - Tipo: {partition.fstype}")
        usage = psutil.disk_usage(partition.mountpoint)
        print(Fore.CYAN + f"    Tamaño Total:" + Fore.GREEN + f" {usage.total / (1024 ** 3):.2f} GB")
        print(Fore.CYAN + f"    Espacio Libre:" + Fore.GREEN + f" {usage.free / (1024 ** 3):.2f} GB")
        print(Fore.CYAN + f"    Uso:" + Fore.GREEN + f" {usage.percent}%")
    print("\n")

# Información de la red
def print_network_info():
    print(Fore.MAGENTA + "\n--- Información de la Red ---")
    net_if_addrs = psutil.net_if_addrs()
    for interface, addrs in net_if_addrs.items():
        print(Fore.YELLOW + f"Interfaz: {interface}")
        for addr in addrs:
            print(Fore.CYAN + f"  Dirección IP:" + Fore.GREEN + f" {addr.address}")
    print("\n")

# Información de Wi-Fi conectada
def get_wifi_info():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True, check=True, encoding='cp1252')
        print(Fore.RED + "--- Detalles de la Red Wi-Fi Conectada ---")
        print(Fore.CYAN + result.stdout)

        match = re.search(r"SSID\s*:\s*(.*)", result.stdout)
        if match:
            connected_ssid = match.group(1)
            print(Fore.GREEN + f"\nRed Wi-Fi conectada: {connected_ssid}")
            try:
                result = subprocess.run(['netsh', 'wlan', 'show', 'profile', connected_ssid, 'key=clear'], capture_output=True, text=True, check=True, encoding='cp1252')
                print(Fore.CYAN + f"Detalles de la red {connected_ssid}:")
                print(result.stdout)
                password_search = re.search(r"Contenido de la clave\s*:\s*(.*)", result.stdout)
                if password_search:
                    print(Fore.GREEN + f"Contraseña de la red Wi-Fi: {password_search.group(1)}")
                else:
                    print(Fore.RED + "Contraseña no disponible o no guardada.")
            except subprocess.CalledProcessError as e:
                print(Fore.RED + f"Error al obtener detalles del perfil Wi-Fi '{connected_ssid}': {e}")
        else:
            print(Fore.RED + "No se pudo determinar la red Wi-Fi a la que estás conectado.")
    
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error al ejecutar el comando 'netsh wlan show interfaces': {e}")

# Listar redes Wi-Fi guardadas
def list_saved_wifi():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'profile'], capture_output=True, text=True, check=True, encoding='cp1252')
        wifi_list = re.findall(r"Perfil de todos los usuarios\s*:\s*(.*)", result.stdout)
        if wifi_list:
            print(Fore.GREEN + "\nRedes Wi-Fi guardadas:")
            for idx, wifi in enumerate(wifi_list, 1):
                print(Fore.YELLOW + f"[{idx}]. ({wifi})")
            choice = input(Fore.CYAN + "\nSeleccione el número de la red para ver la contraseña: ")
            try:
                selected_wifi = wifi_list[int(choice) - 1]
                print(Fore.YELLOW + f"\nObteniendo detalles de la red {selected_wifi}...\n")
                get_wifi_password(selected_wifi)
            except (ValueError, IndexError):
                print(Fore.RED + "Selección inválida.")
        else:
            print(Fore.RED + "No se encontraron redes Wi-Fi guardadas.")
    
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error al ejecutar el comando 'netsh wlan show profile': {e}")

# Obtener contraseña de una red Wi-Fi específica
def get_wifi_password(ssid):
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear'], capture_output=True, text=True, check=True, encoding='cp1252')
        password_search = re.search(r"Contenido de la clave\s*:\s*(.*)", result.stdout)
        if password_search:
            print(Fore.CYAN + f"Contraseña de {ssid}:" + Fore.GREEN + f" {password_search.group(1)}")
        else:
            print(Fore.RED + f"No se pudo obtener la contraseña de {ssid}.")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error al obtener la contraseña de {ssid}: {e}")

# Menú principal
def menu():
    while True:
        clear_screen()
        print(Fore.MAGENTA + "--- Menú de Opciones ---")
        print(Fore.CYAN + "[1]. Información Básica del Sistema")
        print(Fore.CYAN + "[2]. Información sobre el Usuario Actual")
        print(Fore.CYAN + "[3]. Información sobre la Memoria")
        print(Fore.CYAN + "[4]. Información sobre el Almacenamiento")
        print(Fore.CYAN + "[5]. Información de la Red")
        print(Fore.CYAN + "[6]. Información sobre la Red Wi-Fi Conectada")
        print(Fore.CYAN + "[7]. Listar Redes Wi-Fi Guardadas")
        print(Fore.CYAN + "[8]. Salir")

        option = input(Fore.CYAN + "Seleccione una opción: ")

        if option == "1":
            print_system_info()
        elif option == "2":
            print_user_info()
        elif option == "3":
            print_memory_info()
        elif option == "4":
            print_storage_info()
        elif option == "5":
            print_network_info()
        elif option == "6":
            get_wifi_info()
        elif option == "7":
            list_saved_wifi()
        elif option == "8":
            print(Fore.GREEN + "Saliendo...")
            break
        else:
            print(Fore.RED + "Opción no válida, intente nuevamente.")
        
        input(Fore.CYAN + "\nPresione Enter para continuar...")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
