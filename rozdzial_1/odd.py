from datetime import datetime
from random import randint
import time


odds = [ 1, 3, 5, 7, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]


for i in range(5):
    right_this_minute = datetime.today().minute
    wait = randint(1, 60)
    time.sleep(wait)
    
    if right_this_minute in odds:
        print("Ta minuta wydaje sie dość nieparzysta")
    else:
        print ("Minuta parzysta")

