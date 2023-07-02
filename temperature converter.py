import tkinter as tk

def convert_temperature():
    temperature = float(entry.get())
    unit = unit_var.get()

    if unit == "Celsius":
        converted_temp = (temperature * 9/5) + 32
        result_label.config(text=f"{converted_temp:.2f}°F")
    elif unit == "Fahrenheit":
        converted_temp = (temperature - 32) * 5/9
        result_label.config(text=f"{converted_temp:.2f}°C")

root = tk.Tk()
root.title("Temperature Converter")

frame = tk.Frame(root)
frame.pack(pady=20)

entry = tk.Entry(frame, font=("Helvetica", 14))
entry.pack(pady=10)

unit_var = tk.StringVar(value="Celsius")
unit_label = tk.Label(frame, text="Unit:", font=("Helvetica", 12))
unit_label.pack()
unit_menu = tk.OptionMenu(frame, unit_var, "Celsius", "Fahrenheit")
unit_menu.pack()

convert_button = tk.Button(frame, text="Convert", command=convert_temperature)
convert_button.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 18))
result_label.pack(pady=20)

root.mainloop()
