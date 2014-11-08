def is_prime(a) :
    for b in range(2,a):
        if a % b == 0 :
            return False
    return True
is_prime(4000)
