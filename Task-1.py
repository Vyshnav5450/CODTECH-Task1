import re

def password_strength(password):
    strength = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Complexity Checks
    if re.search("[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search("[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search("[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one digit.")

    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Uniqueness Check
    if len(set(password)) >= len(password) * 0.6:  # At least 60% of characters should be unique
        strength += 1
    else:
        feedback.append("Password should have more unique characters.")

    # Feedback and Strength
    if strength == 6:
        return "Strong Password", feedback
    elif strength >= 3:
        return "Medium Strength Password", feedback
    else:
        return "Weak Password", feedback

# Example usage
password = input("Enter your password: ")
strength, feedback = password_strength(password)
print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for comment in feedback:
        print(f" - {comment}")
