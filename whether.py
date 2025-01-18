wether=(1,0,0,0,1,0,0)
summer=0
rainy=0
for i in range(0):
    if  wether [i]==0:
        rainy+=1
    else:
        summer+=1
if summer<rainy:
    print("its a bad wether")
else:
    print("its a good wether")            

