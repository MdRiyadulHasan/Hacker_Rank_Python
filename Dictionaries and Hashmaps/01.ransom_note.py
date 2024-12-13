#!/bin/python3

import math
import os
import random
import re
import sys

def checkMagazine(magazine, note):
    from collections import Counter
    magazine_dic = Counter(magazine)
    for word in note:
        if magazine_dic.get(word,0)==0:
            print("No")
            return
        magazine_dic[word]-=1
    print("Yes")
        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
