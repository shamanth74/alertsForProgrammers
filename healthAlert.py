from pygame import mixer as m
import time


name=input("Enter your name >> ")
# f=open(f"{name}.txt","a")
local_time = time.ctime()
print(f"Your session start at {local_time}")


m.init()
def water():
    m.music.load("water.wav")
    m.music.set_volume(100)
    time.sleep(1800)
    m.music.play()
def eyes():
    m.music.load("eyes.wav")
    m.music.set_volume(1800)
    time.sleep(5)
    m.music.play()
def exercise():
    m.music.load("exercise.wav")
    m.music.set_volume(2400)
    time.sleep(5)
    m.music.play()


#user=name  
def task(user,task,cond):
    print(f"{task} (y/n) or skip(s)  >>")
    userInput = input()

    if userInput=="y":
        cond+=1
        f=open(f"{user}.txt","a")
        m.music.stop()
        local_time1 = time.ctime()
        f.write(f"{local_time1} :{cond}.  {task}  \n")
        f.close()
        print("Sucess..Now you can continue your work")
    elif userInput=="n":
        print(f"Session end at {local_time}")
        exit(0)
    elif userInput=="s":
        print("Skipped...Now you can continue your work..")
        return
    else:
        print("Invalid choice")
        print(f"Session end at {local_time}")
        exit(0)
        

i=0

while True:
    i+=1

    eyes()
    task(name,"Eyes rested",i)
        
    exercise()
    task(name,"Physical activity done",i)

    water()
    task(name,"Drank water",i)
    
    





