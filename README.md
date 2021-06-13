
# Video Streamer

The project is intended for programmer who are required 
to transfer encrypted video frame across the network for 
any monitoring activity. The project can be implemented on
raspberry pi or any PC.

The project implements base64 encoding mechanism and can be 
implemented alongside multiprocessing python module to recieve 
video frame from multiple devices on network at once.

'basic_client.py' and 'basic_server.py' do not contain any encryption
mechanism or bandwidth control, instead are meant to be referce for improvised
version of themselves namely 'Client.py' and 'Server.py'

Please check out the following link to have insight of indepth 
working mechanism of provided scripts. 



## Installation 

Clone github repository to your local device.

For server/administrative computer :

```bash 
  git clone https://github.com/saksham-ghimire/Video-Streamer.git
  cd Video-Streamer
  python Server.py
```

For client/monitored computer :

```bash 
  git clone https://github.com/saksham-ghimire/Video-Streamer.git
  cd Video-Streamer
  python Client.py
```  