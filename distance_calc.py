import math

def calculate_distance(a, b):
    if len(a) == 4 and len(b) == 4:
        xa = a[0] + round((a[2]-a[0])/2)
        ya = a[1] + round((a[-1]-a[1])/2)

        xb = b[0] + round((b[2]-b[0])/2)
        yb = b[1] + round((b[-1]-b[1])/2)

        distance = math.sqrt(math.pow((xb-xa),2) + math.pow((yb-ya),2))

        return distance
    else:
        print("Error: Invalid coordinates provided to calculate_distance.")
        return float('inf')  # Return a large distance value for invalid coordinates

def find_closest_parking(parking_list, entrance):
    if not parking_list:
        print("Error: Parking list is empty.")
        return None

    distance_list = []

    for i in range(len(parking_list)):
        distance = calculate_distance(a=parking_list[i], b=entrance)
        distance_list.append(distance)

    min_distance = min(distance_list)

    if min_distance == float('inf'):
        print("Error: Cannot find closest parking. Invalid distances.")
        return None

    min_index = distance_list.index(min_distance)

    closest_parking = parking_list[min_index]

    return closest_parking
