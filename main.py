import socket
import time

from colorama import Fore, Back, init
from time import sleep
from cfonts import render

init(convert=True)

valid = False
file_mode = False
url_mode = False
output_done = False
output = False
done = False

greetings = render(' URL to IP', colors=['red', 'yellow'])

spacer = "          "

output_file_name = "output"
output_file_number = 1
output_file = output_file_name + str(output_file_number) + ".txt"

ip_list = []


def url_to_ip():

	global valid
	global file_mode, url_mode
	global output_done, done
	global output_file, output_file_name, output_file_number, output

	print(spacer, Fore.BLACK + Back.WHITE + ' By ziadOUA' + Fore.RESET, Back.RESET)

	while not valid:
		print(' ')
		conversion_mode = input("Conversion method \n u : by url \n f : by file \n>>> ")
		if conversion_mode == "u":
			url_mode = True
			file_mode = False
			valid = True
		elif conversion_mode == "U":
			url_mode = True
			file_mode = False
			valid = True
		elif conversion_mode == "f":
			url_mode = False
			file_mode = True
			valid = True
		elif conversion_mode == "F":
			url_mode = False
			file_mode = True
			valid = True
	valid = False

	if file_mode:

		while not valid:
			try:
				print(' ')
				file_path = str(input(".txt File path >>> "))
				open(file_path)
				valid = True
			except:
				print(' ')
				print(Fore.RED + "The file path isn't valid" + Fore.RESET)
		valid = False

		with open(file_path) as url:
			for hostname in url:
				hostname = hostname.rstrip()
				try:
					ip = socket.gethostbyname(hostname)
					print(' ')
					print(hostname)
					print('>', end=' ')
					print(Fore.BLACK, Back.GREEN + ip + Fore.RESET, Back.RESET, end='')
					print(' ')
					ip_list.append(ip)
				except:
					print(' ')
					print(hostname)
					print('>', end=' ')
					print(Fore.BLACK, Back.RED + ' Not Valid' + Fore.RESET, Back.RESET, end='')
					print(' ')
					continue

			while not valid:
				print(' ')
				is_output = input("Create an output file ? \n y : yes \n n : no \n>>> ")
				if is_output == "y":
					output = True
					valid = True
				elif is_output == "Y":
					output = True
					valid = True
				elif is_output == "n":
					output = False
					valid = True
				elif is_output == "N":
					output = False
					valid = True
			valid = False

			while not output_done:
				if output:
					try:
						with open(output_file, 'x') as file:
							file.write('\n'.join(ip_list))
							output_done = True
					except:
						output_file_number = int(output_file_number) + 1
						output_file = output_file_name + str(output_file_number) + ".txt"
				elif not output:
					output_done = True

	elif url_mode:
		while not done:
			print(' ')
			hostname = input("Enter the URL, or \n q : to quit \n>>> ")
			if hostname == "q":
				done = True
			if hostname == "Q":
				done = True
			if hostname != "q":
				try:
					ip = socket.gethostbyname(hostname)
					print(' ')
					print(hostname)
					print('>', end=' ')
					print(Fore.BLACK, Back.GREEN + ip + Fore.RESET, Back.RESET)
				except:
					print(' ')
					print(hostname)
					print('>', end=' ')
					print(Fore.BLACK, Back.RED + ' Not Valid' + Fore.RESET, Back.RESET, end='')
					print(' ')
					continue


print(greetings)

while not done:
	url_to_ip()

	while not valid:
		print(' ')
		is_user_done = input("Leave ? \n y : yes \n n : no \n>>> ")
		print(' ')
		if is_user_done == "y":
			done = True
			valid = True
		elif is_user_done == "Y":
			done = True
			valid = True
		elif is_user_done == "n":
			done = False
			valid = True
		elif is_user_done == "N":
			done = False
			valid = True
	valid = False

print(greetings)
time.sleep(2)
