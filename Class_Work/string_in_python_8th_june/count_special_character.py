#WAP to input a sentence from user and count the number special characters present in sentence
sentence = input("enter a sentence :")
count = 0
for ch in sentence:
    if ch.isalnum()==False:
        count+1
        print("no. of special character",count)