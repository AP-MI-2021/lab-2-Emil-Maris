'''
Găsește ultimul număr prim mai mic decât un număr dat.
'''

def v_prim(x):
    p = 0
    for i in range(2, int(x / 2) + 1):
        if x % i == 0:
            p = 1
            break
    return p


def get_largest_prime_below(m):
    while m != 0:
        if v_prim(m) == 0:
            print(m)
            break
        m = m - 1


n = int(input("n="))
get_largest_prime_below(n)


'''
Transformă un număr dat din baza 10 în baza 2. Numărul se dă în baza 10.
'''

def get_base_2(x):
    a = []
    b = 0
    while x != 0:
        p = x % 2
        a.append(p)
        x = int(x / 2)
    p = 1
    for i in range(len(a) - 1, -1, -1):
        b = b + a[i] * p
        p = p * 10
    return b


n = int(input())
print(get_base_2(n))


'''
Determină dacă un număr este antipalindrom.
'''

def is_antipalindrome(n):

    n = str(n)
    l = len(n) - 1
    i = 0
    ok = 1
    while i < l :
        if n[i]==n[l]:
            ok=0
        i=i+1
        l=l-1
    if ok==0:
        return False
    else: return True

option = '''
Daca vreti sa gasiti ultimul nr prim mai mic decat o valoare data, tastati "1".
Daca vreti sa transformati un numar din baza 10 in baza 2, tastati "2".
Daca vreti sa verificati daca un numar este antipalindrom, tastati "3".
Daca vreti sa inchideti programul, tastati "4".
'''

assert get_largest_prime_below(25) == 23
    assert get_largest_prime_below(2) == None
    assert get_largest_prime_below(30) == 29
    
assert get_base_2('10') == '1010'
    assert get_base_2('54') == '110110'
    assert get_base_2('16') == '10000'
    assert get_base_2('64') == '1000000'

def test_is_antipalindrome():
    assert is_antipalindrome(620) is True
    assert is_antipalindrome(2312) is False
    assert is_antipalindrome(232) is False
    assert is_antipalindrome(162) is True

def main():
    while True:
        optiune = input(option)
        if optiune == '1':
            nr = int(input("SCrieti numarul: "))
            print("Cel mai mare numar prim, mai mic decat {nr}, este: + str(get_largest_prime_below(nr)))
        elif optiune == '2':
            nr= int(input("Scrieti numarul pe care doriti sa-l convertiti din baza 10 in baza 2: "))
            print("Numarul {nr} convertit din baza 10 in baza 2 este: " + get_base_2(numar))
        elif optiune == '3':
            nr = int(input("Scrieti numarul care se va determina daca este antipalindrom: ")
            if is_antipalindrome(nr) == False:
                print(f"Numarul {nr} nu este antipalindrom.")
            else: print(f"Numarul {nr} este antipalindrom.")
         elif optiune == '4':
            print("Programul s-a oprit.")
            break
        else: print("Comanda gresita! Incercati din nou.")

if __name__ == '__main__':
  main()          