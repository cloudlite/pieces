__author__ = 'leon'
import Prime

if __name__ == '__main__':
    from timeit import Timer
    timeit_Prime = Timer("Prime.getPrimes(1000000)","from __main__ import Prime")
    print timeit_Prime.timeit(1)
    timeit_PrimeCount = Timer("Prime.getPrimesCount(1000000)","from __main__ import Prime")
    print timeit_PrimeCount.timeit(1)
