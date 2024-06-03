fc=0
flo=0
fle=0
fn=0
psw=input("δωσε κωδικό")

for i in range(0,len(psw)):
    if psw[i].isupper():
        fc=1

for i in range(0,len(psw)):
    if psw[i].islower():
        flo=1

for i in range(0,len(psw)):
    if psw[i].isdecimal():
        fn=1

if len(psw)>=8:
    fle=1

if fc==1 and flo==1 and fn==1 and fle==1:
    print("Σωστός κωδικός")
else:
    print("Λάθος κωδικός")
