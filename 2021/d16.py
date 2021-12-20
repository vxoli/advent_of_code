# AoC 2021 d16
# --- Day 16: Packet Decoder ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	# Test Data
	data[0]= 'D2FE28'
	#data[0] = '8A004A801A8002F478'
	
	return data[0]

def convert_hex_to_bin(hex_string):
	binary = bin(int(hex_string, base=16))[2:]
	binary = binary.zfill((len(hex_string)//4)*4)

	return binary

def parse_transmission(transmission):
	version = int(transmission[:3],2)
	transmission = transmission[3:]
	type_id = int(transmission[0:3],2)
	transmission = transmission[3:]
	if type_id == 4:
		# Literal packet
		number = []
		while True:
			last_packet_flag = transmission[0]
			transmission = transmission[1:]
			number += transmission[:4]
			transmission = transmission[4:]
			if last_packet_flag == '0': break
		number = (int(''.join(number),base=2))
		return (version, type_id, number)

	else:
		packets = []
		flag = transmission[0]
		transmission = transmission[1:]
		if flag == "0":
			# Operator packet
			length = int(transmission[:15],base=2)
			transmission = transmission[15:]
			d = transmission[:length]
			transmission = transmission[length:]
			while d:
				packets.append(parse_transmission(transmission))
		else:
			number = int(transmission[:11],base=2)
			transmission = transmission[11:]
			for _ in range(number):
				packets.append(parse_transmission(transmission))
		return(version, type_id, packets)


# MAIN
transmission_hex = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d16-input.txt')
transmission_bin = convert_hex_to_bin(transmission_hex)
parsed = parse_transmission(transmission_bin)
print(parsed)
