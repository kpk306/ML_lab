def biased_learner(data):
    for x, y in data:
        if y == 1:
            return x

def unbiased_learner():
    return "Cannot generalize"

data = [
    ([1,0,1],0),
    ([1,1,1],1),
    ([0,1,1],0)
]

print(biased_learner(data))
print(unbiased_learner())
