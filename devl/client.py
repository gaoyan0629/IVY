import socket

def send_message(connection):
    connection.send("Hello World")

def main():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect(('127.0.0.1', 12345))
    send_message(connection)

if __name__ == '__main__':
    main()
