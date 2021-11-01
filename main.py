def invers(n):
    '''
    Returnează inversul unui nr.
    :param n: numărul citit
    :return: inversul nr. citit
    '''
    inversul = 0
    while n > 0:
        inversul = inversul * 10 + n % 10
        n = n // 10
    return inversul


def is_palindrome(n):
    '''
    Verifică dacă un nr citit de la tastatură este palindrom.
    :param n: numărul citit
    :return: true sau false
    '''
    if n == invers(n):
        return True
    else:
        return False


def isPrime(n):
    '''
    Verifică dacă un nr. este prim.
    :param n: nr citit
    :return: true sau false
    '''
    if n < 2:
        return False
    if n == 2:
        return True
    if n >= 2:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


def is_superprime(n):
    '''
    Verifică dacă un nr este superprim.
    :param n: nr citit
    :return: true sau false
    '''
    if n < 2:
        return False
    while n > 0:
        if n < 2:
            return False
        if isPrime(n) == False:
            return False
        n = n // 10
    return True


def get_largest_prime_below(n):
    '''
    Găsește cel mai mare nr. prim mai mic decât cel dat
    :param n: nr dat
    :return: ultimul numar prim mai mic decat n
    '''
    for i in range(n - 1, 1, -1):
        if isPrime(i):
            return i
    return 2


def test_is_palindrom():
    assert is_palindrome(626) == True
    assert is_palindrome(4424) == False
    assert is_palindrome(5) == True


def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(237) is False
    assert is_superprime(72) is False


def test_get_largest_prime_below():
    assert get_largest_prime_below(6) == 5
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(200) == 199


def main():
    while True:
        print("1. Determină dacă un număr dat este palindrom. ")
        print("2. Determină dacă un număr este superprim. ")
        print("3. Găsește ultimul număr prim mai mic decât un număr dat. ")
        print("x. Inchide programul.")
        optiune = input("Opțiunea: ")
        if optiune == "1":
            n = int(input("n = "))
            if is_palindrome(n):
                print("Numărul dat este palindrom.")
            else:
                print("Numărul dat NU este palindrom.")
        elif optiune == "2":
            n = int(input("n = "))
            print(is_superprime(n))
        elif optiune == "3":
            n = int(input("n = "))
            prime = get_largest_prime_below(n)
            print("Ultimul nr. prim mai mic decat {} este {}".format(n, prime))
        elif optiune == "x":
            return
        else:
            print("Opțiune invalidă! Reîncercați: ")


main()
