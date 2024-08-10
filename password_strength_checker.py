import re

def check_password_strength(password):
    
    strength = 0
    conditions = [
        (r'[a-z]', "lowercase letter"),
        (r'[A-Z]', "uppercase letter"),
        (r'[0-9]', "digit"),
        (r'[@$!%*?&#]', "special character")
    ]
    
    
    for pattern, description in conditions:
        if re.search(pattern, password):
            strength += 1
    
    
    if len(password) >= 8:
        strength += 1

    
    if strength < 3:
        return "Weak"
    elif strength == 3:
        return "Okay"
    else:
        return "Strong"


password = input("Enter a password: ")
strength = check_password_strength(password)
print(f"The password is {strength}.")
