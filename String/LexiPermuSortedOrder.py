ans = []


def permute(a, l, r):
    if l == r:
        ans.append(''.join(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]


string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n)
for i in sorted(ans):
    print(i)