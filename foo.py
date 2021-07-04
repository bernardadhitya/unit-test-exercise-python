import random
import time

def split_to_list(word):
    return word.split(' ')

def roll_dice():
    return random.randint(1,6)

def fetch_username():
    time.sleep(3)
    return 'bernardadhitya'