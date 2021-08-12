# Apple of my Eye

"""
Create a program that will take an eye color
as input and output the percentage of people
with that eye color in the room.
"""

color = input("My Eye Color: ")

data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]

colors = ["brown","blue","green","black"]

total = sum(data[0]) + sum(data[1])

for x in range(0,len(colors)):
   if color == colors[x]:
      avg = int((data[0][x]+data[1][x])/total*100)
      print(avg)

# print(int((data[eye_color]*100)/total))
