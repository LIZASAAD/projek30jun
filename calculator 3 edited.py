# Calculator

import time



# operasi tambah
def addition ():

    print("\n - Addition / Tambah - ")
    n = float(input("Masukkan Nombor: "))
    t = 0 #Total number enter
    ans = 0
    while n != 0:
        ans = ans + n
        t+=1
        n = float(input("Masukkan nombor seterusnya (Tekan 0 untuk berhenti): "))
    return [ans,t]
    
# operasi tolak
def subtraction ():

    print("\n - subtraction / Tolak -");
    n = float(input("Masukkan nombor: "))
    t = 0 ##Jumlah nombor dimasukkan
    ans = n
 
    while n != 0:
        t+=1
        n = float(input("Masukkan nombor seterusnya (0 untuk kira): "))
        ans = ans-n
    return [ans,t]

# operasi darab
def multiplication ():

    print("\n - Multiplication/ Darab -")
    n = float(input("Masukkan Nombor: "))
    t = 0 #Total number enter
    ans = 1
    while n != 0:
        ans = ans * n
        t+=1
        n = float(input("Masukkan nombor seterusnya (Tekan 0 to berhenti): "))
    return [ans,t]

# operasi bahagi
def division():
    print(" Division / Bahagi")
    n = float(input("Masukkan nombor: "))
    t = 0 #Jumlah nombor dimasukkan
    ans = n
    while n != 0:
        t+=1
        n = float(input("Masukkan nombor seterusnya (0 untuk kira): "))
        if n!=0:
            ans = ans /n
    return [ans,t]
    

# main...

while True:

    list = []
    from datetime import date # tarikh
    today = date.today()
    print("             Today's date:", today)
    
    print(" \n                  CALCULATOR")
    print("                JOM KITA MENGIRA")
    print(" ###############################################")
    print(" \n Tekan 'a' untuk operasi Addition / Tambah")
    print(" Tekan 's' untuk operasi  Substraction / Tolak")
    print(" Tekan 'm' untuk operasi Multiplication / Darab")
    print(" Tekan 'd' untuk operasi Division / Bahagi")
    print(" Tekan 'q' untuk quit / keluar ")
    print(" \n ##############################################")

    c = input("\nSILA PILIH JENIS  OPERASI :")
    if c != 'q' and c!="Q":

        if c == 'a' or c=="A":
            list = addition() # panggil function
            print("\nHasil Tambah = ", list[0], " Nombor yang dimasukkan ",list[1])
            print("____________________________________________________________")
            time.sleep(6)

        elif c == 's' or c=="S":
            list= subtraction()# panggil function
            print("\nHasil Tolak = ", list[0], " Nombor yang dimasukkan ",list[1])
            print("__________________________________________________")
            time.sleep(6)
            
        elif c == 'm' or c=="M":
            list = multiplication() # panggil function
            print("\nHasil Darab = ", list[0], " Nombor yang dimasukkan ",list[1])
            print("__________________________________________________")
            time.sleep(6)
            
        elif c == 'd'or c=="D":
            list = division() # panggil function
            
            if list[1]==1:
                    print ("Operasi bahagi tidak dapat diteruskan kerana nombor kedua tidak dimasukkan. Anda memasukkan 0 untuk mula mengira")
            else:
                print("----------------------------------------")
                print("\nJumlah nombor yang dimasukkan: ",list[1],"\nHasil bahagi = ", list[0])
                print("----------------------------------------")
                time.sleep(6)

    else:
        print(" -TERIMA KASIH -")
        print(" -   TAMAT -   ")
        break