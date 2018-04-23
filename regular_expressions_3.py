
import re

pattern = r'pam'

match = re.search(pattern, 'eggspamsausage')
if match:
	print(match.group())
	print(match.start())
	print(match.end())
	print(match.span())




import re

pattern = r'test'

match = re.search(pattern, 'some test')

print(match.start())
print(match.end())
