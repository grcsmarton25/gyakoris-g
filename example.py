import os
import random as rnd
os.system('cls')

def isitPerfect(n):
    if n == 1 or n == 0:
        return False
    else:
        divNumbers = [1]
    for i in range(2, n, 1):
        if n % i == 0:
            divNumbers.append(i)
    
    return sum(divNumbers) == n       

def randomGenerator(s, e, a):
    numbers = list()
    for i in range(a):
        numbers.append(rnd.randint(s, e))
    return numbers
        
def makeNumber(text):
    isCorrect = False
    while True:
        n = input(text)
        try:
            n = int(n)
            #isCorrect = True
            return n
        except ValueError:
            print("Helytelen érték.")

perfectNumbers = list()
perfectNumFreq = dict()
startMessage = "Kezdő érték: "
endMessage = "Végérték: "
amountMessage = "Értékek száma: "

start = makeNumber(startMessage)
end = makeNumber(endMessage)
amount = makeNumber(amountMessage)

randomNumbers = randomGenerator(start, end, amount)
#print(randomNumbers)
for n in randomNumbers:
    if isitPerfect(n):
        perfectNumbers.append(n)
        
for n in perfectNumbers:
    if n in perfectNumFreq.keys():
        perfectNumFreq[n] += 1
    else:
        perfectNumFreq[n] = 1
        
for key in perfectNumFreq.keys():
    print(f"{key}: {perfectNumFreq[key]} db")        