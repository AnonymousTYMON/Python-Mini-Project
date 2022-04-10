import stats
lst = [6, 6, 10, 12, 15, 9, 8, 17, 13, 14, 18]
Stats = stats.Stats
lst.sort()
print(lst)

print("Range\t", Stats.range(lst))
print("Min\t", Stats.min(lst))
print("Max\t", Stats.max(lst))
print("Average\t", Stats.average(lst))
print("Median\t", Stats.median(lst))
print("Mode\t", Stats.mode(lst))
print("Inter-quartile range\t", Stats.ir(lst))
print("Standard deviation\t", Stats.SD(lst))
for n in range (Stats.min(lst), Stats.max(lst)):
    if lst.count(n) != 0:
        print("Count", n,  lst.count(n))


