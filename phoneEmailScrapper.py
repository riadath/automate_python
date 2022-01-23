import re, pyperclip

phoneNumberRegex = re.compile(r'''(
((\d\d\d)|(\(\d\d\d\)))?
-
\d\d\d
-
\d\d\d\d
(((ext(\.)?)|x)(\s?)\d{2,5})?
)''',re.VERBOSE)

emailRegex = re.compile(r'''
[a-zA-Z0-9_.]+
@
\w+\.com|org''',re.VERBOSE)


textStr = pyperclip.paste()
print(textStr)

allPhoneNumbers = phoneNumberRegex.findall(textStr)

allEmailAdresses = emailRegex.findall(textStr)

print("______________PHONE______________")
cnt = 0
for i in allPhoneNumbers:
    cnt += 1
    print("%d."%cnt+i[0])

print("______________EMAILS ______________")
cnt = 0
for i in allEmailAdresses:
    cnt += 1
    print("%d."%cnt+i)
