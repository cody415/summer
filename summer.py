temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")

if temperature > 20:
    print("Wear jeans and a T-shirt")

if temperature > 10:
    print("I recommend a jumper as well")

if temperature > 5:
    print("Take a jacket with you")
 
if rain == "yes":
    print("Don't forget your umbrella!")