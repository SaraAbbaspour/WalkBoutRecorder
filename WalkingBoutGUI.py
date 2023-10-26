import tkinter as tk
from datetime import datetime
import csv

start_time = None  # Initialize start time

def start_task():
    global start_time
    start_time = datetime.now()
    timestamp_label.config(text=f"Task Started at: {start_time}")
    start_button.config(state=tk.DISABLED)  # Disable the start button

def stop_task():
    if start_time is not None:
        stop_time = datetime.now()
        elapsed_time = stop_time - start_time
        comment1 = comment_entry1.get()
        comment2 = comment_entry2.get()
        filename = filename_entry.get()  # Get the filename from the entry field
        timestamp_label.config(text=f"Task Stopped at: {stop_time}\nElapsed Time: {elapsed_time}\nComment 1: {comment1}\nComment 2: {comment2}")
        
        # Define the column names
        field_names = ["Start Time", "Stop Time", "Elapsed Time", "Number of Steps", "Comment"]
        
        # Save the start and stop times, comments, and elapsed time to the specified CSV file
        with open(filename, "a", newline='') as file:
            csv_writer = csv.writer(file)
            
            # Write the header row if the file is empty
            if file.tell() == 0:
                csv_writer.writerow(field_names)
                
            csv_writer.writerow([start_time.strftime("%Y-%m-%d %H:%M:%S"), stop_time.strftime("%Y-%m-%d %H:%M:%S"), elapsed_time, comment1, comment2])
        
        start_button.config(state=tk.NORMAL)  # Enable the start button
        
        # Reset comment entry fields to empty strings
        comment_entry1.delete(0, tk.END)
        comment_entry2.delete(0, tk.END)
    else:
        timestamp_label.config(text="Start the task first!")

# Create the main window
root = tk.Tk()
root.title("Task Timer")

# Create an entry field for the filename at the top
filename_label = tk.Label(root, text="Enter Filename (e.g., output.csv):")
filename_label.pack()
filename_entry = tk.Entry(root)
filename_entry.pack()

# Create entry fields for comments
comment_label1 = tk.Label(root, text="Number of steps:")
comment_label1.pack()
comment_entry1 = tk.Entry(root)
comment_entry1.pack()

comment_label2 = tk.Label(root, text="Enter Comment:")
comment_label2.pack()
comment_entry2 = tk.Entry(root)
comment_entry2.pack()

# Create a label to display the timestamp, task time, and comments
timestamp_label = tk.Label(root, text="", font=("Helvetica", 16))
timestamp_label.pack(pady=20)

# Create start and stop buttons
start_button = tk.Button(root, text="Start Task", command=start_task)
start_button.pack()

stop_button = tk.Button(root, text="Stop Task", command=stop_task)
stop_button.pack()

# Start the GUI main loop
root.mainloop()
