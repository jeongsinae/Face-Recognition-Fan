# Face-Recognition-Fan
라즈베리파이를 활용한 얼굴인식 선풍기

# 아이디어
초음파센서를 이용하여 사람을 탐지하고 일정 거리에서 사람이 벗어났을때 (자리를 비웠을 때) 연결된 선풍기를 끄도록 하여 에너지를 절약한다. 그리고 다시 초음파 센서의 일정 거리 안으로 사람이 들어오면 해당 사람이 주인인지를 판단하여 선풍기의 작동을 시작한다.

# 구현
딥러닝을 활용하여 사용자의 얼굴(sinae)와 사용자의 얼굴이 아닌 얼굴(other)을 학습시킨 모델을 추출한다. 
<img src="https://user-images.githubusercontent.com/49273782/167986397-64a1a2c3-3c24-4039-8cf8-028499e9a962.png" width="550px" height="200px"></img>   
학습된 모델을 서버를 통해 라즈베리파이로 불러오고 실시간으로 카메라 센서를 이용하여 사진을 찍는다.   
<img src="https://user-images.githubusercontent.com/49273782/167986365-dcab65ef-0235-4564-8e1a-04d659726052.png" width="450px" height="200px"></img>     
찍힌 이미지가 학습시킨 사용자의 얼굴이고 초음파 센서 안으로 무언가 감지되면 (거리 30cm) 라즈베리파이의 usb port의 전원을 켜 선풍기를 동작시킨다.   
##### #turn on all usb ports     
<pre><code>os.system("sudo uhubctl -l 1-1 -a 1")</code></pre>   
   
반면 학습된 사용자의 얼굴이 아니거나 초음파 센서안으로 아무것도 감지되지 않은 경우(거리 30cm이상)에는 라즈베리파이의 usb port의 전원을 꺼 선풍기의 동작을 정지시킨다.    
##### #turn off all usb ports     
<pre><code>os.system("sudo uhubctl -l 1-1 -a 0")</code></pre>  

#### 시연영상    
<https://youtu.be/DeHT28NKqU4>
