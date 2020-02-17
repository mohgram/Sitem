import random
officialnumbers = [565788, 170606]
def alreadyhaveit():
 print("Please input your flight number.")
 flightnumber = int(input())
 if flightnumber in officialnumbers:
  print("Your flight number has been accepted!")
  seatreserve()
 else:
  print("Sorry, your flight number has been declined.")
  alreadyhaveit()	  
def seatreserve():  
  seatstaken = [1, 5, 7, 8]
  print("Please input the seat number you would like.")
  seatnumber = int(input())
  if seatnumber not in seatstaken:
   seatstaken.append(seatnumber)
   print("That seat has now been reserved!")
  else:
   print("Sorry, but that seat's been taken.")
   seatreserve()
def buyaflight():
 print("Please input the destination you would like to go to.")
 dest = str(input())
 flightnum = random.randint(100000, 400000)
 officialnumbers.append(flightnum)
 flight = str(flightnum)
 print("Your flight number is: " + flight + " and your destination is: " + dest)
 alreadyhaveit()
print("Welcome to Sitem Airways. Would you like to buy a flight, or do you already have one?")
print("Press 1 if you already have one, Press 2 if you would like to buy one.")
choice = int(input())
if choice == 1:
 alreadyhaveit()
elif choice == 2:
 buyaflight()  
