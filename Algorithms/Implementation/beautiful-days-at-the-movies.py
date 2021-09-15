
def reversed(number):
    num_reversed = ""
    num_str = str(number)
    for i in range(len(num_str) - 1, -1, -1):
        num_reversed += num_str[i]
    return int(num_reversed)

def beautiful_movies(start, end, divisor):
    total_movies = 0
    for i in range(start, end + 1):
        if abs(i - reversed(i)) % divisor == 0:
            total_movies += 1
    return total_movies

start, end, divisor = list(map(int, input().strip().split(' ')))
print (beautiful_movies(start, end, divisor))