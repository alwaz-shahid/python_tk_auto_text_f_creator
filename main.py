import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Text File Creator")


# Create a function to create the text file
def create_text_file():
    # Get the name of the file from the entry field
    file_name = file_name_entry.get()

    # Open the file in write mode
    with open(file_name + ".txt", "w") as f:
        # Write the text to the file
        f.write(text_entry.get("1.0", "end-1c"))


# Create a label for the file name field
file_name_label = tk.Label(text="Enter the name of the file:")
file_name_label.pack()

# Create an entry field for the file name
file_name_entry = tk.Entry()
file_name_entry.pack()

# Create a label for the text field
text_label = tk.Label(text="Enter the text to be written to the file:")
text_label.pack()

# Create a text field for the text
text_entry = tk.Text()
text_entry.pack()

# Create a button to create the text file
create_button = tk.Button(text="Create Text File", command=create_text_file)
create_button.pack()

# Run the main loop
window.mainloop()

#commnet