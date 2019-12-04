start = 130254
stop = 678275


validPasswords = 0
for i in range(start, stop):
    password = str(i)
    validPasswords += 1 if password[0] <= password[1] and \
                           password[1] <= password[2] and \
                           password[2] <= password[3] and \
                           password[3] <= password[4] and \
                           password[4] <= password[5] and \
                           ( password[0] == password[1] or \
                             password[1] == password[2] or \
                             password[2] == password[3] or \
                             password[3] == password[4] or \
                             password[4] == password[5] ) else 0

print(validPasswords)
                             
                           
