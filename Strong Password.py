import re


def isStrongPassword(password):
    passlenRegex = re.compile(r".{8,}")
    passUpperRegex = re.compile(r"[A-Z]+")
    passLowerRegex = re.compile(r"[a-z]+")
    passDigitRegex = re.compile(r"\d+")

    if passlenRegex.search(password) is None:
        return False
    if passUpperRegex.search(password) is None:
        return False
    if passLowerRegex.search(password) is None:
        return False
    if passDigitRegex.search(password) is None:
        return False
    return True


strong = isStrongPassword("ThisIsAStrongPa55word")

if strong:
    print("Your password is strong!")
else:
    print("Your password is weak! Please include atleast one Uppercase, Lowercase and digit. Make sure password is atleast 8 characters long")
