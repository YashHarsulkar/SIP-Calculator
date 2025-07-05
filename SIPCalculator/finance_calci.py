import tkinter as tk
from tkinter import messagebox

# ================= Main Window ===================
def open_sip_calculator():
    window = tk.Toplevel()
    window.title("SIP Calculator")
    window.geometry("350x400")
    window.configure(bg="white")

    def calculate_sip():
        try:
            monthly = float(sip_entry1.get())
            rate = float(sip_entry2.get()) / 100 / 12
            years = int(sip_entry3.get())
            months = years * 12
            total = monthly * (((1 + rate)**months - 1) * (1 + rate)) / rate
            result.config(text=f"Total Value: ₹ {total:,.2f}")
        except:
            messagebox.showerror("Error", "Invalid input!")

    tk.Label(window, text="SIP Calculator", font=("Arial", 16), bg="white").pack(pady=10)
    sip_entry1 = tk.Entry(window)
    sip_entry2 = tk.Entry(window)
    sip_entry3 = tk.Entry(window)
    for label, entry in zip(["Monthly Investment (₹):", "Annual Rate (%):", "Years:"],
                            [sip_entry1, sip_entry2, sip_entry3]):
        tk.Label(window, text=label, bg="white").pack()
        entry.pack(pady=5)

    tk.Button(window, text="Calculate", command=calculate_sip, bg="green", fg="white").pack(pady=10)
    result = tk.Label(window, text="", bg="white", font=("Arial", 12))
    result.pack()

def open_fd_calculator():
    window = tk.Toplevel()
    window.title("FD Calculator")
    window.geometry("350x400")
    window.configure(bg="white")

    def calculate_fd():
        try:
            principal = float(fd_entry1.get())
            rate = float(fd_entry2.get()) / 100
            years = float(fd_entry3.get())
            maturity = principal * (1 + rate) ** years
            result.config(text=f"Maturity Amount: ₹ {maturity:,.2f}")
        except:
            messagebox.showerror("Error", "Invalid input!")

    tk.Label(window, text="FD Calculator", font=("Arial", 16), bg="white").pack(pady=10)
    fd_entry1 = tk.Entry(window)
    fd_entry2 = tk.Entry(window)
    fd_entry3 = tk.Entry(window)
    for label, entry in zip(["Principal (₹):", "Annual Rate (%):", "Years:"],
                            [fd_entry1, fd_entry2, fd_entry3]):
        tk.Label(window, text=label, bg="white").pack()
        entry.pack(pady=5)

    tk.Button(window, text="Calculate", command=calculate_fd, bg="blue", fg="white").pack(pady=10)
    result = tk.Label(window, text="", bg="white", font=("Arial", 12))
    result.pack()

def open_rd_calculator():
    window = tk.Toplevel()
    window.title("RD Calculator")
    window.geometry("350x400")
    window.configure(bg="white")

    def calculate_rd():
        try:
            monthly = float(rd_entry1.get())
            rate = float(rd_entry2.get()) / 100 / 4
            years = int(rd_entry3.get())
            n = years * 4
            maturity = monthly * n + monthly * n * (n + 1) * rate / 2400
            result.config(text=f"Maturity Amount: ₹ {maturity:,.2f}")
        except:
            messagebox.showerror("Error", "Invalid input!")

    tk.Label(window, text="RD Calculator", font=("Arial", 16), bg="white").pack(pady=10)
    rd_entry1 = tk.Entry(window)
    rd_entry2 = tk.Entry(window)
    rd_entry3 = tk.Entry(window)
    for label, entry in zip(["Monthly Deposit (₹):", "Annual Rate (%):", "Years:"],
                            [rd_entry1, rd_entry2, rd_entry3]):
        tk.Label(window, text=label, bg="white").pack()
        entry.pack(pady=5)

    tk.Button(window, text="Calculate", command=calculate_rd, bg="purple", fg="white").pack(pady=10)
    result = tk.Label(window, text="", bg="white", font=("Arial", 12))
    result.pack()

def open_emi_calculator():
    window = tk.Toplevel()
    window.title("EMI Calculator")
    window.geometry("350x400")
    window.configure(bg="white")

    def calculate_emi():
        try:
            principal = float(emi_entry1.get())
            rate = float(emi_entry2.get()) / 12 / 100
            months = int(emi_entry3.get())
            emi = (principal * rate * (1 + rate)**months) / ((1 + rate)**months - 1)
            result.config(text=f"EMI: ₹ {emi:,.2f}")
        except:
            messagebox.showerror("Error", "Invalid input!")

    tk.Label(window, text="EMI Calculator", font=("Arial", 16), bg="white").pack(pady=10)
    emi_entry1 = tk.Entry(window)
    emi_entry2 = tk.Entry(window)
    emi_entry3 = tk.Entry(window)
    for label, entry in zip(["Loan Amount (₹):", "Annual Interest Rate (%):", "Tenure (Months):"],
                            [emi_entry1, emi_entry2, emi_entry3]):
        tk.Label(window, text=label, bg="white").pack()
        entry.pack(pady=5)

    tk.Button(window, text="Calculate", command=calculate_emi, bg="orange", fg="white").pack(pady=10)
    result = tk.Label(window, text="", bg="white", font=("Arial", 12))
    result.pack()

# ============= Home Window ================
app = tk.Tk()
app.title("Finance Calculator")
app.geometry("360x500")
app.configure(bg="#f0f4f8")

tk.Label(app, text="📱 Welcome to Finance Calculator", font=("Arial", 16, "bold"), bg="#f0f4f8", fg="#333").pack(pady=30)

tk.Button(app, text="SIP Calculator", command=open_sip_calculator, bg="#007BFF", fg="white", font=("Arial", 12), width=25).pack(pady=10)
tk.Button(app, text="FD Calculator", command=open_fd_calculator, bg="#17a2b8", fg="white", font=("Arial", 12), width=25).pack(pady=10)
tk.Button(app, text="RD Calculator", command=open_rd_calculator, bg="#6f42c1", fg="white", font=("Arial", 12), width=25).pack(pady=10)
tk.Button(app, text="EMI Calculator", command=open_emi_calculator, bg="#fd7e14", fg="white", font=("Arial", 12), width=25).pack(pady=10)

tk.Label(app, text="© 2025 Finance Calculator", font=("Arial", 10), bg="#f0f4f8").pack(side="bottom", pady=20)

app.mainloop()
