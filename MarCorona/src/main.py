from scapy.all import *

DATA_IP : str = '10.0.0.12'
TARGET : bytes = b"Marco, I'm sending you a postcard with a good message for life!"
BYTES_PER_CHUNK : int = 100

def filter(packet) -> bool:
    return (
        packet and
        IP in packet and
        TCP in packet and
        DATA_IP == packet[IP].src
    )

def main() -> None:
    packets = sniff(offline="./MarCorona.pcap", lfilter=filter)
    data = b''
    for packet in packets:
        if Raw in packet:
            data += packet[Raw].load[:BYTES_PER_CHUNK]
    
    data = data[data.find(TARGET)+len(TARGET):]
    
    print(data)
    
    with open("./result.jpg", "wb") as result_image:
        result_image.write(data)        

if __name__ == '__main__':
    main()