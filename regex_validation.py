# regex_validation.py
# Centralized validation logic using Regular Expressions

import re

# -----------------------------
# 1. EMAIL VALIDATION FUNCTION
# -----------------------------
def validate_email(email):
    """
    Validates email address using industry-standard regex.
    Example valid emails:
    user@example.com
    user.name123@gmail.co.in
    """
    if not email:
        return False, "Email cannot be empty"

    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.fullmatch(email_pattern, email):
        return True, "Valid email address"
    else:
        return False, "Invalid email format"


# ----------------------------------
# 2. INDIAN MOBILE NUMBER VALIDATION
# ----------------------------------
def validate_mobile(mobile):
    """
    Validates Indian mobile numbers.
    Rules:
    - Starts with 6,7,8,9
    - Exactly 10 digits
    """
    if not mobile:
        return False, "Mobile number cannot be empty"

    mobile_pattern = r'^[6-9]\d{9}$'

    if re.fullmatch(mobile_pattern, mobile):
        return True, "Valid Indian mobile number"
    else:
        return False, "Invalid mobile number (must be 10 digits & start with 6-9)"


# -----------------------------
# 3. PASSWORD VALIDATION
# -----------------------------
def validate_password(password):
    """
    Password rules:
    - Minimum 8 characters
    - At least one digit
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one special character
    """
    if not password:
        return False, "Password cannot be empty"

    password_pattern = (
        r'^(?=.*[a-z])'      # at least one lowercase
        r'(?=.*[A-Z])'       # at least one uppercase
        r'(?=.*\d)'          # at least one digit
        r'(?=.*[@$!%*?&])'   # at least one special character
        r'[A-Za-z\d@$!%*?&]{8,}$'  # minimum length 8
    )

    if re.fullmatch(password_pattern, password):
        return True, "Strong password"
    else:
        return False, (
            "Invalid password.\n"
            "Password must contain:\n"
            "- Minimum 8 characters\n"
            "- At least one uppercase letter\n"
            "- At least one lowercase letter\n"
            "- At least one digit\n"
            "- At least one special character (@$!%*?&)"
        )


# -----------------------------
# 4. MAIN FUNCTION
# -----------------------------
def main():
    print("=== REGEX VALIDATION SYSTEM ===\n")

    # Email input
    email = input("Enter Email: ").strip()
    status, message = validate_email(email)
    print("Email Check:", message, "\n")

    # Mobile input
    mobile = input("Enter Indian Mobile Number: ").strip()
    status, message = validate_mobile(mobile)
    print("Mobile Check:", message, "\n")

    # Password input
    password = input("Enter Password: ").strip()
    status, message = validate_password(password)
    print("Password Check:", message, "\n")


# -----------------------------
# 5. EDGE CASE TESTING
# -----------------------------
def test_edge_cases():
    print("\n=== EDGE CASE TESTING ===")

    test_emails = ["", "user@", "user@gmail", "user@gmail.com"]
    test_mobiles = ["", "12345", "987654321", "9876543210"]
    test_passwords = ["", "pass123", "Password1", "Password@1"]

    print("\nEmail Tests:")
    for e in test_emails:
        print(e, "->", validate_email(e)[1])

    print("\nMobile Tests:")
    for m in test_mobiles:
        print(m, "->", validate_mobile(m)[1])

    print("\nPassword Tests:")
    for p in test_passwords:
        print(p, "->", validate_password(p)[1])


# -----------------------------
# 6. PROGRAM EXECUTION
# -----------------------------
if __name__ == "__main__":
    main()
    test_edge_cases()
