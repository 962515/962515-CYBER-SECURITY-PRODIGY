import re

def password_strength(password):
    strength = {"length": False, "uppercase": False, "lowercase": False, "numbers": False, "special": False}

    if len(password) >= 8:
        strength["length"] = True
    if re.search(r"[A-Z]", password):
        strength["uppercase"] = True
    if re.search(r"[a-z]", password):
        strength["lowercase"] = True
    if re.search(r"[0-9]", password):
        strength["numbers"] = True
    if re.search(r"[\W_]", password):
        strength["special"] = True

    score = sum(strength.values())
    
    feedback = ""
    if score == 5:
        feedback = "Very Strong"
    elif score == 4:
        feedback = "Strong"
    elif score == 3:
        feedback = "Moderate"
    elif score == 2:
        feedback = "Weak"
    else:
        feedback = "Very Weak"
    
    return strength, feedback

# Test the function
password =input("enter the password for checking:")
strength, feedback = password_strength(password)
print(f"Password Strength: {strength}")
print(f"Feedback: {feedback}")
