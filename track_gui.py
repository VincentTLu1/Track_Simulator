import Track_Simulator
import customtkinter as ctk

#global track_list
track = []

#Current user window for tinkering with the GUI file
u_app = ctk.CTk()
u_app.geometry("600x400")

def add_track_straight():
    length = float(length_input.get())

    segment = {
        "type": "straight",
        "length": length,
        "name": f"S{len(track)+1}"
    }

    track.append(segment)
    update_display()
    print(track)

    print("Straight length: " + length)
    print("Straight added")

def add_track_corner():
    length = float(length_input.get())
    radius = float(radius_input.get())
    string_angle = angle_input.get()
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

    print("Corner length: " + length)
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

u_app.mainloop()