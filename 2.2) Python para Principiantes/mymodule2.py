import mymodule1

mymodule1.add(45, 45)
mymodule1.substract(90, 45)

##########################################################

from mymodule1 import add, substract

add(20, 30)
substract(50, 40)

##########################################################

from colorama import Fore, Style, init
init(convert=True)
print(Fore.RED + "Hello World")