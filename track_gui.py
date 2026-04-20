import Track_Simulator
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from tkinter import ttk

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

#Textbox (Commented out)
# display = ctk.CTkTextbox(u_app, width=400, height=200)
# display.pack()

table_frame = ctk.CTkFrame(u_app)
table_frame.pack(pady=10)

tree = ttk.Treeview(table_frame, columns=("Name", "Type", "Value"), show="headings")

tree.heading("Name", text="Name")
tree.heading("Type", text="Type")
tree.heading("Value", text="Value")

tree.column("Name", anchor="center", width=80)
tree.column("Type", anchor="center", width=100)
tree.column("Value", anchor="center", width=150)

tree.pack()


def update_display():
    # clear table
    for row in tree.get_children():
        tree.delete(row)

    # refill table
    for segment in track:
        if segment["type"] == "straight":
            value = f'Length: {segment["length"]}'
        else:
            value = f'R={segment["radius"]}, A={segment["angle"]}'

        tree.insert("", "end", values=(
            segment["name"],
            segment["type"],
            value
        ))

#Function to display the total time logic
def compute_time():
    total_time = Track_Simulator.compute_track_time(track)
    result_label.configure(text=f"Total Time: {total_time:.2f}")

result_label = ctk.CTkLabel(u_app, text="Total Time:")
result_label.pack()

compute_button = ctk.CTkButton(u_app, text="Compute Time", command=compute_time)
compute_button.pack()

u_app.mainloop()