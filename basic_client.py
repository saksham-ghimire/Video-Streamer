import imagiz
import cv2


client=imagiz.Client("cc1",server_ip="localhost", server_port=7070) # Connect to server ip on 7070 port
vid=cv2.VideoCapture(0) # capturing webcam frames
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    r,frame=vid.read() # reading captured frame continously for tranmission
    if r:
        r, image = cv2.imencode('.jpg', frame, encode_param) # Encoding captured framed in bytes
        client.send(image) # Sending captured frame over to server side
    else:
        break