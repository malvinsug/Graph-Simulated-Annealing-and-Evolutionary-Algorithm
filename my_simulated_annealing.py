import random, math, copy, matplotlib.pyplot as plt

def generate_trip(cities):
    trip = random.sample(range(number_of_cities),number_of_cities)
    return trip

def generate_x_and_y(cities,trip):
    x_cord = [cities[trip[i%number_of_cities]][0] for i in range(number_of_cities+1)]
    y_cord = [cities[trip[j%number_of_cities]][1] for j in range(number_of_cities+1)]
    #print('x coordinates : {0}'.format(x_cord))
    #print('y coordinates : {0}'.format(y_cord))
    return [x_cord,y_cord]

def plot_trip(filename,x_cord,y_cord):
    plt.plot(x_cord,y_cord,'xb-') # xb- : blue x-marked line
    plt.savefig(filename)
    plt.close()

def calculate_distance(x,y):
    distance = 0
    i = 1
    for _ in range(len(x)-1):
        distance += ((x[i]-x[i-1])**2 + (y[i]-y[i-1])**2)**0.5
        i += 1
    return distance

number_of_cities = int(input("How many cities? "))
temperature = int(input("Give us the starting temperature : "))
cooling_rate = float(input("Give us the cooling rate : "))

counter = 2
#establish random cities
cities = []
for _ in range(number_of_cities):
	cities.append(random.sample(range(100),2))

#establish a random trip
trip = generate_trip(cities)
[x,y] = generate_x_and_y(cities,trip)

#show the trip
plot_trip("1_solution.png",x,y)

#calculate the distance
current_distance = calculate_distance(x,y)
print("\n1. solution has a trip, where :\n trip = {0}\n x : {1}\n y :{2} \n distance : {3}\n".format(trip,x,y,current_distance))


while temperature >1:
    [i,j] = sorted(random.sample(range(number_of_cities),2)) #randomly choose where to slice
    new_trip = trip[:i]+trip[j:j+1]+trip[i+1:j]+trip[i:i+1]+trip[j+1:] #switching the edges using slices
    [new_x,new_y] = generate_x_and_y(cities,new_trip)
    new_distance = calculate_distance(new_x,new_y)
    #1
    #2
    ratio = math.exp((new_distance-current_distance)/temperature)
    if (new_distance < current_distance) or (random.random()<=ratio):
        [trip,x,y,current_distance] = [new_trip,new_x,new_y,new_distance]
        #3
    temperature *= 1-cooling_rate
    counter += 1

plot_trip("last_solution.png",x,y)
print("\nMy final solution has a trip, where :\n trip = {0}\n x : {1}\n y :{2} \n distance : {3}\n".format(trip,x,y,current_distance))

#plot_trip("{0}_solution.png".format(counter),new_x, new_y)
#print("\n{0}. solution has a trip, where :\n trip = {1}\n x : {2}\n y :{3} \n distance : {4}\n".format(counter,new_trip,new_x,new_y,new_distance))
#plot_trip("{0}_solution.png".format(counter),x, y)
