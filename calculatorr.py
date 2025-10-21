import tkinter as tk
from math import sin, cos, tan, sqrt, log

# Main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("450x600")
root.configure(bg="#1b1b2f")

# Entry display
entry = tk.Entry(root, font=("Arial", 24), borderwidth=0, relief="ridge", bg="#1b1b2f", fg="white", justify="right")
entry.pack(fill="both", ipadx=8, pady=15, padx=10)

# Functions
def press(num):
    entry.insert(tk.END, num)

def clear():
    entry.delete(0, tk.END)

def delete():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        expr = entry.get()
        expr = expr.replace('^', '**')
        entry.delete(0, tk.END)
        entry.insert(tk.END, eval(expr))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def apply_func(func):
    try:
        val = float(entry.get())
        entry.delete(0, tk.END)
        if func == "sin":
            entry.insert(tk.END, round(sin(val), 6))
        elif func == "cos":
            entry.insert(tk.END, round(cos(val), 6))
        elif func == "tan":
            entry.insert(tk.END, round(tan(val), 6))
        elif func == "sqrt":
            entry.insert(tk.END, round(sqrt(val), 6))
        elif func == "log":
            entry.insert(tk.END, round(log(val, 10), 6))
        elif func == "1/x":
            entry.insert(tk.END, round(1/val, 6))
        elif func == "x^2":
            entry.insert(tk.END, val**2)
        elif func == "x^3":
            entry.insert(tk.END, val**3)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Button colors
num_color = "#4e4e6d"
op_color = "#ff8c42"
func_color = "#6a5acd"
hover_color = "#8888ff"

# Buttons layout
btns = [
    ['7','8','9','/','sqrt'],
    ['4','5','6','*','x^2'],
    ['1','2','3','-','x^3'],
    ['0','.','=','+','1/x'],
    ['sin','cos','tan','log','C']
]

# Create buttons
for r, row in enumerate(btns):
    frame = tk.Frame(root, bg="#1b1b2f")
    frame.pack(expand=True, fill="both")
    for c, btn in enumerate(row):
        color = num_color if btn.isdigit() or btn == '.' else func_color if btn in ['sin','cos','tan','log','sqrt','1/x','x^2','x^3'] else op_color
        b = tk.Button(frame, text=btn, font=("Arial",18), fg="white", bg=color, borderwidth=0,
                      command=lambda x=btn: calculate() if x=='=' else clear() if x=='C' else apply_func(x) if x in ['sin','cos','tan','log','sqrt','1/x','x^2','x^3'] else press(x))
        b.pack(side="left", expand=True, fill="both", padx=3, pady=3)
        
        # Hover effect
        def on_enter(e, b=b):
            b['bg'] = hover_color
        def on_leave(e, b=b, color=color):
            b['bg'] = color
        b.bind("<Enter>", on_enter)
        b.bind("<Leave>", on_leave)

root.mainloop()
