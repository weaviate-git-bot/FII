import socket
import struct
import ipaddress

# s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
print("ta")
while True:
    # print("Waiting for packet")
    packet = s.recvfrom(65535)
    data = packet[0]
    ip_header = struct.unpack('!B11s4s4s', data[14:34])

    version = ip_header[0]
    if version != 0x45:
        print("Unsuported packet")
        continue
    source = ipaddress.IPv4Address(ip_header[2])
    dest = ipaddress.IPv4Address(ip_header[3])
    
    if len(data) < 66:
        continue
    tcp_header = struct.unpack('!HH28s', data[34:66])
    payload = data[66:]
    if source == dest:
        continue

    if any([x in [22, 5353] for x in [tcp_header[0], tcp_header[1]]]):
        continue
    # if all([x.compressed.startswith("10.10.0.") for x in [source, dest]]):
    #     continue
    print("-="*20)
    print("Packet: ", version, source, dest, tcp_header)
    print("Payload: ", payload)
    print("-="*20)
    # break
