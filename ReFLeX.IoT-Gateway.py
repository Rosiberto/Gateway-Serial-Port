import serial.tools.list_ports
import keyboard
import requests
import json

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []


def reflexiot(url=None, resource=None, apikey=None, device_id=None, data=None ):   
    urlhost = 'http://{}{}?k={}&i={}'.format(url, resource, apikey, device_id, data)
    headers = {
                'fiware-service': 'reflexiot',
                'fiware-servicepath': '/',
                'Content-Type': 'application/json'  
            }
    
    datas = data[2:-5]
    d = datas.split(":")  
    d = dict([(k, v) for k,v in zip (d[::2], d[1::2])])
    
    try:
        requests.request("POST", urlhost, headers=headers, data= json.dumps(d) )       
    except:
        print("Error sending the message")

    

for onePort in ports:
    portsList.append( str(onePort) )
    print("\n**********************************************************")
    print("*               ReFLeX.IoT Gateway                       *")
    print("*                                                        *")   
    print("**********************************************************")
    print("\nPort found: ")
    print(str(onePort))

print("\n")
val = input("Select Port: COM")

print("\n=============== ReFLeX.IoT Configuration ================\n")
url = input("Enter URL Host (without 'http://'): ")
valresource = input("Enter Resource: ")
valkey = input("Enter API Key: ")
device_id = input("Enter Device ID: ")
print("\n=========================================================\n")


for x in range(0,len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

print(">>>>> Press 'q' to exit <<<<<")

while keyboard.is_pressed('q') == False:
	
    if serialInst.in_waiting:
        packet = str( serialInst.readline() )
        reflexiot( str(url), str(valresource), str(valkey), str(device_id), packet )
    

serialInst.close() 
print("\nTchau!!") 

