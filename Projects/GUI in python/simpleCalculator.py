import tkinter as tk

root = tk.Tk()

entry = tk.Entry(root)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7","8","9","+",
    "4","5","6","-",
    "1","2","3","*",
    "C","0","=","/"
]

def click(btn):
    if btn == "=":
        entry.insert(tk.END, "="+str(eval(entry.get())))
    elif btn == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn)

row = 1
col = 0
for b in buttons:
    tk.Button(root, text=b, width=5, command=lambda b=b: click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()