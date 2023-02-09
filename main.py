import urlToIp

from defaults.defaultFunctions import new_line
from colorama import Fore, Back, init
from pyfiglet import Figlet

init(convert=True)

valid = False
done = False

start = Figlet(font='univers')

print(start.renderText('URLTools'))

while not valid:
    new_line()
    is_user_done = input("Launch URL to IP ? \n y : yes \n n : no \n>>> ")
    new_line()
    if is_user_done in ['y', 'Y']:
        done = True
        valid = True
        urlToIp.init()
    elif is_user_done in ['n', 'N']:
        done = False
        valid = True
valid = False

test = input("OK")
