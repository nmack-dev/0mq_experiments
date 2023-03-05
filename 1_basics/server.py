# Hello World Server
# Binds REP socket to port 5555
# Expects 'Hello' from client, replies with 'World'

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:5555')

while True:
    # Block and wait for the client
    message = socket.recv()
    print(f'Recieved request: {message}')

    time.sleep(1)

    # Send reply back
    socket.send_string('World')