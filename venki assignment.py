import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to find repeated items
def find_repeated():
    try:
        # Retrieve input tuple from the user
        user_input = entry.get()
        user_tuple = tuple(map(str.strip, user_input.split(',')))
        
        # Find repeated items
        repeated_items = {item for item in user_tuple if user_tuple.count(item) > 1}
        
        # Display result
        if repeated_items:
            result = f"Repeated items: {', '.join(repeated_items)}"
        else:
            result = "No repeated items found."
        
        messagebox.showinfo("Result", result)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create main window
root = tk.Tk()
root.title("Find Repeated Items in Tuple")
root.geometry("400x200")

# Create and place widgets
label = tk.Label(root, text="Enter tuple items (comma-separated):", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

button = tk.Button(root, text="Find Repeated Items", command=find_repeated, font=("Arial", 12), bg="lightblue")
button.pack(pady=10)

# Run the application
root.mainloop()