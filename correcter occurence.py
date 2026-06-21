# take input of a word 
string = input("please enter a word: ")
# take input of a charecter
char = input("please enter your own charecter: ")
i=0
count= 0
# loop will to find occurence of charecter
while(i < len(string)): # string operation
    if(string[i] == char): #condition 1
        count= count + 1
    i = i + 1
# display the result
print("the total number of times", char,"has occered =", count) 

