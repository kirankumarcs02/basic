def Sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    return prime


n = int(input())
l = [1,2,3,4,5,6,7,8,9]
p = Sieve(max(l))
q = []
s = []
for i in l:
    if p[i]:
        q.append(i)
    else:
        s.append(i)
s = s[::-1]
f = [q, s]
for i_out_ in f:
    print(' '.join(map(str, i_out_)))