# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

# situation:
#         Say you have the boring task of finding every phone number and email
#         address in a long web page or document. If you manually scroll through
#         the page, you might end up searching for a long time. But if you had a program
#         that could search the text in your clipboard for phone numbers and
#         email addresses, you could simply press ctrl-A to select all the text, press
#         ctrl-C to copy it to the clipboard, and then run your program. It could
#         replace the text on the clipboard with just the phone numbers and email
#         addresses it finds.

# Functionality :
# • Get the text off the clipboard.
# • Find all phone numbers and email addresses in the text.
# • Paste them onto the clipboard.

# what am i gng to do? :
# • Use the pyperclip module to copy and paste strings.
# • Create two regexes, one for matching phone numbers and the other for
# matching email addresses.
# • Find all matches, not just the first match, of both regexes.
# • Neatly format the matched strings into a single string to paste.
# • Display some kind of message if no matches were found in the text.


phone number's regex code is United States of America.. check it out in browser.

import pyperclip
import re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                   # 1  area code  has 1 group
(\s|-|\.)?                           # 2 separator  has 1 group
(\d{3})                             #  3 first 3 digits has 1 group
(\s|-|\.)                           # 4 separator  has 1 group
(\d{4})                              # 5 last 4 digits    has 1 group
(\s*(ext|x|ext.)\s*(\d{2,5}))?      # 6 ,7, 8 extension has 3 groups
)''', re.VERBOSE)


# Create email regex.
emailRegex = re.compile(r'''(
 [a-zA-Z0-9._%+-]+      # username
 @                  # @ symbol
[a-zA-Z0-9.-]+          # domain name
(\.[a-zA-Z]{2,4})       # dot-something  has 1 group
)''', re.VERBOSE)


# find matches in clipboard text
text = str(pyperclip.paste())

phonematches = []
emailmatches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    phonematches.append(phoneNum)
for groups in emailRegex.findall(text):
    emailmatches.append(groups[0])


matchYouNeed = input(
    "Enter 1 for phone match or 2 for email match to copy on to clipboard.")


if matchYouNeed == '1':
    if len(phonematches) > 0:
        pyperclip.copy('\n'.join(phonematches))
        print('Copied to clipboard:')
        print('\n'.join(phonematches))
    else:
        print('No phone numbers found.')

elif matchYouNeed == '2':
    if len(emailmatches) > 0:
        pyperclip.copy('\n'.join(emailmatches))
        print('Copied to clipboard:')
        print('\n'.join(emailmatches))
    else:
        print('No  email addresses found.')

else:
    print("Sorry, You need to enter right code, either 1 or 2.")
