# Password Strength Analyzer

A Python-based Password Strength Analyzer that evaluates password security using multiple checks such as length, complexity, entropy, common-password detection, and pattern analysis.

---

## Features

### Password Length Analysis

Checks password length and categorizes security level.

| Length | Rating |
|----------|----------|
| < 8 | Weak |
| 8-11 | Medium |
| 12-15 | Strong |
| 16+ | Very Strong |

---

### Complexity Validation

Checks for:

- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

Example:

```text
Admin123!
```

Results:

```text
PASS Uppercase
PASS Lowercase
PASS Number
PASS Special Character
```

---

### Common Password Detection

Detects frequently used passwords such as:

```text
password
123456
admin
qwerty
welcome
```

---

### Pattern Detection

Identifies weak password patterns:

```text
123456
abcdef
qwerty
111111
aaaaaa
```

---

### Entropy Calculation

Calculates password entropy using:

```python
entropy = length * log2(character_set_size)
```

Entropy indicates how resistant a password is to brute-force attacks.

---

### Password Suggestions

Weak passwords receive suggestions for improvement.

Example:

```text
Input:
admin123

Suggestion:
admin123A@XX
```

---

### bcrypt Password Hashing

Passwords are hashed using bcrypt before storage.

Example:

```python
bcrypt.hashpw(password.encode(), bcrypt.gensalt())
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/yourusername/password-strength-analyzer.git
```

Move into project directory:

```bash
cd password-strength-analyzer
```

Install dependencies:

```bash
pip install bcrypt
```

---

## Run

```bash
python password_analyzer.py
```

---

## Sample Output

```text
==================================================
PASSWORD STRENGTH ANALYZER
==================================================

Enter Password: Admin123!

Password Analysis
--------------------------------------------------
Length: 9
Entropy: 58.99 bits
Strength Rating: STRONG

Complexity Checks

Uppercase: PASS
Lowercase: PASS
Numbers: PASS
Special Characters: PASS

Password Hash (bcrypt):
$2b$12$xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Skills Demonstrated

- Python
- Cybersecurity Fundamentals
- Authentication Security
- Password Policy Enforcement
- Entropy Calculation
- Cryptography
- bcrypt
- Secure Coding Practices

---

## Future Improvements

- GUI using Tkinter
- Flask Web Version
- Password Breach Database Check
- Password History Validation
- Active Directory Password Policy Integration
- Splunk Logging Integration

---

## Author

Karthikeyan

SOC Analyst | Blue Team Enthusiast
