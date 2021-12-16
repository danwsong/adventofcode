hex_input = open('input.txt').read()

bits = len(hex_input) * 4
transmission = bin(int(hex_input, 16))[2:]

while len(transmission) < bits:
    transmission = '0' + transmission

class Packet:
    def __init__(self):
        self.version = 0
        self.type_id = 0
        self.literal = 0
        self.subpackets = []
    
    def parse(self, transmission):
        original_length = len(transmission)
        self.version = int(transmission[:3], 2)
        transmission = transmission[3:]
        self.type_id = int(transmission[:3], 2)
        transmission = transmission[3:]
        if self.type_id == 4:
            # literal
            self.literal = 0
            last_group = 1
            while last_group != 0:
                last_group = int(transmission[:1], 2)
                transmission = transmission[1:]
                self.literal <<= 4
                self.literal |= int(transmission[:4], 2)
                transmission = transmission[4:]
        else:
            # operator
            length_type_id = int(transmission[:1], 2)
            transmission = transmission[1:]
            if length_type_id == 0:
                total_length = int(transmission[:15], 2)
                transmission = transmission[15:]
                subpackets_length = 0
                while subpackets_length < total_length:
                    subpacket = Packet()
                    subpacket_length = subpacket.parse(transmission)
                    transmission = transmission[subpacket_length:]
                    subpackets_length += subpacket_length
                    self.subpackets.append(subpacket)
            else:
                num_subpackets = int(transmission[:11], 2)
                transmission = transmission[11:]
                for _ in range(num_subpackets):
                    subpacket = Packet()
                    subpacket_length = subpacket.parse(transmission)
                    transmission = transmission[subpacket_length:]
                    self.subpackets.append(subpacket)
        return original_length - len(transmission)
    
    def version_sum(self):
        version_sum = self.version
        for subpacket in self.subpackets:
            version_sum += subpacket.version_sum()
        return version_sum

packet = Packet()
packet.parse(transmission)
print(packet.version_sum())
