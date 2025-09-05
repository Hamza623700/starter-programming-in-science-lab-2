# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
def calculate_height(h0, t):
    # TODO: Implement this function
    h0 = int(input("enter your height in m:"))
    t = int(input("entere your time in seconds:"))
    g = 9.81 
    height = h0 + 1/2*g*t**2
    print("the height of the ball", height,"m")

    number = 54.905 
    rounded_number = round(number,1)
    print(rounded_number)

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    time = int(input("enter your time in seconds:"))
    speed = int(input("enter your speed" "m/s" ))
    distance = time*speed
    print("the distance of the car", distance,"m")



