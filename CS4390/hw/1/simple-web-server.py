import socket
import os

def get_file_content(file_path):
    try:
        with open(file_path, 'rb') as file:         # binary allows for platform independence
                                                    # and also avoids encoding interpretation
            content = file.read()                   
        return content
    except FileNotFoundError:
        return b'404 Not Found'

def main():

    # initial server set up
    server_port = 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen()

    print(f'Server listening on port {server_port}...')

    request_processed = False                       # loop break flag

    # waits for connection and request. Processes request
    # and returns file content or 404 error msg
    while not request_processed:
        connection_socket, addr = server_socket.accept()

        request = connection_socket.recv(1024).decode()
        requested_file = request.split()[1][1:]

        response_content = get_file_content(requested_file)

        header = b''
        if b'404 Not Found' in response_content:
            header = b'HTTP/1.1 404 Not Found\r\n\r\n'
        else:
            header = b'HTTP/1.1 200 OK\r\n\r\n'

        response = header + response_content

        connection_socket.send(response)
        connection_socket.close()

        request_processed = True  # flag for exiting loop; comment line for inf loop

if __name__ == "__main__":
    main()

