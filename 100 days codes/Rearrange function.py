def rearrange(s):
    breakup = s.split(" ")
    print(",".join(sorted(breakup)))

s = "Tom Dick Harry"
print(rearrange(s))