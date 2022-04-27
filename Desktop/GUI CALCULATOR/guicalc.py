from tkinter import *
root=Tk()
font1='Al-Amraco 20'
root.title("GUI Calculator")           
#display=Entry(root,width=18,font=('Al-Amraco',85)) 
display=Entry(root,width=50,bg='#b5b545',relief=FLAT,font=font1)
root.config(bg="#beccc4")

display.insert(0,"0")

display.grid(row=0,column=0,columnspan=4)

#clearfunction

def clear():
    display.delete(0,END)
    display.insert(0,'0')
   
#backfunction


def back():
    value=display.get()
    display.delete(len(value)-1,END)
    
#putvalue

def put_value(value):
    if (display.get()=='0'):
        display.delete(0,END)
        display.insert(END,value)
    else:
        display.insert(END,value)
        
def set_op(op):
    num=display.get()
    global operand
    global number1
    number1=float(num)
    operand=str(op)
    display.delete(0,END)

#equalfunction

def equal():
    global operand
    global number1
    number2=float(display.get())
    display.delete(0,END)

    if (operand=="+"):
        
        result= number1+number2
       
    elif operand=="-":
        result= number1-number2

    elif operand=="*":
        
        result= number1*number2
  
   
    elif operand=="/":
        
        result= number1/number2
    display.insert(0,result)

    
    

#row1

btn_plus=Button(root,text="+",command=lambda:set_op("+"),bg='#ece8e8',activebackground='#c9c8cb').grid(row=1,column=0,ipadx=24,ipady=10,padx=1,pady=1)
btn_minus=Button(root,text="-",command=lambda:set_op("-"),bg='#ece8e8',activebackground='#c9c8cb').grid(row=1,column=1,ipadx=20,ipady=11,padx=1,pady=1)
btn_clear=Button(root,text="C",command=clear,bg='#ece8e8',activebackground='#c9c8cb').grid(row=1,column=2,ipadx=20,ipady=11,padx=1,pady=1)
btn_back=Button(root,text="<--",command=back,bg='#ece8e8',activebackground='#c9c8cb').grid(row=1,column=3,ipadx=20,ipady=11,padx=1,pady=1)


#row2

btn_7=Button(root,text="7",command=lambda:put_value(7),bg='#ece8e8',activebackground='#c9c8cb').grid(row=2,column=0,ipadx=20,ipady=11,padx=1,pady=1)
btn_8=Button(root,text="8",command=lambda:put_value(8),bg='#ece8e8',activebackground='#c9c8cb').grid(row=2,column=1,ipadx=20,ipady=11,padx=1,pady=1)
btn_9=Button(root,text="9",command=lambda:put_value(9),bg='#ece8e8',activebackground='#c9c8cb').grid(row=2,column=2,ipadx=20,ipady=11,padx=1,pady=1)
btn_multiply=Button(root,text="*",command=lambda:set_op("*"),bg='#ece8e8',activebackground='#c9c8cb').grid(row=2,column=3,ipadx=20,ipady=11,padx=1,pady=1)


#row3

btn4=Button(root,text="4",command=lambda:put_value(4),bg='#ece8e8',activebackground='#c9c8cb').grid(row=3,column=0,ipadx=20,ipady=11,padx=1,pady=1)
btn5=Button(root,text="5",command=lambda:put_value(5),bg='#ece8e8',activebackground='#c9c8cb').grid(row=3,column=1,ipadx=20,ipady=11,padx=1,pady=1)
btn6=Button(root,text="6",command=lambda:put_value(6),bg='#ece8e8',activebackground='#c9c8cb').grid(row=3,column=2,ipadx=20,ipady=11,padx=1,pady=1)
btn_divide=Button(root,text="/",command=lambda:set_op("/"),bg='#ece8e8',activebackground='#c9c8cb').grid(row=3,column=3,ipadx=20,ipady=11,padx=1,pady=1)


#row4

btn1=Button(root,text="1",command=lambda:put_value(1),bg='#ece8e8',activebackground='#c9c8cb').grid(row=4,column=0,ipadx=20,ipady=11,padx=1,pady=1)
btn2=Button(root,text="2",command=lambda:put_value(2),bg='#ece8e8',activebackground='#c9c8cb').grid(row=4,column=1,ipadx=20,ipady=11,padx=2,pady=1)
btn3=Button(root,text="3",command=lambda:put_value(0),bg='#ece8e8',activebackground='#c9c8cb').grid(row=4,column=2,ipadx=20,ipady=11,padx=1,pady=1)



#row5

btn_equal=Button(root,text="=",command=equal,bg='#ece8e8',activebackground='#c9c8cb').grid(row=5,column=1,rowspan=2,ipadx=100,ipady=11,padx=1,pady=1)
btn_0=Button(root,text="0",command=lambda:put_value(0),bg='#ece8e8',activebackground='#c9c8cb').grid(row=5,column=0,ipadx=20,ipady=11,padx=15,pady=1)

btn_point=Button(root,text=".",bg='#ece8e8',activebackground='#c9c8cb').grid(row=4,column=3,ipadx=20,ipady=11,padx=1,pady=1)






                                
                                  




root.mainloop()