#Marc Gonzalez
#12/02/14
#1.1

with open("input.txt",mode ="w", encoding = "utf-8") as text:
    for line in range(5):
        write = input("please enter a line of text: ")
        text.write(write+"\n")
        
