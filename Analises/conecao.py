import serial
import time
import sqlite3
from models import Temperatura
conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('sensores.db') 
conn.close()
cursor = conn.cursor()

while True: #Loop para a conexão com o Arduino
    try:  #Tenta se conectar, se conseguir, o loop se encerra
        arduino = serial.Serial('/dev/ttyACM0', 9600)
        print('Arduino conectado')
        break
    except:
        pass

while True:
    msg = arduino.readline().decode('utf-8').rstrip()

    #print(msg)
    temperatura_string = (msg[13:18])
    temperatura = int(temperatura_string)
    print("Content-Type: text/html\n\n")
    print(temperatura)
    
    """
    ph_string = (msg[23:28])
    ph = int(ph_string)
    print(ph)
    if temperatura <= 30:
	#cursor.execute("INSERT INTO sensores (temperatura, ph) VALUES ({},{}).format(temperatura,ph)
	
    time.sleep(1)
    """
