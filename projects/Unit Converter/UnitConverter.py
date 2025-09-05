import tkinter as tk
from tkinter import ttk


# --- Conversion Logic ---
def convert():
    try:
        value = float(input_entry.get())
        from_unit = from_unit_combo.get()
        to_unit = to_unit_combo.get()
        category = category_var.get()

        result = 0
        if category == "Temperature":
            if from_unit == "Celsius":
                if to_unit == "Fahrenheit":
                    result = (value * 9 / 5) + 32
                elif to_unit == "Kelvin":
                    result = value + 273.15
                else:  # Celsius to Celsius
                    result = value
            elif from_unit == "Fahrenheit":
                if to_unit == "Celsius":
                    result = (value - 32) * 5 / 9
                elif to_unit == "Kelvin":
                    result = (value - 32) * 5 / 9 + 273.15
                else:  # Fahrenheit to Fahrenheit
                    result = value
            elif from_unit == "Kelvin":
                if to_unit == "Celsius":
                    result = value - 273.15
                elif to_unit == "Fahrenheit":
                    result = (value - 273.15) * 9 / 5 + 32
                else:  # Kelvin to Kelvin
                    result = value
        else:
            # For Length and Weight using conversion factors
            factors = unit_data[category]
            # Convert 'from_unit' to base unit (e.g., meters or grams), then to 'to_unit'
            base_value = value / factors[from_unit]
            result = base_value * factors[to_unit]

        result_label.config(text=f"Result: {result:.4f} {to_unit}")

    except (ValueError, KeyError):
        result_label.config(text="Invalid input or selection")


def update_units(*args):
    """Updates the unit comboboxes when the category changes."""
    units = unit_data[category_var.get()]
    from_unit_combo['values'] = list(units.keys())
    to_unit_combo['values'] = list(units.keys())
    from_unit_combo.set(list(units.keys())[0])
    to_unit_combo.set(list(units.keys())[1])


# --- Data ---
unit_data = {
    "Length": {"Meters": 1.0, "Kilometers": 1000.0, "Miles": 1609.34, "Feet": 0.3048},
    "Weight": {"Grams": 1.0, "Kilograms": 1000.0, "Pounds": 453.592, "Ounces": 28.3495},
    "Temperature": {"Celsius": None, "Fahrenheit": None, "Kelvin": None}  # Handled separately
}

# --- UI Setup ---
window = tk.Tk()
window.title("Unit Converter")

# Category Selection
category_var = tk.StringVar()
category_combo = ttk.Combobox(window, textvariable=category_var, values=list(unit_data.keys()))
category_combo.set("Length")
category_combo.pack(pady=10)
category_var.trace("w", update_units)  # Call update_units when category changes

# Frame for inputs
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

input_entry = tk.Entry(input_frame, width=15)
input_entry.pack(side=tk.LEFT, padx=5)

from_unit_combo = ttk.Combobox(input_frame, width=15)
from_unit_combo.pack(side=tk.LEFT, padx=5)

tk.Label(input_frame, text="to").pack(side=tk.LEFT)

to_unit_combo = ttk.Combobox(input_frame, width=15)
to_unit_combo.pack(side=tk.LEFT, padx=5)

# Convert Button
convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.pack(pady=10)

# Result Label
result_label = tk.Label(window, text="Result: ", font=("Helvetica", 12))
result_label.pack(pady=10)

# Initialize the unit dropdowns
update_units()

window.mainloop()