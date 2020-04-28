import os




def sentip():
    print('\033[92m')
    print("  _____            _        _____")
    print(" / ____|          | |      |_   _|")
    print("| (___   ___ _ __ | |_ ______| |  _ __")
    print(" \___ \ / _ \ '_ \| __|______| | | '_ \ ")
    print(" ____) |  __/ | | | |_      _| |_| |_) |")
    print("|_____/ \___|_| |_|\__|    |_____| .__/")
    print("   Created By Alejo Desh         | |")
    print("   Youtube: Alejo Desh           |_|")
    print("   GitHub: https://github.com/4leju/Sent-Ip")
    print()
    print()
    print(" Comandos/ help, scanport, borrar, exit")
    print('\033[0m')
    print()
sentip()
continuar = True
while (continuar):
    cliente = input("\033[7m"+"SentIp:"+"\033[0m"+" ")
    if cliente =="help":
        print("""
     D E S H E R S
        
Listado de dispositivos

devices

Conectar con dispositivo

connect [IP]:[PUERTO] (por defecto el 5555)

Desconectar el dispositivo

disconnect [IP]:[PUERTO]

Copiar un archivo al dispositivo

push [RUTA-LOCAL] [RUTA-DISPOSITIVO]

Reiniciar dispositivo

reboot

Reiniciar dispositivo (arranque)

reboot-bootloader

Instalar APK

install [APK]

Reinstalar APK

-r install [APK]

Desinstalar APK

uninstall [NOMBRE-PAQUETE-APLICACION]

Obtener shell del dispositivo

shell

Iniciar una Activity

shell am start -n [PAQUETE-APLICACION]/.[ACTIVITY]


shell am start -n [PAQUETE-APLICACION]/[ACTIVITY]

Tomar captura de pantalla

shell screencap [RUTA-DISPOSITIVO]


Grabar pantalla del dispositivo

shell screenrecord -time-limit [SEGUNDOS] [RUTA-DISPOSITIVO]

Emular botón encendido

shell input keyevent 26


Emular pantalla de desbloqueo

shell input keyevent 82

Listar paquetes instalados

shell pm list packages

Logcat

logcat

Filtrar por nivel de prioridad

logcat "*:W"

Filtrar por TAG y prioridad

logcat -s Mi_TAG:W

Buscar contenido en el buffer

logcat -b ejemplo

Borrar el buffer

logcat -c

Filtrar con grep

logcat | grep "com.deshers"

Volcar datos del sistema en la pantalla

shell dumpsys

Volcar datos del sistema a un archivo

shell dumpstate -o /sdcard/dump.txt

Volcar datos de un servicio específico

shell dumpsys battery

Mostrar información sobre CPU

shell cat/proc/cpuinfo

Extraer APK

shell pm path [NOMBRE-PAQUETE]

pull /data/app/[NOMBRE-PAQUETE]/base.apk

shell pm path com.deshers.miaplicacion

pull /data/app/com.deshers.miaplicacion/base.apk

Habilitar datos móviles

shell svc data enable

Deshabilitar datos móviles

shell svc data disable

                """)
    elif cliente =="borrar":
        os.system("clear")
        sentip()
    elif cliente =="exit":
        continuar = False
    elif cliente =="scanport":
        scanport = input("Target Ip: ")
        os.system("nmap -Pn "+scanport)
    else:
        os.system("adb "+cliente)

