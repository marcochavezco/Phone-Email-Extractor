# !pyhton3

import re, pyperclip

#  Phone regular expresion
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # Area code
    (\s|-|\.)?                          # Separator
    (\d{3})                             # 3 digits
    (\s|-|\.)                           # Separator
    (\d{4})                             # 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # Ext
    )''', re.VERBOSE)

# Email address regular expresion
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._+%-]+                   # username
    @                                   # @
    [a-zA-Z0-9.-]+                      # domain
    (\.[a-zA-Z0-9]{2,10})               # dot something
    )''', re.VERBOSE)


text = str(pyperclip.paste())

matches = []

# Finds phoneNum in text, changes format and appends phoneNum to matches
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '': # Checks if there is any extention
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
    
# Find and append email to matches
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copies results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to Clipboard')
    print('\n'.join(matches))
else: 
    print('No phone numbers or email addresses found')
