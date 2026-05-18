##a = 3
##print(a)
##a = 3.7
##print(a)
##a = False
##print(a)
##a='Esto es una cadena'
##print(a)
##a= b'Esto es una cadena'
##print(a)
##
##print(hex(15))
##print(hex(255))
##print(hex(65535))
##
##print(bin(15))
##print(bin(128))
##print(bin(192))
##
##print(int(0b10000000))
##print(int(0b11000000))

##import webbrowser
##
##for diario in ['www.elpais.com','www.elmundo.es','www.abc.es']:
##    webbrowser.open(diario)

##t=(1,3,5,7)
##print(t)
##print(t[0])
##print(t[3])
##t=(1,3,5,7,('a','b','c'))
##print(t)

import socket

# the public network interface
##HOST = socket.gethostbyname(socket.gethostname())
##HOST = '192.168.1.44'
HOST=  '10.11.69.17'

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))

# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a package
mensaje = s.recvfrom(65565)
datagramaIP1= mensaje[0]

datagramaIP = list(datagramaIP1)
##print(datagramaIP)

LongitudCabeceraIP = (datagramaIP[0] & 0x0F)*4
cabeceraIP= datagramaIP[0:LongitudCabeceraIP]
print(cabeceraIP)
DatosIP = datagramaIP[LongitudCabeceraIP:]
print(DatosIP)
VersionIP= cabeceraIP[0]>>4
print('Version IP =', VersionIP)
print('Longitud cabecera IP=', LongitudCabeceraIP)
ToS= cabeceraIP[1]
print('ToS =', ToS)
LongitudTotal=cabeceraIP[2]*256+cabeceraIP[3]
print('Longitud total =', LongitudTotal)
IdentificadorIP =cabeceraIP[4]*256+cabeceraIP[5]
print('Identificador IP=',hex(IdentificadorIP))

# disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)