"""
Basically, python strings handle the backlash character weird \. It used as an escape character.
To use the backslashcharacter, you need to escape the backslash character with another backslash character,
resulting in \\. Because a regex uses the backslash character a lot, it becomes really annoying to use regular strings. Therefore, we use raw python strings. When an 'r' or 'R' prefix is present, a character following a backslash is included in the string without change, and all backslashes are left in the string. The way the parser is implemented means that a raw string can not end in an odd number of \ because backslash automatically includes the next character, without evaluating it, which means if you have an odd number, you can have weird behavior. You can still have an even number of backslashes. One confusing things is that when a string
is displayed, it displays escaped characters even though they are not part of the string..
"""

raw_string_value = r"\n"
regular_string_value = '\\n'
assert(raw_string_value == regular_string_value)
