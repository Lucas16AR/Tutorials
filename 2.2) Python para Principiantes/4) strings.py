from typing import MutableMapping


myStr = 'Hello World'

print('Python, ' + myStr)
print(f'Python, {myStr}') #La f es para declarar que hay una variable entre corchetes
print('Python, {0}'.format(myStr))

print(dir(myStr)) #podemos ver propiedades o metodos

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('Hello', 'Bye'))
print(myStr.count('d'))
print(myStr.startswith('Hello'))
print(myStr.find('r'))
print(myStr[0])
print(myStr[-1])
print(myStr.replace('Hello', 'Bye').upper()) #metodos encadenados
#estos son ejemplos de algunos metodos que se pueden usar
