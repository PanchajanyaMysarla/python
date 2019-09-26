spam2 = ['apples', 'bananas', 'tofu', 'cats']
spam = ['apples', 'bananas']


except_last = ', '.join(spam[:-1])

print(except_last + f', and {spam[-1]} ')
