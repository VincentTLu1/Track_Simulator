import Track_Simulator
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

#global track_list
track = []

#Current user window for tinkering with the GUI file
u_app = ctk.CTk()
u_app.geometry("600x400")

def add_track_straight():
    value = length_input.get()

    if value == "":
        CTkMessagebox(title="Warning", message="Please enter a length!", icon="info")
        length_input.focus()
        return
    
    length = float(value)

    length_input.delete(0, "end")

    segment = {
        "type": "straight",
        "length": length,
        "name": f"S{len(track)+1}"
    }

    track.append(segment)
    update_display()
    print(track)

    print("Straight length: " + str(length))
    print("Straight added")

def add_track_corner():
    length_value = length_input.get()
    # length = float(length_input.get())
    if length_value == "":
        CTkMessagebox(title="Warning", message="Please enter a length!", icon="info")
        length_input.focus()
        return
    
    length = float(length_value)

    length_input.delete(0, "end")


    # radius = float(radius_input.get())
    radius_value = radius_input.get()
    if radius_value == "":
        CTkMessagebox(title="Warning", message="Please enter a radius!", icon="info")
        radius_input.focus()
        return
    
    radius = float(radius_value)

    radius_input.delete(0, "end")
    string_angle = angle_input.get()
    angle_input.delete(0, "end")
    picked_angle = Track_Simulator.pick_angle(string_angle)
    

    segment = {
        "type": "corner",
        "radius": radius,
        "angle": picked_angle,
        "name": f"C{len(track)+1}"
    }

    track.append(segment)
    update_display()
    print(track)

    print("Corner length: " + str(length))
    print("Corner added")

straight_button = ctk.CTkButton(u_app, text="Add Straight", command=add_track_straight)
straight_button.pack()

corner_button = ctk.CTkButton(u_app, text="Add Corner", command=add_track_corner)
corner_button.pack()

length_input = ctk.CTkEntry(u_app, placeholder_text="Enter length here")
length_input.pack()

radius_input = ctk.CTkEntry(u_app, placeholder_text="Enter radius here")
radius_input.pack()

angle_input = ctk.CTkEntry(u_app, placeholder_text="Enter angle here")
angle_input.pack()

# angle_option = ctk.CTkOptionMenu(u_app, values=["90", "180", "360"])
# angle_option.pack()

display = ctk.CTkTextbox(u_app, width=400, height=200)
display.pack()

#Function for display logic
def update_display():
    display.delete("0.0", "end")

    for segment in track:
        if segment["type"] == "straight":
            text = f'{segment["name"]}: Straight {segment["length"]}\n'
        else:
            text = f'{segment["name"]}: Corner r={segment["radius"]}\n'

        display.insert("end", text)

#Function to display the total time logic
def compute_time():
    total_time = Track_Simulator.compute_track_time(track)
    result_label.configure(text=f"Total Time: {total_time:.2f}")

result_label = ctk.CTkLabel(u_app, text="Total Time:")
result_label.pack()

compute_button = ctk.CTkButton(u_app, text="Compute Time", command=compute_time)
compute_button.pack()

u_app.mainloop()