from hashlib import md5

init = 'ckczppom'

# ---------- PART ONE -----------------

for i in range(1000000):
    h = md5((init + str(i)).encode()).hexdigest()
    if h[:5] == '00000':
        print(h)
        print(i)
        break

# ---------- PART TWO -----------------
    
for i in range(100000000):
    h = md5((init + str(i)).encode()).hexdigest()
    if h[:6] == '000000': # Just add another zero
        print(h)
        print(i)
        break