import tkinter as tk
  
#window
root = tk.Tk()
root.title("Caleb Tech Flex")
root.geometry('400x200')

def unit():
    unit = unitText.get(1.0, 'end-1c')
    print(unit)

# TextBox Creation
unitLabel = tk.Label(root, text = "What Unit would You like to convert to?")
unitLabel.pack()
  
unitText = tk.Text(root, height = 5, width = 10)
unitText.pack()

# Button Creation
printButton = tk.Button(root, text = "Lock In Units", command = unit)
printButton.pack()
  
# Label Creation
label = tk.Label(root, text = "")
label.pack()
root.mainloop()