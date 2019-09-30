 
#cat_dog('catcat') → False
#cat_dog('1cat1cadodog') → True


def cat_dog(str):
    cats = 0
    dogs = 0
    
    for i in range(len(str)-2):
        print(i)
        if str[i:i+3] == 'cat':
            cats+=1
        elif str[i:i+3] == 'dog':
            dogs+=1
    print(cats,'cats',dogs,'dogs')   
        
        
#cat_dog('catdog')
#cat_dog('catcat')
cat_dog('1cat1cadodog')