# An insecure password locker program
# 22:02 26th july 2020
# dinesh pandikona aka tesla atoz
# it is insecure coz all passwords are stored in this single file.


# future option : Improve this program by adding features like updating passwords and try to make it user friendly.


import pyperclip  # package for copying to clipboard
import sys  # sys.argv is a variable which contains the cmd line arguments


# Here, I stored the passwords (dictionary datastructure.)
PASSWORDS = {
    'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB',
    'geeksgeeks': 'VmALvQyKAxiVH5G8v01if1MLZF3s',
    'bag': '12345'
}

# if the name of the account , that means only if this program is run without any cmd arguments ,
# it should tell about this program.
if len(sys.argv) < 2:
    print('Usage : python passwordLocker[account] - copy account password')
    sys.exit()


# first command line arg is the account name.
# storing the account name whose pwd need to copy which is provided from the cmd line arguments.
account = sys.argv[1]

# Checking if the account is present in the password dictionary and displaying necessary info to the user.
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + 'copied to clipboard')
else:
    print('there is no account nameed' + account)


# Use cases of this program

# 1. for storing frequently used data which is often helpful for the user to directly
# copy to clipbord.

# like passwords, or any block of text for sending massive emails.
