from tkinter import *
 
import subprocess
 
window = Tk()
 
window.title("Object Detection Application")
 
window.geometry('650x700')

window.config(bg='azure3')

selected = IntVar()

label1 = Label(window, text = 'Welcome To The Object Detection Application', bg='azure3', fg='turquoise4', font=("Helvetica", 16))

label2 = Label(window, text = 'Currently We Support Object Detection Of only 7 Objects---', bg='azure3', fg='turquoise4')

label3 = Label(window, text = 'BOTTLE ---- MOBILE ---- PEN----AJITESH----KNIFE----GUN----SCISSORS', bg='azure3', fg='indian red')

label4 = Label(window, text = 'Please click on the button for which you want to search', bg='azure3', fg='turquoise4')

label5 = Label(window, text = "Develeoped for : TCS [TATA CONSULTANCY SERVICES - INTERNSHIP PROJECT]", bg='azure3', fg='indian red')
 
rad1 = Radiobutton(window,text='Bottle', value=1, variable=selected, bg='azure3')
 
rad2 = Radiobutton(window,text='Mobile', value=2, variable=selected, bg='azure3')
 
rad3 = Radiobutton(window,text='Pen', value=3, variable=selected, bg='azure3')

rad4 = Radiobutton(window,text='Ajitesh', value=4, variable=selected, bg='azure3')

rad5 = Radiobutton(window,text='Gun', value=5, variable=selected, bg='azure3')

rad6 = Radiobutton(window,text='Knives', value=6, variable=selected, bg='azure3')

rad7 = Radiobutton(window,text='Scissors', value=7, variable=selected, bg='azure3')
 
def clicked():
 
   print("running the clicked function")
   file = open('obd_input.txt','w')
   file.write(str(selected.get()))
   file.close()
   file2 = open('obd_input.txt','r')
   print(file2.read(1))
   file2.close()
   subprocess.check_call(["python3", "object_detection_UPDATED.py"])

 
btn = Button(window, text="PROCEED -->", command=clicked, bg='SpringGreen3')

label1.grid(column = 0, row = 2, padx=10, pady=10)

label2.grid(column = 0 , row = 4, padx=10, pady=10)

label3.grid(column = 0, row = 6, padx=10, pady=10)

label4.grid(column = 0, row = 8, padx=10, pady=(10,30))
 
rad1.grid(column=0, row=12, padx=0, pady=5)
 
rad2.grid(column=1, row=12, padx=0, pady=5)
 
rad3.grid(column=0, row=13, padx=0, pady=5)

rad4.grid(column=1, row=13, padx=0, pady=5)

rad5.grid(column=0, row=14, padx=0, pady=5)

rad6.grid(column=1, row=14, padx=0, pady=5)

rad7.grid(column=0, row=15, padx=0, pady=5)
 
btn.grid(column=0, row=18, padx=20, pady=50)

label5.grid(column=0, row=20, padx=(50,10), pady=10)
 
window.mainloop()
