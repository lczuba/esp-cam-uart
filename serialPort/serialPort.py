import serial
import io
from PIL import Image
import time

camera = serial.Serial('COM3', 1500000)
print("Waiting for data...")

Start_cap = True
size = 0
start = 0
data_capture = []

while Start_cap:
    data = camera.readline()
    try:
        data = data.decode()
        if data[0:7] == ("fb_size"):
            size = int(data.strip('fb_size:'))
            print("Start capture", round(size/1024, 2), "kB")
            print("...")
            start = time.time()
            Start_cap = False
    except:
        pass

Stop_cap = True
data = 0

while Stop_cap:
    data = camera.read(size)
    # print(data)
    Stop_cap = False
    end = time.time() - start
    print("Stop capture, time: ", round(end, 4), "s")
    print("Speed: ", round(size*8/1024/end, 2), "kb/s")

imgBinary = bytes(data)
imgStream = io.BytesIO(imgBinary)
img = Image.open(imgStream)
# img.save('test.jpg')
img.show()








