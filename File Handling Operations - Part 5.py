with open('Codingal.txt','w') as file:
    file.write("follow my insta page")
file.close()
# split file into words
with open('Codingal.txt','r') as file:
    data=file.readlines()
    print("words in this file are ........")
    for line in data:
        word=line.split()
        print(word)
file.close()