def is_disarium(num):
    return num == sum(int(digit) ** (i + 1) for i, digit in enumerate(str(num)))

def first_n_disarium(n):
    disarium_numbers = []
    num = 1
    while len(disarium_numbers) < n:
        if is_disarium(num):
            disarium_numbers.append(num)
        num += 1
    return disarium_numbers

def disarium_in_range(start, end):
    return [num for num in range(start, end + 1) if is_disarium(num)]
print(first_n_disarium(5))  
print(disarium_in_range(1, 1000))  
