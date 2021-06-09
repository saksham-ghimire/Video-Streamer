import imagiz
import cv2
import multiprocessing
import os
import signal
import base64
import numpy
from io import BytesIO


def start_server(port, sv_op):

    server=imagiz.Server(port=port) # Starting server instance on port 7070

    if sv_op: # if sv_op is True the incoming video frame will be saved as Video.avi
      vid_cod = cv2.VideoWriter_fourcc(*'XVID')
      output = cv2.VideoWriter("Video.avi", vid_cod, 10.0, (640,480))


    while True:
        message=server.receive() # Recieve incoming frame forever with While True loop.
        
        dc_bytes = base64.b64decode(message.image) # Decoding the recieved message using base64 as was encrypted on client side using base64
        df = BytesIO(dc_bytes)
        df = numpy.load(df) # converting bytes into numpy array

        message = cv2.imdecode(df,1)

        # setting resizing parameter as it was compressed to 60% of original size while transmission

        width = int(message.shape[1] / 0.6) 
        height = int(message.shape[0] / 0.6)
        dim = (width, height)
            
        # resizing frame to original size
        resized = cv2.resize(message, dim, interpolation = cv2.INTER_AREA) 


        cv2.imshow("Video",resized) # showing resized frame

        if sv_op:
            output.write(resized) # Writing frame to file if save option is provided true



        if cv2.waitKey(1) & 0xFF == ord('q'): # Close visualization panel if 'q' is pressed
          break
    
    try:
        output.release() 
    except:
        pass 
    
    cv2.destroyAllWindows() # detroy  cv2 window
    current_id = multiprocessing.current_process().pid # getting current server process ID
    os.kill(current_id,signal.SIGTERM) # Making sure the server process is terminated and not running in background

if __name__ == '__main__':
    start_server(7070,True) 