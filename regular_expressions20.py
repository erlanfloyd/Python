                      #------------------ Email Extraction -------------------#
import re

pattern = r"([\w\.-] + )@([\w\. - ] + )(\.[\w\.] + )"
str = "Please contract info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())
                          