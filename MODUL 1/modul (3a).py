#NO. 3a
print("\nNo.3a")
def jumlahVokal(a):
    v="aiueoAIUEO"
    vokal=0
    jumlahhuruf=0
    for i in a:
        jumlahhuruf+=1
        if i in v:
            vokal+=1
    return (jumlahhuruf,vokal)
