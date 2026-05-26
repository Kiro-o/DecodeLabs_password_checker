import re
import secrets

def check_password_strength(password: str) -> tuple[int, list[str]]:
    if not password or password.isspace():
        return 0, ["Password is empty!"]
    
    score = 0
    feedback = []
    
    if 8 <= len(password) <= 12:
        score += 1
    else:
        feedback.append("Password length must be between 8 and 12 characters.")
        
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password must contain at least one uppercase letter (A-Z).")
        
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Password must contain at least one lowercase letter (a-z).")
        
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)
    
    if has_digit and has_special:
        score += 1
    else:
        feedback.append("Password must contain at least one number (0-9) and one special character (!@#$).")
        
    return score, feedback

def verify_admin_password(input_password: str, stored_password: str) -> bool:
    return secrets.compare_digest(input_password, stored_password)

def main():
    print("=== DecodeLabs - Password Strength Checker ===")
    
    user_password = input("Enter your password to check its strength: ")
    
    strength_score, feedback_list = check_password_strength(user_password)
    
    print(f"\nStrength Score: {strength_score}/4")
    
    if strength_score == 4:
        print("💪 Very Strong Password!")
    elif strength_score >= 2:
        print("⚠️ Moderate Password.")
    else:
        print("❌ Very Weak Password!")
        
    if feedback_list and strength_score < 4:
        print("\nSuggestions to improve your password:")
        for hint in feedback_list:
            print(f"- {hint}")
            
    del user_password
    
if __name__ == "__main__":
    main()