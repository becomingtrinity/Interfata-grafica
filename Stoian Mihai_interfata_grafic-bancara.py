"""
Acest proiect isi are scopul de a reprezenta o interfata grafica a unei banci,
unde clientul poate sa efectueze operatiuni de retragere si depunere monetara,
de asemenea avand posibilitatea de a se inregistra in cadrul bancii.
"""
import os
from tkinter import *
from PIL import ImageTk, Image

#interfata
master = Tk()
master.title("Sistem bancar")

#definire functii

def confirmare():
    """In aceasta functie se va crea un registru de confirmare in cazul in care clientul
    si-a introdus datele de inregistrare corect, sau in cazul in care exista deja inregistrat in cadrul bancii.
    """

    nume = temp_nume.get()
    prenume = temp_prenume.get()
    data_nasterii = temp_data_nasterii.get()
    varsta = temp_varsta.get()
    sexul = temp_sexul.get()
    parola = temp_parola.get()
    inregistrari = os.listdir()

    if nume =="" or prenume =="" or data_nasterii =="" or varsta =="" or sexul =="" or parola =="":
        return avertisment.config(fg='violet', text="Toate campurile sunt obligatorii *")

    for verificare_nume in inregistrari:
        if nume == verificare_nume:
            avertisment.config(fg="red", text="Clientul este inregistrat deja la banca noastra!")
            return
        else:
            client_nou = open(nume,"w")
            client_nou.write(nume+"\n")
            client_nou.write(prenume+"\n")
            client_nou.write(data_nasterii+"\n")
            client_nou.write(varsta+"\n")
            client_nou.write(sexul+"\n")
            client_nou.write(parola+"\n")
            client_nou.write("0")
            client_nou.close()
            avertisment.config(fg="purple", text="Clientul a fost inregistrat cu succes")

def inregistrare():
    """In aceasta functie se va crea un registru in care clientul poate sa isi introduca datele personale
    de inregistrare in cadrul bancii.
    """

    inregistrare_interfata = Toplevel(master)
    inregistrare_interfata.title("Inregistrati-va in cadrul bancii noastre!")

    #Informatii de inregistrare
    global temp_nume
    global temp_prenume
    global temp_data_nasterii
    global temp_varsta
    global temp_sexul
    global temp_parola
    global avertisment
    temp_nume = StringVar()
    temp_prenume = StringVar()
    temp_data_nasterii = StringVar()
    temp_varsta = StringVar()
    temp_sexul = StringVar()
    temp_parola = StringVar()

    #inregistrare grafica
    Label(inregistrare_interfata, text="Introduceti datele dvs:", font=("Times New Roman", 12)).grid(row=0, sticky=N,pady=10)
    Label(inregistrare_interfata, text="Nume de familie:", font=("Times New Roman", 12)).grid(row=1, sticky=W)
    Label(inregistrare_interfata, text="Prenume:", font=("Times New Roman", 12)).grid(row=3, sticky=W)
    Label(inregistrare_interfata, text="Data de nastere:", font=("Times New Roman", 12)).grid(row=5, sticky=W)
    Label(inregistrare_interfata, text="Varsta:", font=("Times New Roman", 12)).grid(row=7, sticky=W)
    Label(inregistrare_interfata, text="Sexul:", font=("Times New Roman", 12)).grid(row=9, sticky=W)
    Label(inregistrare_interfata, text="Parola de inregistrare:", font=("Times New Roman", 12)).grid(row=11, sticky=W)
    avertisment = Label(inregistrare_interfata, font=("Times New Roman", 12))
    avertisment.grid(row=15,sticky=N,pady=10)

    #Date de introducere pentru inregistrare
    Entry(inregistrare_interfata, textvariable=temp_nume).grid(row=2, column=0)
    Entry(inregistrare_interfata, textvariable=temp_prenume).grid(row=4, column=0)
    Entry(inregistrare_interfata, textvariable=temp_data_nasterii).grid(row=6, column=0)
    Entry(inregistrare_interfata, textvariable=temp_varsta).grid(row=8, column=0)
    Entry(inregistrare_interfata, textvariable=temp_sexul).grid(row=10, column=0)
    Entry(inregistrare_interfata, textvariable=temp_parola,show="*").grid(row=12, column=0)

    #confirmare
    Button(inregistrare_interfata, text="Inregistrare", command=confirmare, font=("Times New Roman",12)).grid(row=13,sticky=N,pady=10)

def sesiune_conectare():
    """
    Aceasta functie va determina aparitia unei interfete introductive de salutare a utilizatorului
    in momentul in care pe baza datelor introduse corect in cadrul conectarii acesta se va conecta pentru a
    vedea informatiile sale in calitate de client al bancii, insa de asemenea, i se va introduce si posibilitatea
    de a gestiona operatiuniile de retragere si depunere din sold-ul sau disponibil pe care il are la banca.
    """

    global logare_utilizator
    inregistrari = os.listdir()
    logare_utilizator = temp_logare_utilizator.get()
    logare_parola = temp_logare_parola.get()

    for nume in inregistrari:
        if nume == logare_utilizator:
            fisa = open(nume,"r")
            date_fisier = fisa.read()
            date_fisier = date_fisier.split('\n')
            parola = date_fisier[5]

            #Interfata pentru contul clientului

            if logare_parola == parola:
                ecran_logare.destroy()
                interfata_cont = Toplevel(master)
                interfata_cont.title('Interfata')

                #Prezentare
                Label(interfata_cont, text="Interfata contului vostru bancar", font=("Times New Roman", 12)).grid(row=0, sticky=N, pady=10)
                Label(interfata_cont, text="Bine ai venit"+" "+logare_utilizator+ "!", font=("Times New Roman", 12)).grid(row=1, sticky=N,pady=5)

                #Buton
                Button(interfata_cont, text="Detaliile personale ale clientului", font=("Times New Roman", 12), width=30, command=informatii_client).grid(row=2, sticky=N, pady=10)
                Button(interfata_cont, text="Realizati o depozitare!", font=("Times New Roman", 12), width=30, command=depozitare).grid(row=3,sticky=N,pady=10)
                Button(interfata_cont, text="Realizati o retragere!", font=("Times New Roman", 12), width=30, command=retragere).grid(row=4,sticky=N,pady=10)
                Label(interfata_cont).grid(row=5, sticky=N, pady=10)
                return
            else:
                logare_avertisment.config(fg="red", text="Parola introdusa este incorecta!")
                return
    logare_avertisment.config(fg="red", text="Nu s-a regasit niciun cont!")

def depozitare():
    """
    In aceasta functie vom crea pe baza datelor introduse in cadrul inregistrarii clientului
    o interfata in care clientul sa poata sa depuna o suma si aceasta sa i se afiseze in cadrul sold-ului disponibil.
    """

    #Date de depozitare
    global sold
    global avertisment_depozitare
    global balanta_sold

    sold = StringVar()
    continut = open(logare_utilizator, "r")
    data_continut = continut.read()
    detalii_utilizator = data_continut.split("\n")
    info_balanta = detalii_utilizator[6]

    #Interfata_depozit
    interfata_depozitare = Toplevel(master)
    interfata_depozitare.title("Depozit bancar")

    #Etichetare
    Label(interfata_depozitare, text="Depozitul monetar: LEI", font=("Times New Roman", 12)).grid(row=0, sticky=N, pady=10)
    balanta_sold = Label(interfata_depozitare, text="Depozitul monetar actual: LEI"+info_balanta, font=("Times New Roman", 12))
    balanta_sold.grid(row=1, sticky=W)
    Label(interfata_depozitare, text="Suma dorita pentru depozitare:", font=("Times New Roman", 12)).grid(row=2, sticky=W)
    avertisment_depozitare = Label(interfata_depozitare, font=("Times New Roman", 12))
    avertisment_depozitare.grid(row=4, sticky=N, pady=5)

    #Introduceri
    Entry(interfata_depozitare, textvariable= sold).grid(row=2, column=1)

    #Buton
    Button(interfata_depozitare, text="Finalizare proces de depozitare", font=("Times New Roman", 12), command=proces_depozitare).grid(row=3, sticky=W, pady=5)

def proces_depozitare():
    """
    Aceasta functie ne va returna cateva avertismente, fie de confirmare in cazul in care
    depunerea s-a realizat cu succes sau daca nu este specificata corect suma ce este dorita a fi depusa
    sa ne returneze un mic avertisment care sa ne reaminteasca de procedura corecta de depunere.
    """

    if sold.get() == "":
        avertisment_depozitare.config(text="O suma de depunere este necesara!", fg="red")
        return
    if float(sold.get()) <=0:
        avertisment_depozitare.config(text="Nu se poate efectua depunerea!", fg="red")
        return

    continut = open(logare_utilizator, "r+")
    date_continut = continut.read()
    informatii = date_continut.split("\n")
    sold_initial = informatii[6]
    sold_actual = sold_initial
    sold_actual = float(sold_actual) + float(sold.get())
    date_continut = date_continut.replace(sold_initial, str(sold_actual))
    continut.seek(0)
    continut.truncate(0)
    continut.write(date_continut)
    continut.close()

    balanta_sold.config(text="Suma dumneavoastra de depunere: LEI"+str(sold_actual), fg="green")
    avertisment_depozitare.config(text="Sold-ul a fost actualizat cu succes!", fg="green")

def retragere():
    """
       In aceasta functie vom crea pe baza datelor introduse in cadrul inregistrarii clientului la banca
       o interfata specifica de retragere in care clientul sa poata sa retraga o anumita suma din cadrul sold-ului bancar disponibil.
       """

    global retragere_sold
    global avertisment_retragere
    global balanta_sold

    retragere_sold = StringVar()
    continut = open(logare_utilizator, "r")
    data_continut = continut.read()
    detalii_utilizator = data_continut.split("\n")
    info_balanta = detalii_utilizator[6]

    #Interfata_retragere

    interfata_retragere = Toplevel(master)
    interfata_retragere.title("Retragere bancara")

    #Etichetare

    Label(interfata_retragere, text="Retragere monetara: LEI", font=("Times New Roman", 12)).grid(row=0, sticky=N, pady=10)
    balanta_sold = Label(interfata_retragere, text="Depozitul monetar actual: LEI"+info_balanta, font=("Times New Roman", 12))
    balanta_sold.grid(row=1, sticky=W)
    Label(interfata_retragere, text="Suma dorita pentru retragere:", font=("Times New Roman", 12)).grid(row=2, sticky=W)
    avertisment_retragere = Label(interfata_retragere, font=("Times New Roman", 12))
    avertisment_retragere.grid(row=4, sticky=N, pady=5)

    #Introduceri

    Entry(interfata_retragere, textvariable=retragere_sold).grid(row=2, column=1)

    #Buton

    Button(interfata_retragere, text="Finalizare proces de retragere", font=("Times New Roman", 12), command=confirmare_retragere).grid(row=3, sticky=W, pady=5)

def confirmare_retragere():
    """
      Aceasta functie ne va returna cateva avertismente, fie de confirmare in cazul in care
      procesul de retragere s-a realizat cu succes, sau daca nu este specificata corect suma ce este dorita a fi retrasa,
      sa ne fie returnat un avertisment specific care sa ne mentioneze procedura corecta de retragere.
      """

    if retragere_sold.get() == "":
        avertisment_retragere.config(text="O suma de retragere este necesara!", fg="red")
        return
    if float(retragere_sold.get()) <= 0:
        avertisment_retragere.config(text="Nu se poate efectua retragerea!", fg="red")
        return
    continut = open(logare_utilizator, "r+")
    date_continut = continut.read()
    informatii = date_continut.split("\n")
    sold_initial = informatii[6]

    if float(retragere_sold.get()) > float(sold_initial):
        avertisment_retragere.config(text="Insuficiente fonduri pentru realizarea retragerii!", fg="red")
        return

    sold_actual = sold_initial
    sold_actual = float(sold_actual) - float(retragere_sold.get())
    date_continut = date_continut.replace(sold_initial, str(sold_actual))
    continut.seek(0)
    continut.truncate(0)
    continut.write(date_continut)
    continut.close()

    balanta_sold.config(text="Suma dumneavoastra de retragere: LEI"+str(sold_actual), fg="green")
    avertisment_retragere.config(text="Sold-ul a fost actualizat cu succes!", fg="green")

def informatii_client():
    """
    Aceasta functie ne va returna in momentul conectarii cu succes o interfata pentru client unde
    acesta va avea o transparenta a datelor cu caracter personal inregistrate in cadrul bancii.
    """

    informatii = open(logare_utilizator, 'r')
    date_informatii = informatii.read()
    detalii_utilizator = date_informatii.split('\n')
    detalii_nume = detalii_utilizator[0]
    detalii_prenume = detalii_utilizator[1]
    detalii_data_nasterii = detalii_utilizator[2]
    detalii_varsta = detalii_utilizator[3]
    detalii_sexul = detalii_utilizator[4]
    detalii_sold_bancar = detalii_utilizator[6]

    #Afisare detalii personale ale clientului

    afisaj_detalii_personale = Toplevel(master)
    afisaj_detalii_personale.title('Detalii personale ale clientului:')

    #Etichete

    Label(afisaj_detalii_personale, text="Nume client:"+detalii_nume, font=("Times New Roman", 12)).grid(row=0, sticky=W, pady=10)
    Label(afisaj_detalii_personale, text="Prenume client:"+detalii_prenume, font=("Times New Roman", 12)).grid(row=1, sticky=W, pady=10)
    Label(afisaj_detalii_personale, text="Data nasterii:"+detalii_data_nasterii, font=("Times New Roman", 12)).grid(row=2, sticky=W, pady=10)
    Label(afisaj_detalii_personale, text="Varsta:"+detalii_varsta, font=("Times New Roman", 12)).grid(row=3, sticky=W, pady=10)
    Label(afisaj_detalii_personale, text="Sexul:"+detalii_sexul, font=("Times New Roman", 12)).grid(row=4, sticky=W, pady=10)
    Label(afisaj_detalii_personale, text="Sold bancar : LEI "+detalii_sold_bancar, font=("Times New Roman", 12)).grid(row=5, sticky=W, pady=10)

def conectare():
    """
    Se va crea o functie care v-a prelua datele de inregistrare specifice de nume si parola
    in scopul conectarii clientului la banca de unde ulterior se vor
    efectua operatiunile de depunere si retragere monetara de catre acesta.
    """

    #Date de conectare

    global temp_logare_utilizator
    global temp_logare_parola
    global logare_avertisment
    global ecran_logare
    temp_logare_utilizator = StringVar()
    temp_logare_parola = StringVar()

    #interfata

    ecran_logare = Toplevel(master)
    ecran_logare.title("Conectare!")

    #eticheta

    Label(ecran_logare, text="Conectati-va la contul dumneavoastra!", font=("Times New Roman", 12)).grid(row=0, sticky=N, pady=10)
    Label(ecran_logare, text="Utilizator", font=("Times New Roman", 12)).grid(row=1,sticky=W)
    Label(ecran_logare, text="Parola", font=("Times New Roman", 12)).grid(row=2,sticky=W)
    logare_avertisment = Label(ecran_logare, font=("Times New Roman", 12))
    logare_avertisment.grid(row=4, sticky=N)

    #introduceri

    Entry(ecran_logare, textvariable=temp_logare_utilizator).grid(row=1, column=0, padx=1)
    Entry(ecran_logare, textvariable=temp_logare_parola, show="*").grid(row=2, column=0, padx=1)

    #interactiuni
    Button(ecran_logare, text="Conectare", command=sesiune_conectare, width=15, font=("Times New Roman", 12)).grid(row=5, sticky=W, padx=5)

#importare artistica

imagine = Image.open("banca.jpg")
imagine = imagine.resize((150, 150))
imagine = ImageTk.PhotoImage(imagine)

#eticheta

Label(master, text="Banca Nationala Meta", font=('Times New Roman', 16)).grid(row=0,sticky=N,pady=10)
Label(master, text="O banca in care poti investii pentru viitorul confortului vietii tale!", font=('Times New Roman', 12)).grid(row=1,sticky=N)
Label(master, image=imagine).grid(row=2, sticky=N, pady=15)

#puncte de acces

Button(master, text="Inregistrare", font=('Times New Roman', 12),width=20,command=inregistrare).grid(row=3,sticky=N)
Button(master, text="Conectare", font=('Times New Roman', 12),width=20,command=conectare).grid(row=4,sticky=N,pady=10)
