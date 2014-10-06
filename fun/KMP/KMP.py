__author__ = 'leon'

def KMPTableGen(pattern):
    assert len(pattern) > 2
    lenpattern = len(pattern)
    kmptable = [0 for i in xrange(lenpattern+1)]
    kmptable[0] = -1

    i = 0; j = 1
    while j < lenpattern:

        while pattern[j] != pattern[i]:
            j += 1
            if j >= lenpattern - 1:
                break
        while pattern[j] == pattern[i]:
            j += 1
            i += 1
            kmptable[j] = kmptable[j-1] + 1
            if j >= lenpattern - 1:
                break

        i = 0
        if pattern[i] == pattern[j]:
            kmptable[j + 1] = kmptable[j]
        else:
            kmptable[j + 1] = 0
        j += 1

    return kmptable[:-1]

print KMPTableGen('AABAACAABAA')
