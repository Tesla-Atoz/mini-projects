# birthday Or important dates storage program.
# 22:19 26th july 2020
# dinesh pandikona aka tesla atoz
# it stores and returns data upon request

# future option : Improve this program by making it more user-friendly and validation


# Here, I am storing some birthday dates.(dictionary data structure.)
birthdays = {
    'dinesh': 'Sept 13',
    'deepali': 'Sept 22',

}

# this code block asks user to enter name(key) and displays his/her birthday
# Entering nothing can break the loop.
while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    # I am updating the data base if the info doesnt exist already.
    else:
        print('i do not have birthday information for' + name)
        print('What is their birthday')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')


# Use cases of this program

# 1. for storing huge data and retreving their values.

# like huge student databse and you want to retrieve some X
# student's birthday. Here you can just type name and get his birthday


# it can applicable in many similar cases if furtherly improved.
