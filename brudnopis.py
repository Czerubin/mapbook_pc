import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Select City")
    root.geometry("300x150")

    label = tk.Label(root, text="Choose a city:")
    label.pack(pady=10)

    cities = ["Warsaw", "Krakow", "Gdansk", "Wroclaw", "Poznan"]

    selected_city = tk.StringVar()
    combobox = ttk.Combobox(root, textvariable=selected_city, values=cities, state="readonly")
    combobox.pack(pady=5)
    combobox.current(0)

    def submit():
        print(f"Selected city: {selected_city.get()}")

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
