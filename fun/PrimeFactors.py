__author__ = 'leon'

def primefactors(n):
    '''Get all prime factors of input value n.'''
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


print primefactors(999)

