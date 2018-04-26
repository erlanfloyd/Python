names = ['john', 'rachel', 'kano']
colors = ['red', 'blue', 'green', 'yellow']
for name, color in zip(names, colors):
  print(name, '-->', color)
  
  
  
players = ['zizu', 'henry', 'ronni', 'david']
for player in reversed(players):
  print(player, end=' ')

print('\n', players)
print(players[::-1])

word = 'hello'
print(word[::-1])
