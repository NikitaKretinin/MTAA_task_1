import socketserver
import socket
import sys
import time
import logging
import sipfullproxy as sipPy

def start_server(name):
    host = '0.0.0.0'

    print(name + "'s proxy server")

    print("Choose port for the proxy server: ")
    port = int(input())
    if port == 0:
        port = 5060

    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    ipaddress = socket.gethostbyname(hostname)
    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[1]
    logging.info(ipaddress)
    sipPy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, port)
    sipPy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, port)
    server = socketserver.UDPServer((host, port), sipPy.UDPHandler)
    print("Proxy server started at <%s:%s>" % (ipaddress, port))
    server.serve_forever()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_server("Mykyta")


