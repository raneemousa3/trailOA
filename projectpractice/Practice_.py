def is_prime(number):
    prime=True 
    if number==1:
        prime=False
        return False
    else:
        for i in range(2,number):
            remainder=number%i
            if remainder==0:
                prime=False
                return prime
    return prime
if __name__ == '__main__':
    print(is_prime(89)) #true
    print(is_prime(9)) #false
