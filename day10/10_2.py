rawdata = open('input_test.txt').read().splitlines()
rawdata = open('input.txt').read().splitlines()

def remain_chunk(ligne):
    pile = []
    for car in ligne:
        if car in {'(', '{', '[', '<'}:
            pile.append(car)
        else:
            ouvrant = pile.pop()
            if ouvrant + car not in {'()', '{}', '[]', '<>'}:
                return 'corrupted'
    return ''.join(car for car in pile)

incompletes = [line for line in rawdata if not remain_chunk(line) == 'corrupted']

    
def score(chunk):
    chunk = chunk[::-1]
    s = 0
    values = {'(': 1, '[': 2, '{': 3, '<': 4}
    for car in chunk:
        s = 5*s + values[car]
    return s

scores = [score(remain_chunk(line)) for line in incompletes]
scores.sort()
print(scores[len(scores)//2])