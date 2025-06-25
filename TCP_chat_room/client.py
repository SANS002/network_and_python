import socket
import threading

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred. Disconnecting...")
            client.close()
            break

def write():
    while True:
        try:
            msg = input('')
            if msg.strip() != "":
                message = f"{nickname}: {msg}"
                client.send(message.encode('ascii'))
        except:
            print("An error occurred while sending.")
            client.close()
            break

#accessing the functions in a separate thread

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
