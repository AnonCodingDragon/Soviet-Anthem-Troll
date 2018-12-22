import webbrowser
import time

def Meme():
	if(anstoboot == "Yes" or anstoboot == " Yes" or anstoboot == "yes" or anstoboot == " yes"):
		time.sleep(1)
		print("CYKA BLYAT")
		time.sleep(0.5)
		t_end = time.time() + 2.5
		while time.time() < t_end:
		#the two previous lines are a loop system and 3 is the amount of seconds the loop will last
			webbrowser.open("https://www.youtube.com/watch?v=U06jlgpMtQs", new=2, autoraise=True)
	else:
		print("Open the executable again and type in Yes when asked")
		time.sleep(3)
		exit()
		
print("Initializing program:")
time.sleep(0.5)
print("10%")
time.sleep(0.8)
print("15%")
time.sleep(0.7)
print("20%")
time.sleep(0.5)
print("30%")
time.sleep(0.3)
print("35%")
time.sleep(0.5)
print("40%")
time.sleep(1)
print("50%")
time.sleep(0.5)
print("60%")
time.sleep(1)
print("65%")
time.sleep(0.7)
print("70%")
time.sleep(0.4)
print("80%")
time.sleep(2)
print("85%")
time.sleep(0.5)
print("90%")
time.sleep(1)
print("95%")
time.sleep(0.7)
print("100%")
time.sleep(0.5)
print("Done!")
#Text that appears when code is ran

anstoboot = input("Type Yes and press enter to start the game")

Meme()
