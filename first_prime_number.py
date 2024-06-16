n = int(input())
factor = 0
for i in range(1,(n+1)):
    integers = int(input())
    is_prime = True
    if integers > 1 :
        for j in range(2,integers):
            if (integers%j) == 0:
                is_prime = False
                break
        if is_prime:
            print(integers)
            break