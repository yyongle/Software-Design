import customtkinter as ctk
import tkinter as tk
from tkcalendar import DateEntry
from PIL import Image, ImageTk

# Initialize customtkinter settings
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

# Create the main application window
root = ctk.CTk()
root.title("Car Rental Interface")
root.geometry("1200x800")

# Load the background image
bg_image_path = "C:\\Users\\chewy\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-09-24 220901.png"
bg_image = Image.open(bg_image_path)
bg_image = bg_image.resize((1280, 720), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Set the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame for location entries
location1 = ctk.CTkFrame(root, corner_radius=0, fg_color="#bbbbbb")
location1.place(relx=0.269, rely=0.275, relwidth=0.09, relheight=0.025)
location2 = ctk.CTkFrame(root, corner_radius=0, fg_color="#bbbbbb")
location2.place(relx=0.634, rely=0.277, relwidth=0.09, relheight=0.025)

# Pickup & Drop-off location entry
pickup_entry = ctk.CTkEntry(location1, font=("Arial", 10), fg_color="#bbbbbb")
pickup_entry.grid(row=1, column=1, padx=10)
dropoff_entry = ctk.CTkEntry(location2, font=("Arial", 10), fg_color="#bbbbbb")
dropoff_entry.grid(row=1, column=5, padx=10)

# Frame for date entries
date1 = ctk.CTkFrame(root, corner_radius=0, fg_color="#bbbbbb")
date1.place(relx=0.445, rely=0.275, relwidth=0.09, relheight=0.025)
date2 = ctk.CTkFrame(root, corner_radius=0, fg_color="#bbbbbb")
date2.place(relx=0.81, rely=0.277, relwidth=0.09, relheight=0.025)

# Pickup & Drop-off date entry
pickup_date = DateEntry(date1, width=12, background='orange', foreground='white', borderwidth=2, font=("Arial", 10))
pickup_date.grid(row=1, column=3, padx=10)
dropoff_date = DateEntry(date2, width=12, background='orange', foreground='white', borderwidth=2, font=("Arial", 10))
dropoff_date.grid(row=1, column=7, padx=10)

# Create a frame for the filter options
filter_frame = ctk.CTkFrame(root, corner_radius=0, fg_color="white")
filter_frame.place(relx=0.075, rely=0.25, relwidth=0.1, relheight=0.5)

# Brand options
brand_label = ctk.CTkLabel(filter_frame, text="Brand", font=("Arial", 12))
brand_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)

brand_vars = []
brands = ["Toyota", "Mazda", "Perodua", "Mercedes"]
for i, brand in enumerate(brands):
    var = ctk.IntVar()
    chk = ctk.CTkCheckBox(filter_frame, text=brand, variable=var, font=("Arial", 10))
    chk.grid(row=i + 1, column=0, sticky='w', padx=10)
    brand_vars.append(var)

# Seating Capacity options
capacity_label = ctk.CTkLabel(filter_frame, text="Seating Capacity", font=("Arial", 12))
capacity_label.grid(row=5, column=0, sticky='w', padx=10, pady=5)

capacity_vars = []
capacities = ["2-seater", "4-seater", "6-seater"]
for i, capacity in enumerate(capacities):
    var = ctk.IntVar()
    chk = ctk.CTkCheckBox(filter_frame, text=capacity, variable=var, font=("Arial", 10))
    chk.grid(row=i + 6, column=0, sticky='w', padx=10)
    capacity_vars.append(var)

# Transmission Type options
transmission_label = ctk.CTkLabel(filter_frame, text="Transmission Type", font=("Arial", 12))
transmission_label.grid(row=9, column=0, sticky='w', padx=10, pady=5)

transmission_vars = []
transmissions = ["Manual", "Automatic"]
for i, transmission in enumerate(transmissions):
    var = ctk.IntVar()
    chk = ctk.CTkCheckBox(filter_frame, text=transmission, variable=var, font=("Arial", 10))
    chk.grid(row=i + 10, column=0, sticky='w', padx=10)
    transmission_vars.append(var)

# Start the main loop
root.mainloop()
