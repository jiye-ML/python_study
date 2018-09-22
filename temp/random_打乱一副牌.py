'''
使用 random 模块打乱一副牌
'''
import random
try:
    # available in 2.0 and later
    shuffle = random.shuffle
except AttributeError:
    def shuffle(x):
        for i in range(len(x)-1, 0, -1):
            # pick an element in x[:i+1] with which to exchange x[i]
            j = int(random.random() * (i+1))
            x[i], x[j] = x[j], x[i]

cards = [i for i in range(52)]
shuffle(cards)
myhand = cards[:5]
print(myhand)