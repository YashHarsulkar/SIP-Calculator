import tkinter as tk
from tkinter import messagebox

def calculate_sip():
    try:
        monthly_investment = float(entry_investment.get())
        annual_rate = float(entry_rate.get())
        years = int(entry_years.get())

        months = years * 12
        monthly_rate = annual_rate / (12 * 100)

        final_value = monthly_investment * (((1 + monthly_rate) ** months - 1) * (1 + monthly_rate)) / monthly_rate
        invested = monthly_investment * months
        returns = final_value - invested

        label_invested.config(text=f"Total Invested: ₹ {invested:,.2f}")
        label_returns.config(text=f"Estimated Returns: ₹ {returns:,.2f}")
        label_final.config(text=f"Total Value: ₹ {final_value:,.2f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def reset_fields():
    entry_investment.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    entry_years.delete(0, tk.END)
    label_invested.config(text="")
    label_returns.config(text="")
    label_final.config(text="")

# App window
app = tk.Tk()
app.title("📊 SIP Calculator")
app.geometry("360x520")
app.configure(bg="#ffffff")

# Header
tk.Label(app, text="SIP Calculator", font=("Arial", 20, "bold"), bg="#ffffff", fg="#007BFF").pack(pady=20)

# Input Fields
frame = tk.Frame(app, bg="#ffffff")
frame.pack(pady=10)

def create_input(label_text, entry_var):
    tk.Label(frame, text=label_text, font=("Arial", 12), bg="#ffffff", anchor="w").pack(fill="x", padx=30, pady=(10, 0))
    entry = tk.Entry(frame, textvariable=entry_var, font=("Arial", 12), bd=2, relief="groove")
    entry.pack(fill="x", padx=30, pady=5)
    return entry

entry_investment = create_input("Monthly Investment (₹):", tk.StringVar())
entry_rate = create_input("Expected Annual Return (%):", tk.StringVar())
entry_years = create_input("Investment Duration (Years):", tk.StringVar())

# Buttons
tk.Button(app, text="Calculate", command=calculate_sip, bg="#28a745", fg="white", font=("Arial", 12), width=15).pack(pady=10)
tk.Button(app, text="Reset", command=reset_fields, bg="#dc3545", fg="white", font=("Arial", 12), width=15).pack(pady=5)

# Results
result_frame = tk.Frame(app, bg="#ffffff")
result_frame.pack(pady=20)

label_invested = tk.Label(result_frame, text="", font=("Arial", 12), bg="#ffffff", fg="#333")
label_invested.pack(pady=5)

label_returns = tk.Label(result_frame, text="", font=("Arial", 12), bg="#ffffff", fg="#333")
label_returns.pack(pady=5)

label_final = tk.Label(result_frame, text="", font=("Arial", 14, "bold"), bg="#ffffff", fg="#007BFF")
label_final.pack(pady=10)

# Start GUI
app.mainloop()
