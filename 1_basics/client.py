import zmq

context = zmq.Context()

# Init socket to talk to server
print('Connecting to hello world server...')
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

# Do 10 requests, waiting for a response (blocking)
for request in range(10):
    print(f'Sending request {request} ...')
    socket.send_string('Hello')

    # Get the reply
    message = socket.recv()
    print(f'Recieved reply {request} [ {message} ]')