def song(n):
	havebottle = True
	bottle = "bottles"
	while havebottle == True:
		print(str(n) + " " + str(bottle) + " bottles of beer on the wall, " + str(n) + " bottles of beer.")
		n -= 1
		if n == 1:
			bottle = "bottle"
		if n > 0:
			print("Take one down and pass it around, " + str(n) + " " + bottle +" of beer on the wall")
		else:
			print("Take one down and pass it around, no more bottles of beer on the wall")
			print("No more bottles of beer on the wall, no more bottles of beer.")
			print("Go to the store and buy some more, 99 bottles of beer on the wall.")
			havebottle = False

n = 99
song(n)
