# When editing a Wikipedia article,
# you can create a bulleted list by putting each list item on its own line and placing a star in front.
# But say you have a really large list that you want to add bullet points to.
# You could just type those stars at the beginning of each line, one by one.
# Or you could auto-mate this task with the following  short Python script


# Adds wikipedia bullet points to the start of
# each line of text on the clipboard.add()

# 23:14 26th july 2020

# When this program is run,
# it replaces the text on the clipboard with text that has stars at the start of each line.
#  Now the program is complete, and you can try running it with text copied to the clipboard.


import pyperclip

text = pyperclip.paste()

# separting lines and adding stars.

lines = text.split('\n')
for i in range(len(lines)):  # loop thorugh all indexes for 'lines' list.
    lines[i] = '* ' + lines[i]  # adding star to each string in 'lines' list.

text = '\n'.join(lines)

pyperclip.copy(text)
