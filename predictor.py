import tkinter as tk
from tkinter import ttk, messagebox

def simulate_prediction(rainfall, temperature, population_density, sanitation_index):
    base_prob = 0.1
    prob_outbreak = (
        base_prob
        + (rainfall / 300) * 0.3
        + ((temperature - 15) / 20) * 0.2
        + (population_density / 1000) * 0.25
        + (1 - sanitation_index) * 0.35
    )
    prob_outbreak = max(0.05, min(0.95, prob_outbreak))

    if prob_outbreak > 0.5:
        result_text = f"High Risk of Outbreak (Score: {prob_outbreak:.2f})"
        result_class = "high-risk"
    else:
        result_text = f"Low Risk of Outbreak (Score: {prob_outbreak:.2f})"
        result_class = "low-risk"

    return result_text, result_class

def predict():
    try:
        rainfall = float(entry_rainfall.get())
        temperature = float(entry_temperature.get())
        population_density = float(entry_population.get())
        sanitation_index = float(entry_sanitation.get())

        if not 0 <= sanitation_index <= 1:
            raise ValueError("Sanitation index must be between 0 and 1.")

        result_text, risk_level = simulate_prediction(rainfall, temperature, population_density, sanitation_index)

        result_label.config(text=result_text)
        if risk_level == "high-risk":
            result_label.config(foreground="#ef4444")  # red
        else:
            result_label.config(foreground="#22c55e")  # green

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.\nSanitation Index must be between 0 and 1.")

# --- Tkinter Modern UI ---
root = tk.Tk()
root.title("Waterborne Disease Predictor")
root.geometry("500x500")
root.configure(bg="#f0f2f5")

style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 10), background="#f0f2f5")
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
style.configure("TEntry", padding=6)

frame = ttk.Frame(root, padding=20)
frame.pack(pady=30)

header = ttk.Label(frame, text="Waterborne Disease Predictor", font=("Segoe UI", 16, "bold"))
header.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Input fields
fields = [
    ("Average Rainfall (mm):", "entry_rainfall"),
    ("Average Temperature (°C):", "entry_temperature"),
    ("Population Density (persons/km²):", "entry_population"),
    ("Sanitation Index (0.0 - 1.0):", "entry_sanitation")
]

entries = {}

for i, (label_text, var_name) in enumerate(fields):
    ttk.Label(frame, text=label_text).grid(row=i+1, column=0, sticky="e", pady=8, padx=5)
    entry = ttk.Entry(frame, width=30)
    entry.grid(row=i+1, column=1, pady=8, padx=5)
    entries[var_name] = entry

entry_rainfall = entries["entry_rainfall"]
entry_temperature = entries["entry_temperature"]
entry_population = entries["entry_population"]
entry_sanitation = entries["entry_sanitation"]

# Predict button
predict_btn = ttk.Button(frame, text="Predict Risk", command=predict)
predict_btn.grid(row=6, column=0, columnspan=2, pady=20)

# Result display
result_label = ttk.Label(frame, text="Enter values and click Predict", font=("Segoe UI", 12, "bold"))
result_label.grid(row=7, column=0, columnspan=2, pady=10)

# Set defaults
entry_rainfall.insert(0, "120")
entry_temperature.insert(0, "26")
entry_population.insert(0, "450")
entry_sanitation.insert(0, "0.6")

root.mainloop()
