import bluetooth, json, time
from multiprocessing import Process
import restful_service

api_service = restful_service.ApiService("device1", "8fe63a92-b916-11e6-80f5-76304dec7eb7")

def server_function(client_sock, address):
    try:
        print ("Accepted connection from ", address)
        data = client_sock.recv(1024).decode("utf-8")
        print ("received [%s]" % data)
        data = json.loads(data);
        data["attendAt"] = int(time.time() * 1000)
        attend_info = data
        print ("json data [%s]" % attend_info)
        response = api_service.send_attendance_request(attend_info)
        print (response.text)
        client_sock.send(response.text)
    except KeyboardInterrupt:
        if client_sock is not None:
            client_sock.close()
        if address is not None:
            server_sock.close()

    if client_sock is not None:
        client_sock.close()
    if address is not None:
        server_sock.close()


server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 0
server_sock.bind(("", port))
server_sock.listen(1)

print ("listening on port %d" % port)

uuid = "00001101-0000-1000-8000-00805F9B34FB"
bluetooth.advertise_service(server_sock, "foobar service", uuid)

socket, addr = None, None
while True:
    try:
        socket, addr = server_sock.accept()
        p = Process(target=server_function, args=(socket, addr))
        p.start()
        p.join()
    except KeyboardInterrupt:
        if socket is not None:
            socket.close()
        if addr is not None:
            server_sock.close()