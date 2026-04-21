# Track Simulator

This is a Python based GUI-based application that simulates a custom track. Users can create their own custom track and simulate it using specifications (straights and corners). Users can add custom segments to simulate their own version of a track. From physics, this simulator utilizes the kinematic equations to simulate the time it would take for a car to complete a lap using factors like acceleration, velocity, distance, and friction. For this project, the aim is to replicate what it would be like to be constrained to time how a car moves through a track similar to F1 and NASCAR. The simulated car simulates a projected time based on constraints such as speed entering a corner and the optimal time to complete every segment of the track. This project is intended to be realistic in the fact that simulated cars should not "fly" off a corner and be disqualified from the track.

## Features
- Add straight and corners
- GUI built with CustomTkinter
- Track list visualization
- More will be added

## Project Structure

- `track_gui.py` – main GUI application
- `Segment_Builder` - Segment builder class 
- `Track_Simulator.py` – simulation logic

## Project Application
Let's explore a use case for this track simulator using a real-world example: The Indianapolis Motor Speedway!
- https://www.nascar.com/news-media/2021/08/11/indianapolis-motor-speedway-road-course-turn-by-turn-analysis/
This project is applicable in the Indy 500 due to the nature of the course such as the straights, corners, and velocity constraints.

## Project Example
- For the nature of this example, the angles and lengths will be arbitrary; however, the course structure will reimain the same.
- Arbitrary photo: https://drive.google.com/file/d/1thPG71kdrF2gO1evKwUfBH9owAU_fnxz/view?usp=sharing
- Solved problem: https://drive.google.com/file/d/1BSmM9B99ElsxpTGHxp2nSIR5CW7LwkVC/view?usp=drive_link


## Note
- For the purposes of this program and simplicity, this simulates minimal to no user error. This project assumes that the car will complete the track undergoing max acceleration from the car.
- This project uses 0.7 as the coefficient of friction, 9.81 for the coefficient of gravity, 14 as the max acceleration
- For the angles of the track, the simulator assumes that a left/right turn will consist of a 90 degree angle, if the car flips it will be 180 degrees, and if the car spins it will be a 360 degree change
- With that being said, the only angles available are 90, 180, and 260 to reduce ambiguity of this program (may be edited in the future)