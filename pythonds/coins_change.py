
memo = {}

def recMC(coinValueList,change):
    numCoins= 0;
    if change in coinValueList:
        return 1
    else:
        for c in coinValueList:
            if c <= change:
                
                numCoins = 1 + recMC(coinValueList,change-c)
                #print(numCoins)
                break
        return numCoins

print(recMC([25,10,5,1],63))



# def recMC2(coinValueList,change):
#    minCoins = change
#    if change in coinValueList:
#      return 1
#    else:
#       for i in [c for c in coinValueList if c <= change]:
#          numCoins = 1 + recMC2(coinValueList,change-i)
#          if numCoins < minCoins:
#             minCoins = numCoins
#    return minCoins
# 
# print(recMC2([1,5,10,25],63))