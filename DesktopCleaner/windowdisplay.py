import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import main


# Function to create the GUI for the desktop cleaner
def clean_desktop_gui():
    # Function to select the source directory
    def select_source():
        # Open a directory selection dialog and store the selected path
        source_path = filedialog.askdirectory()
        # Update the source entry field with the selected directory path
        source_entry.delete(0, tk.END)
        source_entry.insert(0, source_path)

    # Function to select the destination directory
    def select_destination():
        # Open a directory selection dialog and store the selected path
        dest_path = filedialog.askdirectory()
        # Update the destination entry field with the selected directory path
        dest_entry.delete(0, tk.END)
        dest_entry.insert(0, dest_path)

    # Function to start the file cleaning process
    def start_cleaning():
        # Get the source and destination folder paths from the entry fields
        source_folder = source_entry.get()
        dest_folder = dest_entry.get()
        # Check if both source and destination are selected
        if not source_folder or not dest_folder:
            # If either is missing, show an error message
            tk.messagebox.showerror("Error", "Please select both source and destination folders.")
            return
        # Call the clean_desktop function from the main module with the selected paths
        main.clean_desktop(source_folder, dest_folder)

    # Create the main window for the GUI
    window = tk.Tk()
    window.title("Desktop Cleaner")  # Set the window title

    window.geometry("600x400")  # Set the window size

    # Create a label and entry for the source folder input
    source_label = tk.Label(window, text="Source Folder:")
    source_label.pack()
    source_entry = tk.Entry(window)
    source_entry.pack()
    source_button = tk.Button(window, text="Select Source", command=select_source)
    source_button.pack()

    # Create a label and entry for the destination folder input
    dest_label = tk.Label(window, text="Destination Folder:")
    dest_label.pack()
    dest_entry = tk.Entry(window)
    dest_entry.pack()
    dest_button = tk.Button(window, text="Select Destination", command=select_destination)
    dest_button.pack()

    # Create a start button to initiate the file cleaning process
    start_button = tk.Button(window, text="Start Cleaning", command=start_cleaning)
    start_button.pack()

    # Start the Tkinter event loop to display the GUI
    window.mainloop()
