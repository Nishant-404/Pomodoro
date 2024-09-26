import time
import os

print("Hi User!\nCustomize your work session and breaks.")

hour = int(input("Enter total number of hours: "))
minn = int(input("Enter the total number of breaks (including long breaks): "))
sbd = int(input("Enter duration of short break (in minutes): "))
lbd = int(input("Enter duration of long break (in minutes): "))

input("Press Enter to start the timer!!\nRemember, there's NO GOING BACK...Enjoy!")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def short_break(minm):
    for i in range(minm-1, -1, -1):
        for c in range(59, -1, -1):
            print(f"Short Break: {i} min {c} sec")
            time.sleep(1)
            clear_screen()

def long_break(minm):
    for i in range(minm-1, -1, -1):
        for c in range(59, -1, -1):
            print(f"Long Break: {i} min {c} sec")
            time.sleep(1)
            clear_screen()

minutes = hour * 60  
break_interval = minutes // minn  #
long_break_count = minn // 4  
short_break_count = minn - long_break_count


for mi in range(minutes, 0, -1):
    for sec in range(59, 0, -1):
        print(f"Work Time: {mi // 60} hour(s) {mi % 60} min(s) {sec} sec")
        time.sleep(1)
        clear_screen()

    
    if mi % break_interval == 0 and mi != minutes:  
        if short_break_count > 0:
            short_break(sbd)
            short_break_count -= 1
        elif long_break_count > 0:
            long_break(lbd)
            long_break_count -= 1

print("Session Complete! Great job!")
