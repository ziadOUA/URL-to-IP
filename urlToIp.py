# -*- coding: utf-8 -*-

from defaults.defaultFunctions import new_line

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

hostname = ''
old_hostname = ''

file_path = ''

ip_list = []

slash = '/'
arrow = u'→'
dot = '.'
separator = '|'


def url_to_ip():
    global valid
    global file_conversion_mode, url_conversion_mode
    print(f'{Fore.BLACK + Back.WHITE} By ziadOUA {Fore.BLACK + Back.RESET} {separator} {Fore.RESET}')
    conversion_mode_prompt()
    if file_conversion_mode:
        file_mode()
    elif url_conversion_mode:
        url_mode()


def conversion_mode_prompt():
    global valid
    global url_conversion_mode, file_conversion_mode
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


def file_mode():
    global valid
    global hostname, old_hostname
    while not valid:
        file_path_input()
    valid = False
    start_time = time.perf_counter()
    with open(file_path) as url:
        for old_hostname in url:
            old_hostname = old_hostname.rstrip()
            hostname = old_hostname
            hostname_finder()
            hostname_conversion()
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        elapsed_time = elapsed_time.__round__(0)
        new_line()
        elapsed_time = str(datetime.timedelta(seconds=elapsed_time))
        print(f'The execution took {elapsed_time}s')
        file_output()


def file_output():
    global valid
    global output_done
    global output_file, output_file_name, output_file_number, output, file_path
    output_prompt()
    while not output_done:
        if output:
            try:
                with open(output_file, 'x') as file:
                    file.write('\n'.join(ip_list))
                    output_done = True
            except FileExistsError:
                output_file_number = int(output_file_number) + 1
                output_file = output_file_name + str(output_file_number) + '.txt'
        else:
            output_done = True


def output_prompt():
    global valid, output
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


def file_path_input():
    global valid, file_path
    try:
        new_line()
        file_path = str(input("Enter the path to the .txt file >>> "))
        open(file_path)
        valid = True
    except FileNotFoundError:
        new_line()
        print(f"{Fore.RED}The file path isn't valid{Fore.RESET}")


def url_mode():
    global valid
    global hostname, old_hostname
    global done
    while not done:
        new_line()
        old_hostname = input("Enter the URL, or \n q : to quit the mode \n>>> ")
        hostname = old_hostname
        hostname_finder()
        if hostname in ['q', 'Q']:
            done = True
        if hostname != "q":
            hostname_conversion()


def hostname_finder():
    global hostname
    if hostname.find("/") != -1:
        new_line()
        print(f"{Fore.CYAN}The URL provided isn't only a domain name{Fore.RESET}")

        cut_hostname = hostname.split(slash)
        while '' in cut_hostname:
            cut_hostname.remove('')
        for possible_hostname in cut_hostname:
            if possible_hostname.count(dot) >= 1:
                hostname = possible_hostname
                break
    else:
        pass


def hostname_conversion():
    global hostname, old_hostname
    try:
        ip = socket.gethostbyname(hostname)
        new_line()
        if old_hostname == hostname:
            print(hostname)
        else:
            print(old_hostname, arrow, hostname)
        print(f'{arrow} {Fore.BLACK + Back.GREEN} {ip} {Fore.BLACK + Back.RESET} {separator} {Fore.RESET}')
        ip_list.append(ip)
    except OSError:
        new_line()
        print(hostname)
        print(f'{arrow} {Fore.BLACK + Back.RED} Not Valid {Fore.BLACK + Back.RESET} {separator} {Fore.RESET}')


def init():
    global done, valid
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
                exit()
        valid = False
