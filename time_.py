# SET COUNTDN TIMER 

import time 

while True:
      try:
            seconds = int(input("🕰️ enter time in seconds: "))
            if seconds < 1:
                  print(" enter number greater than 0")
                  continue
            break
      except ValueError:
            print(" Invalid input, please enter whole number ")

print("\n 🔔 Timer started..")
for remaining in range(seconds, 0, -1):
      mins, secs = divmod(remaining,60)
      time_format = f"{mins:02}:{secs:02}"
      print(f"🕰️ time left: {time_format} ",end="\r")
      time.sleep(1)

print("\n Time up! ")
