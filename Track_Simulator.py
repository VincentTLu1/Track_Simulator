import math

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
        {"type": "straight", "length": S1_length}, 
        {"type": "corner", "radius": C1_radius, "angle": degree_90},
        {"type": "corner", "radius": C2_radius, "angle": degree_90},
        {"type": "corner", "radius" : C3_radius, "angle" : degree_90},
        {"type": "straight", "length": S2_length},
        {"type": "corner", "radius": C4_radius, "angle": degree_90},
        {"type": "straight", "length": S3_length},
        {"type": "corner", "radius": C5_radius, "angle": degree_90}

    ]
    return track

def compute_track_time(track):
    v_current = 0
    total_time = 0
    all_segment_times = []
    all_corner_times = [] #Debug
    all_straight_times = [] #Debug
    all_segment_velocity = []

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
            total_time += segment_time
            v_current = segment_velocity
            all_corner_times.append(segment_time)
            all_segment_times.append(segment_time)
            all_segment_velocity.append(segment_velocity)
        else:
            v_exit_limit = corner_max_speed(next_segment["radius"])
            segment_time, segment_velocity = solve_straight(segment["length"], v_current, v_exit_limit)
            total_time += segment_time
            v_current = segment_velocity
            all_straight_times.append(segment_time)
            all_segment_times.append(segment_time)
            all_segment_velocity.append(segment_velocity)

        print("Hello World")
        return total_time
    
    
    print(f"{total_time:.4f}")
    print(all_corner_times)
    print(all_straight_times)
    # print(all_segment_times)
    # print(all_segment_velocity)

#This is a test for the repo
def main():
    """Main function of the script."""
    # Your main program logic goes here
    print("This code runs when the script is executed directly.")
    a = build_track()
    compute_track_time(a)



if __name__ == "__main__":
    main()