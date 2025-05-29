words=[ ]
#read from a file
with open("all_words.txt",'r') as f:
    for line in f:
        word=line.strip()
        if len(word)>=4:
            words.append(word)

#write to a file

with open("words_reqd_hangman.txt",'w') as f2:
    for word in words:
        f2.write(word+'\n')
    print("File saved, closed")
