""" getting more comfortable using regex
read about it here: https://www.w3schools.com/python/python_regex.asp
"""

import re

# https://stackoverflow.com/a/9477447/11304289 may use for Two Strings problem

s1 = "I don't even have time to explain why I don't have time to explain"
sComp1 = "therearenospacesherebecausetheyarenotrequired"
sComp2 = "pressftopayrespects"

sFor = re.findall('.?'*7, sComp1)

for bit in sFor:
    print(bit)