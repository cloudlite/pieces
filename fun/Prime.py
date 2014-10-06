__author__ = 'leon'
import time

def getPrimes(number):
    res = []
    toSieve = [True for i in xrange(0, number + 1)]
    for i in xrange(2, len(toSieve)):
        if toSieve[i] == True:
            res.append(i)
            j = 2
            while i * j < len(toSieve):
                toSieve[i*j] = False
                j += 1
        elif toSieve[i] == False:
            continue
    # print res
    return res

def getPrimesCount(number):

    count = 0
    toSieve = [True for i in xrange(0, number + 1)]
    for i in xrange(2, len(toSieve)):
        if toSieve[i] == True:
            count += 1
            j = 2
            while i * j < len(toSieve):
                toSieve[i*j] = False
                j += 1
        elif toSieve[i] == False:
            continue
    print count
    return count


t0 = time.clock()
res = getPrimesCount(1000000)
print time.clock() - t0
#print 'Totally ', len(res), ' prime numbers'
#print res




