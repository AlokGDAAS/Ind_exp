"""
A painter's most prized painting has been stolen, and the thief is making a run for it on the number line.
 The police have been alerted, and they immediately begin chasing the thief.

On the number line: The policeman starts at position X and moves at a speed of 2 units per second.
The thief starts at position Y and moves at a speed of 1 unit per second.

Your task is to determine the minimum time (in seconds) it will take for the policeman to catch the thief.
The policeman catches the thief when their positions become equal. The thief will try to evade for as long as possible,
but since the policeman is faster, they will eventually meet.

Can you help the police calculate how long it will take to catch the thief?
"""
def  main():
  X = int(input("Enter relative position of police man "))
  Y = int(input("Enter relative position of thief "))
  relativeSpeed = 2-1
  distance = Y-X
  time = distance/relativeSpeed
  print("Time to catch thief ",time)
  
main();


