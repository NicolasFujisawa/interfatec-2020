tcs = []
ds = []
tme = []
tmt = []

n = int(input())
if(n >= 1 and n <= 100):
    for i in range(0, n):
        [tc, d] = [int(value) for value in input().split(" ")]
        if(i > 0):
            tme.append(sum(ds) - tc)
            tmt.append(sum(ds) + d - tc)
        else:
            tme.append(tc)
            tmt.append(d - tc)
        tcs.append(tc)
        ds.append(d)

tmeFinal = round(sum(tme)/n, 1)
tmtFinal = round(sum(tmt)/n, 1)
print("TME:{tme}".format(tme=tmeFinal))
print("TMT:{tmt}".format(tmt=tmtFinal))
