while True:   
    from tkinter import*
    root=Tk()
    root.title('Age finder')
    root.geometry('700x200')
    root.config(bg='#94fc03')
    Label(text='DATE>>>>>',font=('comicsansms',10,'bold'),fg='#fc033d',bg='#94fc03').grid(row=1)
    Label(text='MONTH>>>>>',font=('comicsansms',10,'bold'),fg='#fc033d',bg='#94fc03').grid(row=2)
    Label(text='YEAR>>>>>',font=('comicsansms',10,'bold'),fg='#fc033d',bg='#94fc03').grid(row=3)
    Label(text='ABOUT YEAR YOU BORN',font=('comicsansms',13,'bold'),fg='purple',bg='#94fc03').grid(row=0,column=1)
    date=StringVar()
    month=StringVar()
    year=StringVar()
    dateentry=Entry(textvariable=date,border=4,fg='white',bg='purple')
    monthentry=Entry(textvariable=month,border=4,fg='white',bg='purple')
    yearentry=Entry(textvariable=year,border=4,fg='white',bg='purple')
    dateentry.grid(row=1,column=1)
    monthentry.grid(row=2,column=1)
    yearentry.grid(row=3,column=1)
    import tkinter.messagebox as tmsg
    def age():
        tyear= int(yearentry1.get())
        tmonth=int(monthentry1.get())
        tdate=int(dateentry1.get())

        byear=int(yearentry.get())
        bmonth=int(monthentry.get())
        bdate=int(dateentry.get())

        yearsold= tyear-byear
        if byear>tyear:
         tmsg.showinfo('error','pls type a valid year')
        if tmonth<bmonth:
          yearsold-=1
          monthold=12-(bmonth-tmonth)
          if tdate>=bdate:
            daysold=tdate-bdate
          if tdate<bdate:
            monthold-=1
            daysold=(31-bdate)+tdate
          Label(text=f'you are {daysold}days,{monthold}month,{yearsold}year old',font=('comicsansms',13,'bold'),fg='blue',bg='#94fc03').grid(row=5,column=0)

        if tmonth>bmonth:
           monthold=tmonth-bmonth
           if tdate>=bdate:
            daysold=tdate-bdate
           if tdate<bdate:
            monthold-=1
            daysold=(31-bdate)+tdate
           Label(text=f'you are {daysold}days,{monthold}month,{yearsold}year old',font=('comicsansms',13,'bold'),fg='blue',bg='#94fc03').grid(row=5,column=0)
        
        if tmonth==bmonth:
          monthold=tmonth-bmonth
          if tdate>=bdate:
            daysold=tdate-bdate
          if tdate<bdate:
            monthold-=1
            daysold=(31-bdate)+tdate
          Label(text=f'you are {daysold}days,{monthold}month,{yearsold}year old',font=('comicsansms',13,'bold'),fg='blue',bg='#94fc03').grid(row=5,column=0)

    def reset():
       root.destroy()



    Label(text='ABOUT TODAY',font=('comicsansms',13,'bold'),fg='purple',bg='#94fc03').grid(row=0,column=4)
    Label(text='<............>',font=('comicsansms',10,'bold'),fg='red',bg='#94fc03').grid(row=2,column=3)
    date=StringVar()
    month=StringVar()
    year=StringVar()
    dateentry1=Entry(textvariable=date,border=4,fg='white',bg='purple')
    monthentry1=Entry(textvariable=month,border=4,fg='white',bg='purple')
    yearentry1=Entry(textvariable=year,border=4,fg='white',bg='purple')
    dateentry1.grid(row=1,column=4)
    monthentry1.grid(row=2,column=4)
    yearentry1.grid(row=3,column=4)
    Button(text='Submit',command=age,font=('comicsansms',10,'bold'),fg='black',padx=12,pady=5,bg='cyan').grid(row=4,column=1,padx=1,pady=1)
    Button(text='quit',command=quit,font=('comicsansms',10,'bold'),fg='black',padx=12,pady=5,bg='cyan').grid(row=4,column=3,padx=1,pady=1)
    Button(text='reset',command=reset,font=('comicsansms',10,'bold'),fg='black',padx=12,pady=5,bg='cyan').grid(row=4,column=2,padx=1,pady=1)
    root.mainloop()
