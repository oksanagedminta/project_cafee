from tkinter import *
import psycopg2
import tkinter as tk
from tkinter import ttk
from traceback import StackSummary
from tkinter import messagebox
import random
from tkinter import messagebox
import time
from tkinter.font import Font
from PIL import ImageTk, Image
import datetime as date


logs=tk.Tk()
logs.title("Cafee")
logs.iconbitmap("C:/Users/gedmi/Desktop/LVT/06_Python/16.06.22/pancake.ico")
logs.geometry("1050x700")


def notirit():
    a_name.delete(0, END)
    b_name.delete(0, END)
    c_name.delete(0, END)
    d_name.delete(0, END)
    e_name.delete(0, END)
    f_name.delete(0, END)
    g_name.delete(0, END)
    b_name_sk.delete(0, END)
    c_name_sk.delete(0, END)
    d_name_sk.delete(0, END)
    e_name_sk.delete(0, END)
    f_name_sk.delete(0, END)
    g_name_sk.delete(0, END)
    b_name_sum.delete(0, END)
    c_name_sum.delete(0, END)
    d_name_sum.delete(0, END)
    e_name_sum.delete(0, END)
    f_name_sum.delete(0, END)
    g_name_sum.delete(0, END)
    h_name_sum.delete(0, END)   

def query():
    conn=psycopg2.connect(
        host="abul.db.elephantsql.com",
        database="awftyeay",
        user="awftyeay",
        password="7mA3mXW-GW8IUl25NYFWCk1cd1vCdtIV",
        port=5432
    )

def vadit():
    global laiks
    abcdefg_text=a_name.get() and b_name.get() and c_name.get() and d_name.get() and e_name.get() and f_name.get() and g_name.get()
    bcdefg_sk=b_name_sk.get() and c_name_sk.get() and d_name_sk.get() and e_name_sk.get() and f_name_sk.get() and g_name_sk.get()
    bcdefg_sum=b_name_sum.get() and c_name_sum.get() and d_name_sum.get() and e_name_sum.get() and f_name_sum.get() and g_name_sum.get()
    if abcdefg_text =="":
        messagebox.showwarning("Paziņojums!", "Lūdzu, aizpildiet visus laukus.")
    elif bcdefg_sk == "":
        messagebox.showwarning("Paziņojums!", "Lūdzu, ievadiet skaitu.")  
    elif bcdefg_sum == "":
        messagebox.showwarning("Paziņojums!", "Lūdzu, ievadiet cenu.")
    else:
        messagebox.showinfo('Paziņojuma logs', "Pasūtījums Nr.: "f" {a_name.get()} ir veikts. \n Tas būs gatavs 20 minūšu laika.")


    bb_name_sk=int(b_name_sk.get())
    bb_name_sum=float(b_name_sum.get())
    bb_name_sum_sum=(bb_name_sk * bb_name_sum)
    b_name_sum.delete(0, END)
    b_name_sum.insert(0, str(bb_name_sum_sum))
    cc_name_sk=int(c_name_sk.get())
    cc_name_sum=float(c_name_sum.get())
    cc_name_sum_sum=(cc_name_sk * cc_name_sum)
    c_name_sum.delete(0, END)
    c_name_sum.insert(0, str(cc_name_sum_sum))
    dd_name_sk=int(d_name_sk.get())
    dd_name_sum=float(d_name_sum.get())
    dd_name_sum_sum=(dd_name_sk * dd_name_sum)
    d_name_sum.delete(0, END)
    d_name_sum.insert(0, str(dd_name_sum_sum))
    ee_name_sk=int(e_name_sk.get())
    ee_name_sum=float(e_name_sum.get())
    ee_name_sum_sum=(ee_name_sk * ee_name_sum)
    e_name_sum.delete(0, END)
    e_name_sum.insert(0, str(ee_name_sum_sum))
    ff_name_sk=int(f_name_sk.get())
    ff_name_sum=float(f_name_sum.get())
    ff_name_sum_sum=(ff_name_sk * ff_name_sum)
    f_name_sum.delete(0, END)
    f_name_sum.insert(0, str(ff_name_sum_sum))
    gg_name_sk=int(g_name_sk.get())
    gg_name_sum=float(g_name_sum.get())
    gg_name_sum_sum=(gg_name_sk * gg_name_sum)
    g_name_sum.delete(0, END)
    g_name_sum.insert(0, str(gg_name_sum_sum))


    conn=psycopg2.connect(
        host="abul.db.elephantsql.com",
        database="awftyeay",
        user="awftyeay",
        password="7mA3mXW-GW8IUl25NYFWCk1cd1vCdtIV",
        port=5432
    )
    c=conn.cursor()
    c.execute('''INSERT INTO ooorder(nr, uzkodas, uzk_sk, uzk_cena, pamatedieni, pam_sk, pam_cena, piedevas, pied_sk,
    pied_cena, deserti, d_sk, d_cena, dzerieni, dz_ba, dz_ba_cena, dz_alk, dz_alk_sk, dz_alk_cena)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (a_name.get(), b_name.get(),
        b_name_sk.get(), b_name_sum.get(), c_name.get(), c_name_sk.get(), c_name_sum.get(), d_name.get(), d_name_sk.get(), d_name_sum.get(),
        e_name.get(), e_name_sk.get(), e_name_sum.get(), f_name.get(), f_name_sk.get(), f_name_sum.get(), g_name.get(), g_name_sk.get(), g_name_sum.get())
    )
    c.execute('''INSERT INTO ooorder_sk(nr, uzk_sk, pam_sk, pied_sk, d_sk, dz_ba, dz_alk_sk)
        VALUES (%s, %s, %s, %s, %s, %s, %s)''', (a_name.get(), b_name_sk.get(), c_name_sk.get(), d_name_sk.get(), e_name_sk.get(), f_name_sk.get(), g_name_sk.get())
    )
    c.execute('''INSERT INTO ooorder_sum(nr, uzk_cena, pam_cena, pied_cena, d_cena, dz_ba_cena, dz_alk_cena)
        VALUES (%s, %s, %s, %s, %s, %s, %s)''', (a_name.get(), b_name_sum.get(), c_name_sum.get(), d_name_sum.get(), e_name_sum.get(), f_name_sum.get(), g_name_sum.get())
    )
    conn.commit()
    conn.close()
    a_name.delete(0, END)
    b_name.delete(0, END)
    c_name.delete(0, END)
    d_name.delete(0, END)
    e_name.delete(0, END)
    f_name.delete(0, END)
    g_name.delete(0, END)
    b_name_sk.delete(0, END)
    c_name_sk.delete(0, END)
    d_name_sk.delete(0, END)
    e_name_sk.delete(0, END)
    f_name_sk.delete(0, END)
    g_name_sk.delete(0, END)
    b_name_sum.delete(0, END)
    c_name_sum.delete(0, END)
    d_name_sum.delete(0, END)
    e_name_sum.delete(0, END)
    f_name_sum.delete(0, END)
    g_name_sum.delete(0, END)
    h_name_sum.delete(0, END)   

def skaita_so():
    bcdefg_sk=b_name_sk.get() and c_name_sk.get() and d_name_sk.get() and e_name_sk.get() and f_name_sk.get() and g_name_sk.get()
    bcdefg_sum=b_name_sum.get() and c_name_sum.get() and d_name_sum.get() and e_name_sum.get() and f_name_sum.get() and g_name_sum.get()
    if bcdefg_sk == "":
        messagebox.showwarning("Paziņojums!", "Lai veiktu aprēķinu, ievadiet porciju skaitu.")  
    elif bcdefg_sum == "":
        messagebox.showwarning("Paziņojums!", "Lai veiktu aprēķinu, ievadiet cenu.")
    else:
        h_name_sum.delete(0, END)
        hh_name_sum=0
        bb_name_sk=int(b_name_sk.get())
        bb_name_sum=float(b_name_sum.get())
        cc_name_sk=int(c_name_sk.get())
        cc_name_sum=float(c_name_sum.get())
        dd_name_sk=int(d_name_sk.get())
        dd_name_sum=float(d_name_sum.get())
        ee_name_sk=int(e_name_sk.get())
        ee_name_sum=float(e_name_sum.get())
        ff_name_sk=int(f_name_sk.get())
        ff_name_sum=float(f_name_sum.get())
        gg_name_sk=int(g_name_sk.get())
        gg_name_sum=float(g_name_sum.get())
        hh_name_sum=(bb_name_sk * bb_name_sum) + (cc_name_sk * cc_name_sum) + (dd_name_sk * dd_name_sum) + (ee_name_sk * ee_name_sum) + (ff_name_sk * ff_name_sum) + (gg_name_sk * gg_name_sum)
        h_name_sum.insert(0, str("{:,.2f}".format(hh_name_sum)))
        messagebox.showinfo('Paziņojuma logs', "Pasūtījuma kopēja summa būs: "f" {h_name_sum.get()} eur.")


def skaita():
    conn=psycopg2.connect(
        host="abul.db.elephantsql.com",
        database="awftyeay",
        user="awftyeay",
        password="7mA3mXW-GW8IUl25NYFWCk1cd1vCdtIV",
        port=5432
    )
    c=conn.cursor()
    c.execute("SELECT SUM(uzk_cena + pied_cena + pam_cena + d_cena + dz_ba_cena + dz_alk_cena) FROM ooorder_sum;")
    records=c.fetchall()
    output=" "
    for record in records:
        i_name_sum.config(text=f"{output} {record}", font="arial, 20")
        output=i_name_sum["text"]
    conn.close()  

my_font=Font(family="Times New Roman", size=20, weight="bold", slant="italic")
my_frame=LabelFrame(logs, text="CafeE", font=my_font)
my_frame.grid(row=0, column=0, padx=10, pady=25)

def timing():
    global laiks
    laiks = time.strftime("%H : %M : %S")
    dat_laiks.config(text=f"{date.datetime.now():%x}  " + laiks)
    dat_laiks.after(200,timing)
dat_laiks=Label(my_frame)
dat_laiks.grid(row=0, column=1, pady=15, padx=30)
timing()

aa_label=Label(my_frame, text="Pasūtījuma dati:")
aa_label.grid(row=0, column=0, padx=10, pady=10)

a_label=Label(my_frame, text="Pas.Nr.")
a_label.grid(row=1, column=0, padx=10, pady=10)
"""                 # ja izmantoju "random", tad Entry jāparveido par Label, bet Ja ir Label, tad Nr.nesūtās uz DB
a="0123456789"
askaits=5
a_name=Label(my_frame, width=27, text="".join(random.sample(a, askaits)))
"""
a_name=Entry(my_frame, width=24, font=("times",10,"bold"), bg="light grey")
a_name.grid(row=1, column=1)

b_label=Label(my_frame, text="Uzkodas")
b_label.grid(row=2, column=0, padx=10, pady=10)
b_name=Entry(my_frame, width=27)
b_name.grid(row=2, column=1)

c_label=Label(my_frame, text="Pamatēdiens")
c_label.grid(row=3, column=0, padx=10, pady=10)
c_name=Entry(my_frame, width=27)
c_name.grid(row=3, column=1)

d_label=Label(my_frame, text="Piedevas")
d_label.grid(row=4, column=0, padx=10, pady=10)
d=tk.StringVar()
d_name=ttk.Combobox(my_frame, width=27, textvariable=d)
d_name["values"]=(" - ", "Rīsi", "Griķi", "Kartupeļu biezenis", "Kartupeļu daiviņas",
                    "Vārīti-cepti kartupeļi", "Kartupeļi FRĪ", "Vārītie kartupeļi")
d_name.grid(row=4, column=1, padx=10, pady=10)
d_name.current()

e_label=Label(my_frame, text="Deserts")
e_label.grid(row=5, column=0, padx=10, pady=10)
e_name=Entry(my_frame, width=27)
e_name.grid(row=5, column=1)

f_label=Label(my_frame, text="Dzērieni b/alk.")
f_label.grid(row=6, column=0, padx=10, pady=10)
f_name=Entry(my_frame, width=27)
f_name.grid(row=6, column=1)

g_label=Label(my_frame, text="Dzērieni alk.")
g_label.grid(row=7, column=0, padx=10, pady=10)
g_name=Entry(my_frame, width=27)
g_name.grid(row=7, column=1)


skaits=Label(my_frame, text="Skaits: ", font="Arial, 14")
skaits.grid(row=1, column=2, padx=5, pady=5)
b_name_sk=Entry(my_frame)
b_name_sk.grid(row=2, column=2, padx=5, pady=5)
c_name_sk=Entry(my_frame)
c_name_sk.grid(row=3, column=2, padx=5, pady=5)
d_name_sk=Entry(my_frame)
d_name_sk.grid(row=4, column=2, padx=5, pady=5)
e_name_sk=Entry(my_frame)
e_name_sk.grid(row=5, column=2, padx=5, pady=5)
f_name_sk=Entry(my_frame)
f_name_sk.grid(row=6, column=2, padx=5, pady=5)
g_name_sk=Entry(my_frame)
g_name_sk.grid(row=7, column=2, padx=5, pady=5)

cena=Label(my_frame, text="Cena Eur: ", font="Arial, 14")
cena.grid(row=1, column=3, padx=10, pady=10)
b_name_sum=Entry(my_frame)
b_name_sum.grid(row=2, column=3, padx=5, pady=5)
c_name_sum=Entry(my_frame)
c_name_sum.grid(row=3, column=3, padx=5, pady=5)
d_name_sum=Entry(my_frame)
d_name_sum.grid(row=4, column=3, padx=5, pady=5)
e_name_sum=Entry(my_frame)
e_name_sum.grid(row=5, column=3, padx=5, pady=5)
f_name_sum=Entry(my_frame)
f_name_sum.grid(row=6, column=3, padx=5, pady=5)
g_name_sum=Entry(my_frame)
g_name_sum.grid(row=7, column=3, padx=5, pady=5)

h_name_sum=Entry(my_frame, fg="blue")
h_name_sum.grid(row=8, column=3, padx=5, pady=5)
i_name_sum=Label(my_frame, text=" ")
i_name_sum.grid(row=9, column=3, padx=5, pady=5)


poga_submit=Button(my_frame, text="       Ievadīt sistēmā      ", bg="yellow", command=vadit)
poga_submit.grid(row=8, column=1, padx=10, pady=10)

poga_dzest=Button(my_frame, text="dzēsts", command=notirit)
poga_dzest.grid(row=8, column=0, padx=10, pady=10)

poga_iziet=Button(my_frame, text="Iziet", command=logs.quit)
poga_iziet.grid(row=9, column=0, padx=10, pady=10)

poga_sum1=Button(my_frame, text="Pasūtījuma summa: ", command=skaita_so)
poga_sum1.grid(row=8, column=2, padx=50, pady=10)

poga_sum2=Button(my_frame, text="Visu pasūtījumu summa", command=skaita)
poga_sum2.grid(row=9, column=2, padx=50, pady=10)

saraksts=Menu(logs)
logs.config(menu=saraksts)
faila_menu=Menu(saraksts)
saraksts.add_cascade(label="File", menu=faila_menu)
faila_menu.add_command(label="Exit", command=logs.quit)
faila_menu.add_command(label="Delete", command=notirit)

my_frame2=LabelFrame(logs, text="Kalkulātors: ")
my_frame2.grid(row=0, column=1, padx=10, pady=25)

def btnClik(number):
    current=e.get()
    e.delete(0, END)
    jauns=str(current)+str(number)
    e.insert(0, jauns)

def komm(comand):
    global mathOp
    global num1
    mathOp=comand
    num1=float(e.get())
    e.delete(0, END)

def tiriit():
    e.delete(0, END)
    num1=0
    mathOp=""

def ir():
    num2=float(e.get())
    rezultats=0
    if mathOp =="+":
        rezultats=num1+num2
    elif mathOp =="-":
        rezultats=num1-num2
    elif mathOp =="*":
        rezultats=num1*num2
    elif mathOp =="/" and num2==0:
            messagebox.showerror("Brdinjums!!!", "Ar 0 dalīt nedrīkst!!!")
    elif mathOp =="/": 
        rezultats=num1/num2
    else:
        rezultats=0
    e.delete(0, END)
    e.insert(0, str("{:,.2f}".format(rezultats)))

e=Entry(my_frame2, width=15, font=("Arial Black", 22))
poga0=Button(my_frame2, text="0", padx="30", pady="20", command=lambda:btnClik(0))
poga1=Button(my_frame2, text="1", padx="30", pady="20", command=lambda:btnClik(1))
poga2=Button(my_frame2, text="2", padx="30", pady="20", command=lambda:btnClik(2))
poga3=Button(my_frame2, text="3", padx="30", pady="20", command=lambda:btnClik(3))
poga4=Button(my_frame2, text="4", padx="30", pady="20", command=lambda:btnClik(4))
poga5=Button(my_frame2, text="5", padx="30", pady="20", command=lambda:btnClik(5))
poga6=Button(my_frame2, text="6", padx="30", pady="20", command=lambda:btnClik(6))
poga7=Button(my_frame2, text="7", padx="30", pady="20", command=lambda:btnClik(7))
poga8=Button(my_frame2, text="8", padx="30", pady="20", command=lambda:btnClik(8))
poga9=Button(my_frame2, text="9", padx="30", pady="20", command=lambda:btnClik(9))
sask=Button(my_frame2, text="+", font=100, padx="30", pady="20", command=lambda:komm("+"))
atn=Button(my_frame2, text="-", font=100, padx="30", pady="20", command=lambda:komm("-"))
reiz=Button(my_frame2, text="*", font=100, padx="30", pady="20", command=lambda:komm("*"))
dal=Button(my_frame2, text="/", font=100, padx="30", pady="20", command=lambda:komm("/"))
komats=Button(my_frame2, text=",", font=150, padx="30", pady="20", command=lambda:btnClik("."))
ir=Button(my_frame2, text="=", padx="30", pady="80", command=ir)
c=Button(my_frame2, text="C", padx="30", pady="60", command=tiriit)

poga7.grid(row=1, column=5)
poga8.grid(row=1, column=6)
poga9.grid(row=1, column=7)

poga4.grid(row=2, column=5)
poga5.grid(row=2, column=6)
poga6.grid(row=2, column=7)

poga1.grid(row=3, column=5)
poga2.grid(row=3, column=6)
poga3.grid(row=3, column=7)

poga0.grid(row=4, column=6)
sask.grid(row=4, column=5)
atn.grid(row=4, column=7)

e.grid(row=0, column=5, columnspan=5)
ir.grid(row=1, column=8, rowspan=3)
c.grid(row=4, column=8, rowspan=5)

reiz.grid(row=5, column=5)
komats.grid(row=5, column=6)
dal.grid(row=5, column=7)

logs.mainloop()