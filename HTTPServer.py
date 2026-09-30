import logging
from scapy.all import sniff
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

class PassiveDnsMonitor():
    def __init__(self, interface=None):
        self.interface = interface
    
    def process_dns_packet(self, packet):
        if packet.haslayer(IP) and packet.haslayer(DNS):
            dns_layer = packet[DNS]
            
            if dns_layer.qr == 0 and packet.haslayer(DNSQR):
                source_ip = packet[IP].src
                query_name = packet[DNSQR].qname.decode('utf-8', errors='ignore')
                
                print("[DNS REQUEST] Client:",source-ip, "queried ->", query_name)
        
    def start_sniffing(self, count=0):
        """Spawns the socket sniffing engine targeting UDP port 53 only."""
        print("Monitoring local DNS traffic on UDP port 53...")
        print("-" * 65)
    
        sniff(iface=self.interface, filter="udp port 53", prn=self.process_dns_packet, store=0, count=count)


if __name__ == '__main__':
    monitor = PassiveDnsMonitor()
    
    monitor.start_sniffing(count=10)
