import time

while True:
    try:
        seconds = int(input("Enter the time in second"))
        if seconds < 1:
            print("Please enter number grater than 1 ")
            continue
        break
        pass
    except ValueError:
        print("Invalid input please enter whole number")
        
print("\n & Timer started... ")
for remaining in range(seconds, 0, -1):
    mins, secs =divmod(remaining, 60)
    time_format = f"{mins:02}:{secs:02}"
    print(f"* TIme left : {time_format}", end="\r")
    time.sleep(1)
    
print("\n Times up! Take a break or move on to next tsks")
print("\a") 