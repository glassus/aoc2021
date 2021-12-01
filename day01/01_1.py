data_str = open('input1.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()


data = [int(chaine) for chaine in data_str] 

sol = sum([1 for i in range(1, len(data)) if data[i] > data[i-1]])

print(sol)