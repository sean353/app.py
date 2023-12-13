from icecream import ic


for i in range(1,100):
    if i%15==0 :
         ic("fizzbuzz")
    elif i%5==0 :
        ic("buzz")
    elif i%3==0 : 
        ic("fizz")
    else: ic(i)