import imagiz
import cv2
import multiprocessing
import os
import signal


def start_server():

    server=imagiz.Server(port=7070) # Starting server instance on port 7070
    while True:
        message=server.receive() # Recieve incoming frame forever with While True loop.
        frame=cv2.imdecode(message.image,1) # Decoding Bytes of Image
        cv2.imshow("Video",frame) # Showing decoded frame
        if cv2.waitKey(1) & 0xFF == ord('q'): # Close visualization panel if 'q' is pressed
          break
    
    cv2.destroyAllWindows() 
    current_id = multiprocessing.current_process().pid # getting current server process ID
    
    os.kill(current_id,signal.SIGTERM) # Making sure the server process is terminated and not running in background

if __name__ == '__main__':
    start_server()
