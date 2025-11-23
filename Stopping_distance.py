V = float(input("Enter the Vehicle Speed (mph) :"))
F = float(input("Enter the coefficient of friction : "))
G = float(input("Enter the grade of the road, from 0 to 0.5 : "))
Tr = float(input("Enter the reaction time of the driver(sec) : "))
Slope = input("Enter '+' if its uphill or '-' if its downhill : ")
S = 0

if V > 0 and V < 200 and F > 0 and F < 1 and G > 0 and G < 0.5 and Tr > 0:
    if Slope == '+':
        S = (V ** 2 / (29.84 * (F + G))) + (1.4678 * V * Tr)
    if Slope == '-':
        S = (V ** 2 / (29.84 * (F - G))) + (1.4678 * V * Tr)
else:
    print("Invalid inputs")

print(f"The stopping distance of the vehicle should be {S:.2f}ft")




