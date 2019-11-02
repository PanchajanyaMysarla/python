arr = [1,2,3,3,5,3,7]

print(arr)

print(list(filter(lambda x: x!=3,arr)))
# y = 0
# for x in range(len(arr)):
#     if arr[x] != 3:
#         arr[y]=arr[x]
#         y+=1
#     
# print(arr)