

import os
import math

# Complete the encryption function below.
def encryption(s):
    result = ""
    if math.sqrt(len(s)) % 1 == 0:
        row = col = int(math.sqrt(len(s)))
    else:
        row = int(math.sqrt(len(s)))
        col = int(math.sqrt(len(s)) + 1)

    for i in range(col):
        j = i
        while j < len(s):
            result += s[j]
            j += col 
        result += " "
    return result

if __name__ == '__main__':
    result = encryption(input())
    print (result + '\n')
