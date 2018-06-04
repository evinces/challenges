"""Convert string to camel case

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.

Examples
    to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

    to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

"""


def to_camel_case(text):
    text = text.replace("_", "-").split("-")
    return "".join(text[:1] + [word.capitalize() for word in text[1:]])
