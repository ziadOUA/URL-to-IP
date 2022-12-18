# -*- coding: utf-8 -*-

import socket
import time
import os
import datetime

from colorama import Fore, Back, init
from time import sleep, perf_counter
from pyfiglet import Figlet

init(convert=True)

valid = False
file_mode = False
url_mode = False
output_done = False
output = False
done = False

start = Figlet(font='univers')

output_file_name = "output"
output_file_number = 1
output_file = output_file_name + str(output_file_number) + ".txt"

ip_list = []

slash = '/'
arrow = u'→'


def url_to_ip():

	global valid
	global file_mode, url_mode
	global output_done, done
	global output_file, output_file_name, output_file_number, output

	print(Fore.BLACK + Back.WHITE + ' By ziadOUA ' + Fore.RESET + Back.RESET)

	while not valid:
		print('')
		conversion_mode = input("Chose your conversion method \n u : by url \n f : by file \n>>> ")
		if conversion_mode in ['u', 'U']:
			url_mode = True
			file_mode = False
			valid = True
		elif conversion_mode in ['f', 'F']:
			url_mode = False
			file_mode = True
			valid = True
	valid = False

	if file_mode:

		while not valid:
			try:
				print('')
				file_path = str(input("Enter the path to the .txt file >>> "))
				open(file_path)
				valid = True
			except FileNotFoundError:
				print(' ')
				print(Fore.RED + "The file path isn't valid" + Fore.RESET)
		valid = False

		start_time = time.perf_counter()

		with open(file_path) as url:
			for old_hostname in url:
				old_hostname = old_hostname.rstrip()
				hostname = old_hostname
				try:
					if hostname.find("/") != -1:
						print(' ')
						print(Fore.CYAN + "The URL provided isn't only a domain name" + Fore.RESET, end='')
						print(' ')
						hostname = hostname.split(slash)[2]
					else:
						pass
					ip = socket.gethostbyname(hostname)
					print(' ')
					if old_hostname == hostname:
						print(hostname)
					else:
						print(old_hostname, arrow, hostname)
					print(arrow, end=' ')
					print(Fore.BLACK, Back.GREEN + ip + Fore.RESET, Back.RESET, end='')
					print(' ')
					ip_list.append(ip)
				except OSError:
					print(' ')
					print(hostname)
					print(arrow, end=' ')
					print(Fore.BLACK, Back.RED + ' Not Valid' + Fore.RESET, Back.RESET, end='')
					print(' ')
					continue

			end_time = time.perf_counter()
			elapsed_time = end_time - start_time
			elapsed_time = elapsed_time.__round__(0)
			print('')
			elapsed_time = str(datetime.timedelta(seconds=elapsed_time))
			print(f'The execution took {elapsed_time}s')

			while not valid:
				print(' ')
				is_output = input("Create an output file ? \n y : yes \n n : no \n>>> ")
				if is_output in ['y', 'Y']:
					output = True
					valid = True
				elif is_output in ['n', 'N']:
					output = False
					valid = True
			valid = False

			while not output_done:
				if output:
					try:
						with open(output_file, 'x') as file:
							file.write('\n'.join(ip_list))
							output_done = True
					except FileExistsError:
						output_file_number = int(output_file_number) + 1
						output_file = output_file_name + str(output_file_number) + ".txt"
				elif not output:
					output_done = True

	elif url_mode:
		while not done:
			print(' ')
			old_hostname = input("Enter the URL, or \n q : to quit the mode \n>>> ")
			hostname = old_hostname
			if hostname.find("/") != -1:
				print(' ')
				print(Fore.CYAN + "The URL provided isn't only a domain name" + Fore.RESET, end='')
				print(' ')
				hostname = hostname.split(slash)[2]
			else:
				pass
			if hostname in ['q', 'Q']:
				done = True
			if hostname != "q":
				try:
					ip = socket.gethostbyname(hostname)
					print(' ')
					if old_hostname == hostname:
						print(hostname)
					else:
						print(old_hostname, arrow, hostname)
					print(arrow, end='')
					print(Fore.BLACK, Back.GREEN + ' ' + ip + Fore.RESET, Back.RESET)
				except OSError:
					print(' ')
					print(hostname)
					print(arrow, end='')
					print(Fore.BLACK, Back.RED + ' Not Valid' + Fore.RESET, Back.RESET, end='')
					print(' ')
					continue


if __name__ == '__main__':
	while not done:
		os.system('CLS')
		print(start.renderText('URL to IP'))
		url_to_ip()

		while not valid:
			print(' ')
			is_user_done = input("Leave ? \n y : yes \n n : no \n>>> ")
			print(' ')
			if is_user_done in ['y', 'Y']:
				done = True
				valid = True
			elif is_user_done in ['n', 'N']:
				done = False
				valid = True
		valid = False

print(start.renderText('URL to IP'))
time.sleep(3)
