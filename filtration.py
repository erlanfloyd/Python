                #----------------- Фильтрация --------------#

names = ['jack', 'john', 'david', 'claire']

new_names = [n for n in names if n.startswith('j')]

print(new_names)

                #------------------ Теперь запишем традиционным циклом эту же фильтрацию ---------------#

new_names = []
for n in names:
    if n.startswith('j'):
        new_names.append(n)

print(new_names)                                        