import random
from tkinter import *
from tkinter import messagebox as mbox, ttk

import mysql.connector as ms
from PIL import ImageTk
from tabulate import tabulate
from tkcalendar import DateEntry


def login():
    tk = Tk(className=" LOGIN PAGE")
    tk.geometry("1200x1000+0+0")

    bg = ImageTk.PhotoImage(file="theatre.jpg", master=tk)

    canvas = Canvas(tk, width="1200", height="1000", bd=0, highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)

    canvas.create_image(600, 400, image=bg)

    canvas.create_text(620, 90, text="WELCOME TO MOVIE HITS", font=("Algerian", 40), fill="white")

    login_but = Button(tk, text="LOGIN", font=("Consolas", 12, 'bold'), bg="spring green", height='1',
                       width='20', command=lambda: user(User_entry, Pass_entry))
    canvas.create_window(700, 330, window=login_but)

    canvas.create_text(360, 400, text="New User? ", font=("Arial", 16, "bold"))

    create_but = Button(tk, text="CREATE ACCOUNT", font=("Consolas", 12, 'bold'), bg="red", height='1',
                        width='20', command=lambda: create())
    canvas.create_window(520, 400, window=create_but)

    def user(User_, Pass_):
        user = User_.get()
        pass_ = Pass_.get()

        mycon = ms.connect(host='localhost', user='root',
                           password='fra@mysqlroot2003',
                           database='Projectcse5a')
        cur = mycon.cursor()

        cur.execute("select Login_Id, Password from Customer where Login_Id='{}' and Password='{}'".format(user, pass_))
        login_credentials = cur.fetchall()
        # [('rfa','6464')]
        count = cur.rowcount

        if count > 0:
            if user == login_credentials[0][0] and pass_ == login_credentials[0][1]:
                tk.destroy()
                options(user)

        else:
            mbox.showerror("Invalid", "Incorrect Username or Password")

    tk.mainloop()


def create():
    tk1 = Tk(className=" MY PROFILE")
    tk1.geometry("1200x1000+0+0")

    bg1 = ImageTk.PhotoImage(file="theatre.jpg", master=tk1)

    canvas1 = Canvas(tk1, width="1200", height="1000", bd=0, highlightthickness=0)
    canvas1.pack(fill=BOTH, expand=True)

    canvas1.create_image(600, 400, image=bg1)
    canvas1.create_text(620, 90, text="ENTER THE DETAILS", font=("Algerian", 40), fill="white")

    canvas1.create_text(400, 200, text="USER NAME", font=("Arial", 20, "bold"))
    canvas1.create_text(400, 260, text="PASSWORD", font=("Arial", 20, "bold"))
    canvas1.create_text(400, 320, text="EMAIL ID", font=("Arial", 20, "bold"))
    canvas1.create_text(400, 380, text="DOB", font=("Arial", 20, "bold"))
    canvas1.create_text(400, 440, text="PHONE NO", font=("Arial", 20, "bold"))

    User_entry = Entry(tk1, width=30, font=("Arial", 15, 'bold'), highlightthickness=1)
    Pass_entry = Entry(tk1, width=30, font=("Arial", 15, 'bold'), highlightthickness=1)
    Email_entry = Entry(tk1, width=30, font=("Arial", 15, 'bold'), highlightthickness=1)
    Dob_entry = DateEntry(tk1, width=26, font=("Arial", 16, 'bold'), selectmode='day')
    Phone_entry = Entry(tk1, width=30, font=("Arial", 15, 'bold'), highlightthickness=1)

    canvas1.create_window(700, 200, window=User_entry)
    canvas1.create_window(700, 260, window=Pass_entry)
    canvas1.create_window(700, 320, window=Email_entry)
    canvas1.create_window(700, 380, window=Dob_entry)
    canvas1.create_window(700, 440, window=Phone_entry)

    submit_but = Button(tk1, text="SUBMIT", font=("Consolas", 12, 'bold'), bg="light blue", height='1',
                        width='20',
                        command=lambda: submit(User_entry, Pass_entry, Email_entry, Dob_entry, Phone_entry))
    canvas1.create_window(700, 500, window=submit_but)

    def submit(User_, Pass_, Email_, Dob_, Phone_):
        mycon = ms.connect(host='localhost', user='root', password='fra@mysqlroot2003', database='Projectcse5a')
        cur = mycon.cursor()

        User = User_.get()
        Pass = Pass_.get()
        Email = Email_.get()
        Dob = Dob_.get()
        Phone = Phone_.get()

        if User != '' and Pass != '' and Email != '' and Phone != '':
            cur.execute("Insert into  customer values(%s,%s,%s,STR_TO_DATE(%s,'%m/%d/%y'),%s)",
                        (User, Pass, Email, Dob, Phone))

            mycon.commit()
            mycon.close()

            User_.delete(0, END)
            Pass_.delete(0, END)
            Dob_.delete(0, END)
            Email_.delete(0, END)
            Phone_.delete(0, END)

            mbox.showinfo("User Details", "Details are successfully saved")

        else:
            mbox.showerror("Incomplete Details", "Please fill in all the fields")

    tk1.mainloop()


def options(User_):
    tk2 = Tk(className=" WELCOME USER")
    tk2.geometry("1200x1000+0+0")

    bg2 = ImageTk.PhotoImage(file="theatre.jpg", master=tk2)

    canvas2 = Canvas(tk2, width="1200", height="1000", bd=0, highlightthickness=0)
    canvas2.pack(fill=BOTH, expand=True)

    canvas2.create_image(600, 400, image=bg2)
    canvas2.create_text(620, 90, text="WELCOME " + User_, font=("Algerian", 40), fill="white")

    edit_but = Button(tk2, text="EDIT MY PROFILE", font=("Consolas", 18, 'bold'), bg="maroon", fg="white", height='2',
                      width='50', command=lambda: edit_profile(User_))
    canvas2.create_window(605, 200, window=edit_but)

    view_but = Button(tk2, text="VIEW MY BOOKINGS", font=("Consolas", 18, 'bold'), bg="maroon", fg="white", height='2',
                      width='50', command=lambda: my_bookings(User_))
    canvas2.create_window(605, 290, window=view_but)
  
    tk2.mainloop()


def edit_profile(User_):
    tk3 = Tk(className=" EDIT PROFILE")
    tk3.geometry("1200x1000+0+0")

    bg3 = ImageTk.PhotoImage(file="theatre.jpg", master=tk3)

    canvas3 = Canvas(tk3, width="1200", height="1000", bd=0, highlightthickness=0)
    canvas3.pack(fill=BOTH, expand=True)

    canvas3.create_image(600, 400, image=bg3)

    Email_entry = Entry(tk3, width=30, font=("Arial", 20, 'bold'), highlightthickness=1)
    Phone_entry = Entry(tk3, width=30, font=("Arial", 20, 'bold'), highlightthickness=1)

    canvas3.create_window(700, 270, window=Email_entry)
    canvas3.create_window(700, 340, window=Phone_entry)

    edit_but = Button(tk3, text="UPDATE PROFILE", font=("Consolas", 12, 'bold'), bg="red", fg="white",
                      height='1', width='20', command=lambda: edit(User_, Email_entry, Phone_entry))
    canvas3.create_window(700, 420, window=edit_but)

    def edit(login, email_entry, phone_entry):
        email = email_entry.get()
        phone = phone_entry.get()

        mycon = ms.connect(host='localhost', user='root', password='fra@mysqlroot2003', database='Projectcse5a')
        cur = mycon.cursor()

        mycon.commit()
        mycon.close()

        email_entry.delete(0, END)
        phone_entry.delete(0, END)

        mbox.showinfo("Update", "Details Updated Successfully")

    tk3.mainloop()


def my_bookings(User_):
    tk4 = Tk(className=" SHOWS BOOKED")
    tk4.geometry("1200x1000+0+0")

    bg5 = ImageTk.PhotoImage(file="resize.jpg", master=tk4)

    canvas4.create_image(600, 400, image=bg5)

    mycon = ms.connect(host='localhost', user='root', password='fra@mysqlroot2003', database='Projectcse5a')
    cur = mycon.cursor()

    cur.execute("Select Movie_Name, Language, Theatre_Name, Date, Timing, Payment_Id, No_Of_Seats, Type_Of_Seats,"
                "Payment_Amount from my_shows where Login_Id like '{}'".format(User_))

    records = cur.fetchall()

    tk4.mainloop()


def book_movies(User_):
    tk5 = Tk(className=" BOOKING MOVIES")
    tk5.geometry("1200x1000+0+0")

    bg5 = ImageTk.PhotoImage(file="theatre.jpg", master=tk5)

    canvas5 = Canvas(tk5, width="1200", height="1000", bd=0, highlightthickness=0)
    canvas5.pack(fill=BOTH, expand=True)

    canvas5.create_image(600, 400, image=bg5)

    canvas5.create_window(400, 250, window=Search_theatres)

    def findtheatre(e1):
        Movie_Name = e1.get()

        mycon = ms.connect(host='localhost', user='root', password='fra@mysqlroot2003', database='Projectcse5a')
        cur = mycon.cursor()

        cur.execute("Select Theatre_Name from Theatre t, Movies m, Booking b where Movie_Id=MMovie_Id and "
                    "TTheatre_Id=Theatre_Id and Movie_Name like '{}'".format(Movie_Name))

        theatres = cur.fetchall()
        count = cur.rowcount

        if count > 0:
            canvas5.create_text(410, 300, text="Choose the Movie Theatre", font=("Arial", 16, "bold"))

            theatre = []  # [(theatre1, theatre)]  #[theatre1, theatre2, theatre3, .......]
            for i in theatres:
                for j in i:
                    theatre.append(j)

            entry_2 = ttk.Combobox(tk5, values=theatre, width=36, font=("Arial", 12, 'bold'))
            canvas5.create_window(730, 300, window=entry_2)

            canvas5.create_text(390, 350, text="Choose the Language", font=("Arial", 16, "bold"))

            cur.execute("Select Languages from Movies m, Movie_languages ml where m.Movie_id=ml.Movie_id and "
                        "Movie_Name like'{}'".format(Movie_Name))

            languages = cur.fetchall()
            lang = []
            for i in languages:
                for j in i:
                    lang.append(j)

            entry_3 = ttk.Combobox(tk5, values=lang, width=36, font=("Arial", 12, 'bold'))
            canvas5.create_window(730, 350, window=entry_3)

            canvas5.create_text(400, 400, text="Choose the Show Dates", font=("Arial", 16, "bold"))

            cur.execute("Select Date from Movies m, Movie_dates md where m.Movie_id=md.Movie_id and Movie_Name like "
                        "'{}'".format(Movie_Name))

            dates = cur.fetchall()
            date = []
            for i in dates:
                for j in i:
                    date.append(j)

            entry_4 = ttk.Combobox(tk5, values=date, width=36, font=("Arial", 12, 'bold'))
            canvas5.create_window(730, 400, window=entry_4)

            canvas5.create_text(410, 450, text="Choose the Show Timings", font=("Arial", 16, "bold"))
            cur.execute("Select Timing from Movies m, Movie_timings mt where m.Movie_id=mt.Movie_id and Movie_Name like"
                        "'{}'".format(Movie_Name))

            timings = cur.fetchall()
            timing = []
            for i in timings:
                for j in i:
                    timing.append(j)

            entry_5 = ttk.Combobox(tk5, values=timing, width=36, font=("Arial", 12, 'bold'))
            canvas5.create_window(730, 450, window=entry_5)

            Proceed_but = Button(tk5, text="PROCEED", font=("Consolas", 12, 'bold'), bg="gold", height='1',
                                 width='20',
                                 command=lambda: payment(User_, Movie_Name, entry_2, entry_3, entry_4, entry_5))

            canvas5.create_window(730, 500, window=Proceed_but)

        else:
            mbox.showerror("Invalid ", "This Movie isn't Available")

    tk5.mainloop()




    def amount(e1, e2):
        Seats = {'Normal': 100, 'Executive': 140, 'Premium': 200} #DICT1={key1:v1,key2:v2}  # DICT1[key1]
        num = int(e1.get())
        Seat = e2.get()
        amt = Seats[Seat] * num

        canvas6.create_text(370, 350, text="Total Amount", font=("Arial", 16, "bold"))
        canvas6.create_text(540, 350, text=str(amt), font=("Arial", 16, "bold"))

        Pay_but = Button(tk6, text="PAY", font=("Consolas", 12, 'bold'), bg="light blue", height='1',
                         width='20', command=lambda: pay(Seat, num, amt))

        canvas6.create_window(400, 400, window=Pay_but)

    def pay(Seat, num, amt):
        canvas6.create_text(440, 450, text="Amount Paid Successfully", font=("Arial", 16, "bold"))

        Pay_id = str(random.randint(10000000, 99999999))

        canvas6.create_text(440, 500, text="Payment Id", font=("Arial", 16, "bold"))

        canvas6.create_text(640, 500, text=Pay_id, font=("Arial", 16, "bold"))

        mycon = ms.connect(host='localhost', user='root', password='fra@mysqlroot2003', database='Projectcse5a')
        cur = mycon.cursor()

        cur.execute("Insert into Payment values(%s,'ONLINE',%s)", (Pay_id, amt))

        cur.execute("Insert into my_shows(Login_Id, Movie_Name, Language, Theatre_Name, Date, Timing, Payment_Id,"
                    "No_of_Seats, Type_Of_Seats, Payment_Amount) values(%s,%s,%s,%s,STR_TO_DATE(%s,'%d-%m-%Y'),%s,%s,"
                    "%s,%s,%s)", (User_, Movie_Name.upper(), Language.upper(), Theatre_Name.upper(), Date.upper(),
                                  Timing.upper(), Pay_id, num, Seat.upper(), amt))

        mycon.commit()
        mycon.close()

    tk6.mainloop()


def delete_ticket(User_):
    tk7 = Tk(className=" DELETE MY BOOKING")
    tk7.geometry("1200x1000+0+0")

    bg = ImageTk.PhotoImage(file="theatre.jpg", master=tk7)
    canvas7 = Canvas(tk7, width="1200", height="1000", bd=0, highlightthickness=0)
    canvas7.pack(fill=BOTH, expand=True)

    canvas7.create_image(600, 400, image=bg)

    canvas7.create_text(620, 90, text="WELCOME " + User_, font=("Algerian", 40), fill="white")

    canvas7.create_text(400, 200, text="Enter the Payment Id", font=("Arial", 16, "bold"))

    mycon = ms.connect(host='localhost', user='root', password='fra@mysqlroot2003', database='Projectcse5a')
    cur = mycon.cursor()

    entry_1 = Entry(tk7, width=30, font=("Arial", 16, 'bold'), highlightthickness=1)
    canvas7.create_window(730, 200, window=entry_1)

    ticket_but = Button(tk7, text="FIND MY TICKET", font=("Consolas", 12, 'bold'), bg="light blue", height='1',
                        width='20', command=lambda: ticket(entry_1))

    canvas7.create_window(400, 240, window=ticket_but)

    def ticket(entry_1):
        Payment_Id = entry_1.get()

        cur.execute("Select Movie_Name, Theatre_Name from my_shows where Payment_Id='{}'".format(Payment_Id))
        records = cur.fetchall()
        count = cur.rowcount

        if count > 0:
            Movie_Name = records[0][0]
            Theatre_Name = records[0][1]

            canvas7.create_text(400, 300, text='MOVIE NAME', font=("Arial", 16, "bold"))
            canvas7.create_text(400, 350, text='THEATRE NAME', font=("Arial", 16, "bold"))

            canvas7.create_text(650, 300, text=Movie_Name, font=("Arial", 16, "bold"))
            canvas7.create_text(650, 350, text=Theatre_Name, font=("Arial", 16, "bold"))

            canvas7.create_text(570, 400, text='Do You Really Want To Delete?', font=("Arial", 20, "bold"))

            yes_but = Button(tk7, text="Yes", font=("Consolas", 12, 'bold'), bg="spring green", height='1',
                             width='10', command=lambda: yes(Payment_Id))
            canvas7.create_window(500, 450, window=yes_but)

            no_but = Button(tk7, text="No", font=("Consolas", 12, 'bold'), bg="red", height='1',
                            width='10', command=lambda: no())
            canvas7.create_window(650, 450, window=no_but)

            def yes(Payment_Id):
                cur.execute("delete from my_shows where Payment_Id like '{}'".format(Payment_Id))
                mbox.showinfo("Delete", "Ticket Has Been Deleted Successfully")
                mycon.commit()
                mycon.close()

            def no():
                tk7.destroy()

        else:
            mbox.showerror("Invalid ", "This Ticket Does Not Exist")

    tk7.mainloop()


login()
