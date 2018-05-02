
import re 

pattern = r"[^0-9]"

m = re.search(pattern, "Hi, there!")

print(m)
