print("welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()  
    
print("Okay! Let's play :)")


answer = input("wha does cpu stand for? ")
if answer.lower == "central processing unit":
    print("Correct!")   
else: 
    print("Incorrect!")
    
answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")   
else: 
    print("Incorrect!")
    
answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")   
else: 
    print("Incorrect!")
    
answer = input("what does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")   
else: 
    print("Incorrect!")