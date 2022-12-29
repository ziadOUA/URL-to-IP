# -*- coding: utf-8 -*-

import socket
import time
import os
import datetime

from colorama import Fore, Back, init
from pyfiglet import Figlet

init(convert=True)

valid = False
file_conversion_mode = False
url_conversion_mode = False
output_done = False
output = False
done = False

start = Figlet(font='univers')

output_file_name = "output"
output_file_number = 1
output_file = output_file_name + str(output_file_number) + ".txt"

hostname = None

file_path = None

ip_list = []

slash = '/'
arrow = u'→'
dot = '.'
separator = '|'


def url_to_ip():
    global valid
    global file_conversion_mode, url_conversion_mode
    global output_done, done
    global output_file, output_file_name, output_file_number, output

    print(f'{Fore.BLACK + Back.WHITE} By ziadOUA {Fore.RESET + Back.RESET} {separator}')

    while not valid:
        new_line()
        conversion_mode = input("Chose your conversion method \n u : by url \n f : by file \n>>> ")
        if conversion_mode in ['u', 'U']:
            url_conversion_mode = True
            file_conversion_mode = False
            valid = True
        elif conversion_mode in ['f', 'F']:
            url_conversion_mode = False
            file_conversion_mode = True
            valid = True
    valid = False

    if file_conversion_mode:
        file_mode()
    elif url_conversion_mode:
        url_mode()


def file_mode():
    global valid
    global hostname
    global file_conversion_mode, url_conversion_mode
    global output_done, done
    global output_file, output_file_name, output_file_number, output, file_path

    while not valid:
        try:
            new_line()
            file_path = str(input("Enter the path to the .txt file >>> "))
            open(file_path)
            valid = True
        except FileNotFoundError:
            new_line()
            print(f"{Fore.RED}The file path isn't valid{Fore.RESET}")
    valid = False

    start_time = time.perf_counter()

    with open(file_path) as url:
        for old_hostname in url:
            old_hostname = old_hostname.rstrip()
            hostname = old_hostname
            hostname_finder()
            try:
                ip = socket.gethostbyname(hostname)
                new_line()
                if old_hostname == hostname:
                    print(hostname)
                else:
                    print(old_hostname, arrow, hostname)
                print(f'{arrow} {Fore.BLACK + Back.GREEN} {ip} {Fore.RESET + Back.RESET} {separator}')
                ip_list.append(ip)
            except OSError:
                new_line()
                print(hostname)
                print(f'{arrow} {Fore.BLACK + Back.RED} Not Valid {Fore.RESET + Back.RESET} {separator}')
                continue

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        elapsed_time = elapsed_time.__round__(0)
        new_line()
        elapsed_time = str(datetime.timedelta(seconds=elapsed_time))
        print(f'The execution took {elapsed_time}s')

        while not valid:
            new_line()
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


def url_mode():
    global valid
    global hostname
    global file_conversion_mode, url_conversion_mode
    global output_done, done
    global output_file, output_file_name, output_file_number, output

    while not done:
        new_line()
        old_hostname = input("Enter the URL, or \n q : to quit the mode \n>>> ")
        hostname = old_hostname
        hostname_finder()
        if hostname in ['q', 'Q']:
            done = True
        if hostname != "q":
            try:
                ip = socket.gethostbyname(hostname)
                new_line()
                if old_hostname == hostname:
                    print(hostname)
                else:
                    print(old_hostname, arrow, hostname)
                print(f'{arrow} {Fore.BLACK + Back.GREEN} {ip} {Fore.RESET + Back.RESET} {separator}')
            except OSError:
                new_line()
                print(hostname)
                print(f'{arrow} {Fore.BLACK + Back.RED} Not Valid {Fore.RESET + Back.RESET} {separator}')
                continue


def hostname_finder():
    global hostname
    if hostname.find("/") != -1:
        new_line()
        print(f"{Fore.CYAN}The URL provided isn't only a domain name{Fore.RESET}")
        if hostname.count(slash) >= 3:
            finder = hostname.split(slash)[0]
            if finder.count(dot) >= 1:
                hostname = finder
            else:
                hostname = hostname.split(slash)[2]
        elif hostname.count(slash) == 2:
            finder = hostname.split(slash)[2]
            if finder.count(dot) >= 1:
                hostname = finder
            else:
                hostname = hostname.split(slash)[0]
        else:
            hostname = hostname.split(slash)[0]
    else:
        pass


def new_line():
    print('')


if __name__ == '__main__':
    while not done:
        os.system('CLS')
        print(start.renderText('URL to IP'))
        url_to_ip()

        while not valid:
            new_line()
            is_user_done = input("Leave ? \n y : yes \n n : no \n>>> ")
            new_line()
            if is_user_done in ['y', 'Y']:
                done = True
                valid = True
            elif is_user_done in ['n', 'N']:
                done = False
                valid = True
        valid = False

print(start.renderText('URL to IP'))
time.sleep(3)
