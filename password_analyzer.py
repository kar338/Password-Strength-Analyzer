import math
import re
import bcrypt

COMMON_PASSWORDS = {
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "welcome",
    "letmein",
    "password123",
    "abc123"
}


def calculate_entropy(password):
    charset_size = 0

    if re.search(r"[a-z]", password):
        charset_size += 26

    if re.search(r"[A-Z]", password):
        charset_size += 26

    if re.search(r"[0-9]", password):
        charset_size += 10

    if re.search(r"[^A-Za-z0-9]", password):
        charset_size += 32

    if charset_size == 0:
        return 0

    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)


def check_length(password):
    length = len(password)

    if length < 8:
        return 0
    elif length < 12:
        return 1
    elif length < 16:
        return 2
    else:
        return 3


def check_complexity(password):
    score = 0

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    return score


def check_common_password(password):
    return password.lower() in COMMON_PASSWORDS


def detect_patterns(password):
    patterns = [
        "123456",
        "abcdef",
        "qwerty",
        "password",
        "111111",
        "aaaaaa"
    ]

    for pattern in patterns:
        if pattern in password.lower():
            return True

    return False


def generate_suggestion(password):
    suggestion = password

    if not re.search(r"[A-Z]", suggestion):
        suggestion += "A"

    if not re.search(r"[0-9]", suggestion):
        suggestion += "7"

    if not re.search(r"[^A-Za-z0-9]", suggestion):
        suggestion += "@"

    while len(suggestion) < 12:
        suggestion += "X"

    return suggestion


def get_strength(password):
    score = 0

    score += check_length(password)
    score += check_complexity(password)

    entropy = calculate_entropy(password)

    if entropy >= 80:
        score += 2
    elif entropy >= 60:
        score += 1

    if score <= 3:
        return "WEAK"
    elif score <= 5:
        return "MEDIUM"
    elif score <= 7:
        return "STRONG"
    else:
        return "VERY STRONG"


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()


def main():
    print("=" * 50)
    print("PASSWORD STRENGTH ANALYZER")
    print("=" * 50)

    password = input("Enter Password: ")

    entropy = calculate_entropy(password)

    print("\nPassword Analysis")
    print("-" * 50)

    print(f"Length: {len(password)}")
    print(f"Entropy: {entropy} bits")
    print(f"Strength Rating: {get_strength(password)}")

    print("\nComplexity Checks")

    print(
        f"Uppercase: {'PASS' if re.search(r'[A-Z]', password) else 'FAIL'}"
    )
    print(
        f"Lowercase: {'PASS' if re.search(r'[a-z]', password) else 'FAIL'}"
    )
    print(
        f"Numbers: {'PASS' if re.search(r'[0-9]', password) else 'FAIL'}"
    )
    print(
        f"Special Characters: {'PASS' if re.search(r'[^A-Za-z0-9]', password) else 'FAIL'}"
    )

    if check_common_password(password):
        print("\nWARNING: Common password detected.")

    if detect_patterns(password):
        print("WARNING: Weak pattern detected.")

    if get_strength(password) in ["WEAK", "MEDIUM"]:
        print("\nSuggested Stronger Password:")
        print(generate_suggestion(password))

    print("\nPassword Hash (bcrypt):")
    print(hash_password(password))


if __name__ == "__main__":
    main()
