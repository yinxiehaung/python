string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 


def findkeylen(c):
    '''limit key len <= 13'''

    i, k, count = 1,0,0
    maxcount = 0
    ret = 0
    while i <= 13:
        while k + i < len(c):
            if(c[k + i] == c[k]):
                count += 1
            k += 1  
        if count > maxcount:
            maxcount = count
            ret = i
        count = 0
        i += 1
        k = 0
    return ret

def findkey(c, kl = findkeylen(c)):
    W = {'A':0.082,'B':0.015,'C':0.028,'D':0.043,'E':0.127,'F':0.022,
         'G':0.020,'H':0.061,'I':0.070,'J':0.001,'K':0.008,'L':0.040,
         'M':0.024,'N':0.067,'O':0.075,'P':0.019,'Q':0.001,'R':0.060,
         'S':0.063,'T':0.091,'U':0.028,'V':0.010,'W':0.023,'X':0.001,
         'Y':0.020,'Z':0.001}
    n = len(c)
    key = []

    for j in range(kl):
        P = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,
             'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,
             'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,
             'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,
             'Y':0,'Z':0}
        for i in range(j, n, kl):
            P[c[i].upper()] += 1
        for i in string:
            P[i] = P[i]/ (n/kl)
        
        list1 = []
        for i in range(0,26):
            count = 0
            for j in string:
                count +=  P[j] * W[string[(ord(j) - ord('A') - i) % 26]]
            list1.append(abs(count - 0.066))
          
        print(string[list1.index(min(list1))],end ='')
