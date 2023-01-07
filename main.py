import tkinter as tk
from tkinter import filedialog

# Create the main window
window = tk.Tk()
window.title("Text File Creator")

# Create a function to create the text file
def create_text_file():
    # Open a file dialog to choose the save location
    file_path = filedialog.asksaveasfilename()

    # Open the file in write mode
    with open(file_path+ ".txt", "w") as f:
        # Write the text to the file
        f.write(text_entry.get("1.0", "end-1c"))

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
