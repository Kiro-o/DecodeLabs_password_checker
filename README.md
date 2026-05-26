# Password Strength Checker

This is a simple Python script I built for Project 1 during my DecodeLabs internship. It checks how strong a password is based on common security rules.

## What it checks:
- Length (between 8 and 12 characters)
- Needs at least one uppercase letter (A-Z)
- Needs at least one lowercase letter (a-z)
- Needs at least one number and a special character (like !, @, #, etc.)

## Safety stuff I added:
- It handles empty inputs so it doesn't crash.
- Used `secrets.compare_digest` for password verification to stop timing attacks.
- Cleans up the password variable from memory (`del`) right after checking it.

## How to run it:
Just run `python password_checker.py` in your terminal and type a password to test it.
