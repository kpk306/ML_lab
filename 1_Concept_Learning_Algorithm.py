def find_s(data):
    h = ['ϕ'] * (len(data[0]) - 1)
    for row in data:
        if row[-1] == 'Yes':
            for i in range(len(h)):
                if h[i] == 'ϕ':
                    h[i] = row[i]
                elif h[i] != row[i]:
                    h[i] = '?'
    return h

data = [
    ['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
    ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
    ['Rainy','Cold','High','Strong','Warm','Change','No'],
    ['Sunny','Warm','High','Strong','Cool','Change','Yes']
]

print(find_s(data))
