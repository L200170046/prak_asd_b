#NO. 3b
print("\nNo.3b")
def jumlahKonsonan(a):
    v="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    konsonan=0
    jumlahhuruf=0
    for x in a:
        jumlahhuruf+=1
        if x in v:
            konsonan+=1
    return (jumlahhuruf,konsonan)

