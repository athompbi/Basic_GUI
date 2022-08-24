import tkinter as tk

window = tk.Tk()

window.title('Weight Converter')

### variables for checkboxes
var1 = tk.IntVar()
var2 = tk.IntVar()

## Weight Label
lbl_weight = tk.Label(text = "What is the weight?")
lbl_weight.pack()

### Weight Entry
ent_weight = tk.Entry()
ent_weight.pack()

### Units Label
lbl_units = tk.Label(text = "What are the units?")
lbl_units.pack()


def lbs_to_kgs(weight):
    kgs = int(weight) * 2.2
    return kgs

def kgs_to_lbs(weight):
    lbs = int(weight) / 2.2
    return lbs

def convert_units():
    ### if lbs -> kgs
    if (var1.get() == 1) & (var2.get() == 0):
        ### get the weight to convert from the entry
        weight = ent_weight.get()
        ### run the weight through the converter
        kgs = lbs_to_kgs(weight)
        ### add converted weight to results label
        lbl_results.config(text=f"{weight} lbs = {kgs} kgs")

    ### if kgs -> lbs
    elif (var1.get() == 0) & (var2.get() == 1):
        weight = ent_weight.get()
        lbs = kgs_to_lbs(weight)
        lbl_results.config(text=f'{weight} kgs = {lbs} lbs')
        

c1 = tk.Checkbutton(window, text='Lbs',variable=var1, onvalue=1, offvalue=0, command=convert_units)
c1.pack()
c2 = tk.Checkbutton(window, text='Kgs',variable=var2, onvalue=1, offvalue=0, command=convert_units)
c2.pack()

### Conversion Results Label
lbl_results = tk.Label(text = '')
lbl_results.pack()


window.mainloop()

