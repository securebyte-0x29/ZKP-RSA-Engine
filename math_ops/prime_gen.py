import random
import math

def is_prime(rand_num):
    
    flag = True
    limit = int(math.sqrt(rand_num)+1)
    for i in range(2,limit):
        if rand_num % i == 0:
            flag = False
    if flag:
        return True
    return False

def gen_prime():
    while True:
        rand_num = random.randint(10001,99999)
        if rand_num & 1 != 0:
            if is_prime(rand_num):
                return rand_num
