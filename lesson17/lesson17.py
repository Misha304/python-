"""
Написати функцію, що приймає на вхід строку, а повертає її перевернутою. 
Приклад: abc —> cba. 
Примітка: ❌У цьому завданні заборонено виростовувати зрізи. 
"""

def reverse_string(string):
    reversed_string = ''
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string


print(reverse_string('abcde'))