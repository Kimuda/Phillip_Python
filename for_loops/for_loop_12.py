#counter1=1 ---useless and never used, so why put it there?

i=0

for i in range(1,101): #range(counter1,101) not necessary
    #counter1=counter1+10 ---yes it's in the loop but does nothing
    print(i, end=" ")
    if i%10==0:
        print()
