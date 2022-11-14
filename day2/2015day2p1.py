hs = 0
vs = 0

for d in :
    k,v = d.split()

    if k =="forward":
        hs+=int(v)
    elif k == "down":
        vs+=int(v)
    elif k=="up":
        vs-=int(v)

print(hs*vs)