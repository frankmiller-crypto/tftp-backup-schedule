# **TFTP Backup Automation Tool**  

### **Descripción**  
Este script automatiza el respaldo de configuraciones de dispositivos de red (routers y switches Cisco) mediante SSH utilizando la biblioteca `netmiko`. Los backups se guardan localmente en archivos de texto con marca de tiempo y se registran en un archivo de log para seguimiento.  

---

## **Características**  
✅ Respaldar configuraciones ejecutivas (`running-config`) de múltiples dispositivos.  
✅ Organiza los backups en carpetas por fecha (`YYYY-MM-DD`).  
✅ Genera logs detallados con el estado de cada respaldo.  
✅ Soporta autenticación por usuario/contraseña.  

---

## **Requisitos**  

### **1. Software**  
- **Python 3.8+** ([Descargar](https://www.python.org/downloads/))  
- **Bibliotecas necesarias**:  
  ```bash
  pip install netmiko
  ```

### **2. Configuración de dispositivos**  
- Los dispositivos deben tener **SSH habilitado**.  
- El usuario debe tener permisos para ejecutar `show running-config`.  

---

## **Configuración**  

### **1. Editar el archivo `devices`**  
Modifica la lista de dispositivos en el script:  
```python
devices = [
    {
        'name': 'Router',           # Nombre descriptivo
        'device_type': 'cisco_ios',  # Tipo de dispositivo (netmiko)
        'ip': '10.10.10.254',       # IP del dispositivo
        'username': 'cisco',        # Usuario SSH
        'password': 'cisco'         # Contraseña SSH
    },
    # Añade más dispositivos si es necesario
]
```

### **2. Estructura de archivos generada**  
El script crea la siguiente estructura de directorios:  
```
📦 project_folder/
┣ 📂 network_backups/
┃ ┣ 📂 YYYY-MM-DD/          # Carpeta por fecha
┃ ┃ ┗ 📜 hostname-TIMESTAMP.cfg  # Backup del dispositivo
┃ ┗ 📂 logs/
┃   ┗ 📜 backup_log.txt     # Registro de ejecuciones
```

---

## **Ejecución**  

### **1. Desde la terminal**  
```bash
python backup_script.py
```

### **2. Programar en Windows (Tareas Programadas)**  
1. Abre el **Programador de Tareas**.  
2. Crea una nueva tarea:  
   - **Acción:** Iniciar programa → `python.exe`  
   - **Argumentos:** `"ruta\al\script.py"`  
   - **Programar:** Cada 5 minutos (o según necesidad).  

---

## **Posibles errores y soluciones**  

| **Error**                          | **Causa**                          | **Solución** |
|------------------------------------|------------------------------------|--------------|
| `NetmikoTimeoutException`          | El dispositivo no responde.        | Verificar IP/SSH. |
| `Authentication failed`            | Credenciales incorrectas.          | Revisar usuario/contraseña. |
| `No such file or directory`        | Ruta de backups inválida.          | Crear manualmente `network_backups`. |

---

## **Contribuciones**  
Si deseas mejorar el script:  
1. Haz un **fork** del repositorio.  
2. Crea una rama (`git checkout -b feature/nueva-funcion`).  
3. Envía un **Pull Request**.  

---

## **Licencia**  
Este proyecto está bajo la licencia **MIT**.  

---

### **📌 Notas adicionales**  
- **Soporta Cisco IOS**, pero puede adaptarse para otros dispositivos cambiando `device_type` ([Referencia Netmiko](https://github.com/ktbyers/netmiko/blob/develop/PLATFORMS.md)).  
- Para mayor seguridad, considera usar **claves SSH** en lugar de contraseñas.  

--- 

