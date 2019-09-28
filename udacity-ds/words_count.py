message = """Nory was a Catholic because her mother was a Catholic, and Nory’s 
mother was a Catholic because her father was a Catholic, 
and her father was a Catholic because his mother was a Catholic, or had been."""

words = message.split()

words_count = {}

for word in words:
    words_count.setdefault(word,0)
    words_count[word] +=1
    
print(words_count)