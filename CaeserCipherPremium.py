text = input("Enter your message: ")
cip= int(input("Press 1 for cipher and 0 for decipher "))
shift = int(input("Enter value of shift (1 - 25): "))

while shift < 1 or shift > 25:
    shift = int(input("Enter value of shift (1 - 25): "))

cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    
    if char.islower():
        lowletter = True
    else: lowletter = False
    
    if cip == 1:
        char = char.upper()
        code = ord(char) + shift
        if code > ord('Z'):
            code = (ord('A')+ code - ord('Z') - 1)
        if lowletter == True:
            cipher += chr(code).lower()
        else: cipher+=chr(code)
            
    elif cip == 0:
        char = char.upper()
        code = ord(char) - shift
        if code < ord('A'):
            code = (ord('Z') + code - ord('A') +1)
       
        if lowletter == True:
            cipher += chr(code).lower()
        else: cipher+=chr(code)

print(cipher)
