text=input("Enter a string:")

words=text.split()
count={}

for word in words:
     count[word]=count.get(word,0)+1

print("Word Occurrences:")
print(count)
