def candies(ratings):
    length=len(ratings)
    candies=[1]*length

    for i in range(1,length):
        if ratings[i]>ratings[i-1]:
            candies[i]=candies[i-1]+1

    for i in range(length-2,-1,-1):
        if ratings[i]>ratings[i+1]:
            candies[i]=max(candies[i],candies[i+1]+1)
    print(candies)
    return sum(candies)

print(candies([0,2,1]))