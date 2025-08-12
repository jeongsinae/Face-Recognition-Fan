import paramiko
import os
import time

import RPi.GPIO as GPIO 
import picamera

username = 'ddochi'
passwd = 'passward'

src = '/home/pi/Desktop/capture/img.jpg'
dst = '/home/ddochi/Desktop/face/data/result/result/test.jpg'

def put_file(src, dst): 
    transport = paramiko.Transport('114.70.193.160', 22)
    transport.connect(username = username, password = passwd)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(src, dst)
    sftp.close()
    transport.close()

def getResult():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('114.70.193.160', username=username, password=passwd)

    inter = '/home/ddochi/anaconda3/envs/my_env/bin/python3'
    path = '/home/ddochi/Desktop/face/original.py'
    command = inter + ' ' + path

    stdin, stdout, stderr = ssh.exec_command(command)

    lines = stdout.readlines()
    ssh.close()
    
    return lines[0]

camera=picamera.PiCamera()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
trig = 23
echo = 24       
print ("start")

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN) 
GPIO.output(trig, False)      
print("Waiting for sensor to settle") 
time.sleep(2)

i=0
try:
    while True:
        GPIO.output(trig, True)     
        time.sleep(0.00001)       
        GPIO.output(trig, False)
        while GPIO.input(echo) == 0 :
            pulse_start= time.time()    
        while GPIO.input(echo) == 1 : 
            pulse_end= time.time()    
              
        pulse_duration = pulse_end-pulse_start 
        distance = pulse_duration * 34300/2 
        distance = round(distance, 2) 

        print ("Distance : ", distance, "cm") 
        time.sleep(0.1)   
        
        camera.capture('/home/pi/Desktop/capture/img.jpg')
        print('capture')
        
        put_file(src, dst)
        res = getResult()
        print(res)
        if(distance <30 and ('sinae' in res)):
            #turn on all usb ports
            os.system("sudo uhubctl -l 1-1 -a 1")
            time.sleep(3)
            i+=1
        else:
            #turn off all usb ports
            os.system("sudo uhubctl -l 1-1 -a 0")
            continue
 
except KeyboardInterrrupt: 
    print("Measurement stopped by User") 
    GPIO.cleanup()
