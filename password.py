password = input('enter password:\n')
has_number = any(char.isdigit() for char in password)
has_letter = any(char.isalpha() for char in password)
if len(password) < 8:
    print('password is not strong enough')
elif has_number*has_letter:
    print('password is strong enough')
else: print('password is not strong enough')