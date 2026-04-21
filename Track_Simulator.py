import math
import pandas as pd
import Segment_Builder as segments

# Givens
coefficient_of_friction = 0.7 #Adjust accordingly
coefficient_of_gravity = 9.81
max_acceleration = 14 #Adjust accordingly for the max acceleration of the car in question

#angle values
degree_90 = (math.pi) / 2 #turn 90 left/right
degree_180 = math.pi #u-turn
degree_360 = 2 * (math.pi) #full circle

#default values of test track
S1_length = 100
C1_radius = 22.5
C2_radius = 20
C3_radius = 20
S2_length = 60
C4_radius = 5.00
S3_length = 75.00
C5_radius = 5.00


#return max speed of track
def corner_max_speed(radius):
    max_speed = math.sqrt((coefficient_of_friction * coefficient_of_gravity * radius))
    return max_speed

#determines the arc length of a corner
def arc_length(radius, angle):
    arc_len = radius * angle
    return arc_len

#calculate constant velocity
def calculate_constant_speed(distance, speed):
    velocity = distance * speed
    return velocity

#calulate final_velocity
def final_velocity(v0, a, d):
    velocity = math.sqrt((v0**2) + (2 * a * d))
    return velocity

#calculate time of velocity
def time_of_velocity(v0, v, a):
    time = ((v - v0) / a)
    return time

#calculate the time and velocity coming out a corner
def solve_for_corner(radius, angle):
    arc_len = arc_length(radius, angle)
    v = corner_max_speed(radius)
    time = (arc_len / v)
    return time, v

#solve for a straight (acceleration and  braking)
def solve_straight(length, v_entry, v_exit_limit):
    #Case 1 (Assume for max acceleration through the entire straight)
    v_possible = final_velocity(v_entry, max_acceleration, length)
    t_possible = time_of_velocity(v_entry, v_possible, max_acceleration)
    if v_possible <= v_exit_limit:
        return t_possible, v_possible
    
    #Case 2 (Assume that the exit velocity may be greater than the size of straight)
    else:
        v_peak = math.sqrt(((2 * max_acceleration * length) + (v_entry**2) + (v_exit_limit**2)) / 2)
        #time accelerating
        t_acceleration = time_of_velocity(v_entry, v_peak, max_acceleration)
        #time braking
        t_braking = abs(time_of_velocity(v_peak, v_exit_limit, max_acceleration))
        total_time = t_acceleration + t_braking
        return total_time, v_exit_limit
        
#Will adjust the size and specifications of the track accordigly once solved
#Will change for the user so that they are able to customize and make their own straights and corners
def build_track():
    track = [
        {"type": "straight", "length": S1_length, "name": "S1"}, 
        {"type": "corner", "radius": C1_radius, "angle": degree_90, "name": "C1"},
        {"type": "corner", "radius": C2_radius, "angle": degree_90, "name": "C2"},
        {"type": "corner", "radius" : C3_radius, "angle" : degree_90, "name": "C3"},
        {"type": "straight", "length": S2_length, "name": "S2"},
        {"type": "corner", "radius": C4_radius, "angle": degree_90, "name": "C4"},
        {"type": "straight", "length": S3_length, "name": "S3"},
        {"type": "corner", "radius": C5_radius, "angle": degree_90, "name": "C5"}

    ]
    return track

# Computes the total time on the track accounting for the straight and corner
def compute_track_time(track):
    v_current = 0
    total_time = 0

    for i in range(len(track)):
        segment = track[i]
        next_segment = track[(i + 1) % len(track)]

        if next_segment["type"] == "corner":
            v_exit_limit = corner_max_speed(next_segment["radius"])
        else:
            # no constraint (no upcoming corner)
            v_exit_limit = float('inf')

        if segment["type"] == "corner":
            segment_time, segment_velocity = solve_for_corner(
                segment["radius"], segment["angle"]
            )
        else:
            segment_time, segment_velocity = solve_straight(
                segment["length"], v_current, v_exit_limit
            )

        total_time += segment_time
        v_current = segment_velocity

    return total_time
    
        
def create_segment_time_dict(track):
    v_current = 0
    all_segment_times = {}

    for i in range(len(track)):
        segment = track[i]
        next_segment = track[(i + 1) % len(track)]

        if next_segment["type"] == "corner":
            v_exit_limit = corner_max_speed(next_segment["radius"])
        else:
            # no constraint (no upcoming corner)
            v_exit_limit = float('inf')

        if segment["type"] == "corner":
            segment_time, segment_velocity = solve_for_corner(segment["radius"], segment["angle"])
            v_current = segment_velocity
            all_segment_times[segment["name"]] = segment_time
        else:
            v_exit_limit = corner_max_speed(next_segment["radius"])
            segment_time, segment_velocity = solve_straight(segment["length"], v_current, v_exit_limit)
            v_current = segment_velocity
            all_segment_times[segment["name"]] = segment_time
        
    # print(all_segment_times) # Debug code

    return all_segment_times
    
#User specifies their own type of track
def build_custom_track_for_user():
    flag = False
    user_track = []
    length = None
    radius = None
    name = None

    while flag == False:
        select = input("Do you want straight or corner? (S/C)")
        if select.lower() == "s":
            length = input("Type in your length: ")
            name = input("Type in the name (S1/C1): ")
            straight = segments.Straight(int(length), name)
            user_track.append(straight.to_dict())
        elif select.lower() == "c":
            radius = input("Type in your radius: ")
            string_angle = input("Type in your angle (90/180/360): ")
            name = input("Type in the name (S1/C1): ")
            picked_angle = pick_angle(string_angle)
            corner = segments.Corner(int(radius), picked_angle, name)
            user_track.append(corner.to_dict())
        
        choice = input("Are you done? (Y/N)")
        if (choice.lower() == "y"):
            flag = True
        else:
            flag = False
    
    return user_track


#Converts the angle into something the program can understand
def pick_angle(angle):
    selected_angle = None
    if angle == "90":
        selected_angle = degree_90
    elif angle == "180":
        selected_angle = degree_180
    else:
        selected_angle = degree_360
    return selected_angle
        

#Prints the results into a table in which the user can understand
def print_results(segment_times, total_time):
    labels = list(segment_times.keys()) + ["Total"]
    values = list(segment_times.values()) + [total_time]

    print("      | " + "  ".join(f"{l:>6}" for l in labels))
    print("-" * (8 + len(labels) * 8))
    print("Time  | " + "  ".join(f"{v:6.2f}" for v in values))

    


def main():
    """Main function of the script."""
    # Your main program logic goes here
    print("This code runs when the script is executed directly.")
    # test = []
    
    # Test 1: Build a specified track
    a = build_track()
    test = create_segment_time_dict(a)
    time = compute_track_time(a)
    print_results(test, time)

    # Test 2: Utilize the segment builder file
    # c1 = segments.Straight(100, name="S1")
    # c2 = segments.Corner(50, degree_90, name="C1")
    # test.append(c1.to_dict())
    # test.append(c2.to_dict())
    # aga = create_segment_time_dict(test)
    # time = compute_track_time(test)
    # print(test)
    # print_results(aga, time)

    
    #Test 3: Custom build a track based on what the user wants (Assuming they don't break the inputs)
    # a = build_custom_track_for_user()
    # print(a)
    # test = create_segment_time_dict(a)
    # time = compute_track_time(a)
    # print_results(test, time)


if __name__ == "__main__":
    main()