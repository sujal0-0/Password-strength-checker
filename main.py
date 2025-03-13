import re

def check_password_strength(password):
    strength = 0
    suggestions = []
    if len(password) >= 8:
       strength += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        suggestions.append("Add at least one uppercase letter.")
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        suggestions.append("Add at least one lowercase letter.")
    if re.search(r'\d', password):
        strength += 1
    else:
        suggestions.append("Add at least one number.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        suggestions.append("Add at least one special character.")
    if strength == 5:
        return "Strong password! Great job!"
    elif strength >= 3:
        return "Medium password. Suggestions to improve:\n" + "\n".join(suggestions)
    else:
        return "Weak password. Suggestions to improve:\n" + "\n".join(suggestions)


user_password = input("Enter your password: ")
print(check_password_strength(user_password))
