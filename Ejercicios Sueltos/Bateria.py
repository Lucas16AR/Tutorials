#import modules

from plyer import notification 
import psutil

#returns a tuple
battery = psutil.sensors_battery()

plugged = battery.power_plugged

#description of code
if __name__=="__main__": 
    if plugged:
        percent = battery.percent
        if percent <= 80:
            notification.notify( 
            #title of notification
            title = "Conectar", 

            #message of notification
            message=" Para mas bateria, cargar a 80%" , 
            
            # displaying time 
            timeout=2 
            )
           
        elif percent == 100: 
            notification.notify( 
            title = "Desconectar", 
            message=" Desconectar cargador. Batería completa" , 
            timeout=2 
            )
           
        else :
            notification.notify( 
            title = "Desconectar", 
            message= "Desconectar cargador. Para mejor calidad de vida de bateria, cargar hasta 80%" , 
            timeout=2 
            )

    else:
        percent = battery.percent
        if percent <=20:
            notification.notify( 
            title = "Recordatorio de batería", 
            message= "Bateria baja. Conectar a tomacorriente " , 
            timeout=2 
            )
       
        elif percent <=50:
            notification.notify( 
            title = "Recordatorio de batería", 
            message=f"Nivel de batería {percent}." ,
            timeout=2 
            )
        
        elif percent == 100:
            notification.notify( 
            title = "Recordatorio de batería", 
            message= "Cargado completamente" , 
            timeout=2 
            )

        else:
            notification.notify( 
            title = "Recordatorio de batería", 
            message= f"Nivel de batería {percent}" , 
            timeout=2 
            )