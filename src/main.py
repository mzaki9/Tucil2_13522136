from dnq import *
from bruteforce import *




def main():
    while(True):
       
        print("Program Kurva Bezier")
        print("Pilih metode:")
        print("1. Divide and Conquer")
        print("2. Brute Force")
        print("3. Keluar")
        
        while True:
            try:
                choice = int(input("Masukkan pilihan: "))
                break
            except ValueError:
                print("Invalid input.")
        
        if choice == 1:
            divideandConquer()
        elif choice == 2:
            bruteForce()
        elif choice == 3:
            print("Thank You!")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()