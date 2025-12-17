def candidate_elimination(data):
    S = ['ϕ'] * (len(data[0]) - 1)
    G = [['?' for _ in range(len(S))]]

    for row in data:
        if row[-1] == 'Yes':
            G = [g for g in G if all(g[i] == '?' or g[i] == row[i] for i in range(len(S)))]
            for i in range(len(S)):
                if S[i] == 'ϕ':
                    S[i] = row[i]
                elif S[i] != row[i]:
                    S[i] = '?'
        else:
            newG = []
            for g in G:
                for i in range(len(S)):
                    if g[i] == '?' and S[i] != row[i]:
                        temp = g.copy()
                        temp[i] = S[i]
                        newG.append(temp)
            G = newG
    return S, G

data = [
    ['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
    ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
    ['Rainy','Cold','High','Strong','Warm','Change','No'],
    ['Sunny','Warm','High','Strong','Cool','Change','Yes']
]

print(candidate_elimination(data))
