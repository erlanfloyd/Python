                     #---------------- Search & Replace ---------------#

import re

str = 'My name is David. Hi David.'
pattern = r'David'
newstr = re.sub(pattern, 'Amy', str)
print(newstr)



import re

num = '07987549836'
pattern = r'9'
num = re.sub(pattern, '0', num)
print(num)
