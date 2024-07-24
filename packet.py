from scapy.all import sniff, get_if_list
from scapy.layers.inet import IP, TCP, UDP
from datetime import datetime

def packet_callback(packet):
    print("Packet received")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        if TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            proto_name = 'TCP'
        elif UDP in packet:
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            proto_name = 'UDP'
        else:
            sport = None
            dport = None
            proto_name = 'Other'

        print(f"[{timestamp}] {proto_name} Packet: {ip_src}:{sport} -> {ip_dst}:{dport}")

def main():
    print("Starting packet sniffer...")
    iface = "YOUR_NETWORK_INTERFACE"  # Replace with your network interface name
    print(f"Using interface: {iface}")
    sniff(prn=packet_callback, iface=iface, store=0)

if __name__ == "_main_": 
    main()
