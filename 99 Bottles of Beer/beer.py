lyrics = ["bottles of beer on the wall,", "bottles of beer", "Take one down and pass it around,", "bottles of beer on the wall."]
singLyrics = ["bottle of beer on the wall,", "bottle of beer", "no more bottles of beer on the wall", "bottle of beer on the wall."]

bottles = 99
while (bottles > 1):
    print(bottles, lyrics[0], bottles, lyrics[1], "\n", lyrics[2], bottles, lyrics[3], "\n")
    bottles = bottles - 1
print(bottles, singLyrics[0], bottles, singLyrics[1], "\n", lyrics[2], bottles, singLyrics[3])
