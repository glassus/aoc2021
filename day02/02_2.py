data_str = open('input1.txt').read().splitlines()
#data_str = open('input_test.txt').read().splitlines()


data = [chaine.split(' ') for chaine in data_str] 

hor = 0
depth = 0
aim = 0

for couple in data:
    if couple[0] == 'forward':
        hor += int(couple[1])
        depth += aim * int(couple[1])
        
    if couple[0] == 'down':
        aim += int(couple[1])
        
    if couple[0] == 'up':
        aim -= int(couple[1])
        
      
print(hor*depth)