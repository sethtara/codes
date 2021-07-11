st = ['c', 'a', 't', 'd', 'o', 'g']
ls = len(st)
temp = ""
count = 0
for i in range(ls):
    for j in range(ls):
        if i == j:
            continue
        else:
            print(st[i] + st[j])
            for k in range(ls):
                if j == k or i == k:
                    continue
                else:
                    print(st[i] + st[j] + st[k])
                    for l in range(ls):
                        if k == l or i == l or j == l:
                            continue
                        else:
                            print(st[i] + st[j] + st[k] + st[l])
                            for m in range(ls):
                                if l == m or i == m or j == m or k == m:
                                    continue
                                else:
                                    print(st[i] + st[j] + st[k] + st[l] + st[m])
                                    for n in range(ls):
                                        if m == n or i == n or j == n or k == n or l == n:
                                            continue
                                        else:
                                            print(st[i] + st[j] + st[k] + st[l] + st[m] + st[n])

                                            count += 1

print(count)
