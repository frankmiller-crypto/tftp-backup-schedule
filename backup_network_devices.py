from netmiko import ConnectHandler
import os
from datetime import datetime

# Dispositivos a respaldar
devices = [
    {
        'name': 'Router',
        'device_type': 'cisco_ios',
        'ip': '10.10.10.254',
        'username': 'cisco',
        'password': 'cisco'
    },
    {
        'name': 'Switch',
        'device_type': 'cisco_ios',
        'ip': '10.10.10.253',
        'username': 'cisco',
        'password': 'cisco'
    }
]

def obtener_hostname(connection):
    try:
        output = connection.send_command("show run | include hostname")
        hostname = output.split()[-1] if output else 'unknown'
        return hostname
    except:
        return 'unknown'

def realizar_backup(device):
    try:
        print(f"\nConectando a {device['name']} ({device['ip']})...")
        
        connection_params = {
            'device_type': device['device_type'],
            'ip': device['ip'],
            'username': device['username'],
            'password': device['password']
        }
        
        connection = ConnectHandler(**connection_params)
        
        # Obtener configuración
        output = connection.send_command("show running-config")
        hostname = obtener_hostname(connection)
        
        # Crear carpeta de backups con fecha
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        backup_folder = os.path.join(os.getcwd(), 'network_backups', fecha_actual)
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
        
        # Nombre de archivo con timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(backup_folder, f"{hostname}-{timestamp}.cfg")
        
        # Guardar backup
        with open(filename, "w") as file:
            file.write(output)
        
        print(f"Backup exitoso guardado en: {filename}")
        connection.disconnect()
        return True
    
    except Exception as e:
        print(f"ERROR al respaldar {device['name']}: {str(e)}")
        return False

def main():
    print("Iniciando proceso de respaldo...")
    print(f"Hora de inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Registrar inicio en log
    log_folder = os.path.join(os.getcwd(), 'network_backups', 'logs')
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    
    log_file = os.path.join(log_folder, 'backup_log.txt')
    
    with open(log_file, 'a') as log:
        log.write(f"\nInicio de respaldo: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        for device in devices:
            success = realizar_backup(device)
            status = "EXITO" if success else "FALLO"
            log.write(f"{device['name']} ({device['ip']}): {status}\n")
        
        log.write(f"Fin de respaldo: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print("Proceso de respaldo completado.")

if __name__ == "__main__":
    main()