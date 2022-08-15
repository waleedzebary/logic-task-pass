# Q1 \ Write a method that will remove any given character from a String?

def remove_string(str, char):
    return str.replace(char, '')


string_tasting = input('Enter your string: ')
enter_string = input('Enter any string to delete this string: ')
print(remove_string(string_tasting, enter_string))

# --------------------------------------------------------------------------

# Q2/Write a program to find all prime numbers up to a given range of numbers?


def prime_number(number1, number2):
    prime = []
    for i in range(number1, number2 + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime.append(i)
    print(prime)


number = int(input("Enter your first numbers: "))
number2 = int(input('Enter your second numbers'))
prime_number(number, number2)

# ------------------------------------------------------------------------------

# Q3/write a function that count how many the given character repeated in a given string?


def counter_of_string_repeated(string, char):
    counter = 0
    for key in string:
        if key == char:
            counter += 1
    print('the counter of the char is:', counter)


string = input('Enter your string: ')
character = input('Enter a character: ')
counter_of_string_repeated(string, character)


