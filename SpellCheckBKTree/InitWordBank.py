import pandas as pd
from BKTree import BKTree

def initWordBank(func):
    wordBank = BKTree(func)
    csvthing = pd.read_csv("WordBanks/3000.csv")

    for i in csvthing['a']:
        wordBank.add(i)

    return wordBank