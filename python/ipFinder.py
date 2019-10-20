# Python3 code to display hostname and IP address 
  
import json
import socket 

def save_IP(nameChoice): 
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	IP = s.getsockname()[0]
	
	machine_name = {nameChoice: IP}
	
	with open('names.JSON') as jsonIP:
		names_data = json.load(jsonIP)
		
	names_data.update(machine_name) # adds to JSON file names_data the ip address and name of the machine
	
	with open('names.JSON', 'w') as jsonIP:
			json.dump(names_data, jsonIP)

def get_IP():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	host_ip = s.getsockname()[0]
	return host_ip  	

def save_name_password(nameChoice):
	namePword = input("Password: ")
	namePword2 = input("Type again: ")
	while namePword != namePword2:
		namePword = input("Password: ")
		namePword2 = input("Type again: ")
	save_IP(nameChoice)



