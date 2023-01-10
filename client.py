import socket, select, string, sys

def display() :
	you="\33[33m\33[1m"+" You: "+"\33[0m"
	sys.stdout.write(you)
	sys.stdout.flush()

def main():
    port = 9876
    name=input("\33[34m\33[1m CREATING NEW ID:\n Enter username: \33[0m")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("20.235.76.21", port))
    s.send(name.encode())
    display()

    while 1:
        socket_list = [sys.stdin, s]
        rList, wList, error_list = select.select(socket_list , [], [])
        for sock in rList:
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print ('\33[31m\33[1m \rDISCONNECTED!!\n \33[0m')
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    display()
            else :
                msg=sys.stdin.readline()
                s.send(msg.encode())
                display()

if __name__ == "__main__":
    main()