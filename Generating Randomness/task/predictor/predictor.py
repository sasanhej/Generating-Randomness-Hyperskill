import random
s=""
t=""
cg=0
ng=0
tt=""
sdict={}
pdict={}
res=""
bl=1000
print("Please provide AI some data to learn...\nThe current data length is 0, 100 symbols left")
while len(s)<100:
    userin=""
    userin=input("Print a random string containing 0 or 1:\n")
    for i in userin:
        if (i=="0" or i=="1"):
            s+=i
    print("Current data length is {}, {} symbols left".format(len(s),100-len(s)))
print("Final data string:{}\n".format(s))
for j in range(len(s)-3):
    seq=s[j:j+4]
    sdict.update({seq: (int(sdict.get(seq)) if (seq) in sdict else 0) +1 })
for k in range(8):
    triad=bin(k)[2:].zfill(3)
    c0=sdict.get(triad+"0") if (triad+"0") in sdict else 0
    c1=sdict.get(triad+"1") if (triad+"1") in sdict else 0
    p0=c0/(c0+c1)
    p1=c1/(c0+c1)
    pdict.update({triad: ("0" if p0>p1 else ("1" if p1>p0 else random.choice(["0","1"])))})
print("You have $1000. Every time the system successfully predicts your next press, you lose $1.\nOtherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")
while t!="enough":
    t = input("Print a random string containing 0 or 1:")
    cg=0
    ng=0
    if (len(t)>=4 and t.count("0")+t.count("1")==len(t)):
        for j in range(len(t)-3):
            tseq = t[j:j + 3]
            pred=pdict.get(tseq)
            tt+=pred

            if t[j+3]==pred:
                cg+=1
            else:
                ng+=1
        bl=bl-cg+ng
        print("predictions:\n{}\n".format(tt))
        print("Computer guessed {} out of {} symbols right ({}%)".format(cg, cg+ng, cg / (cg + ng) * 100))
        print("Your balance is now ${}\n".format(bl))
print("Game over!")