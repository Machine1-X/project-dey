import module_artematika_simpelnya


while True:
    def main():
        a = int(float(input("masukan angka pertama: ")))
        b = int(float(input("masukan angka ke dua: "))) 
        print(module_artematika_simpelnya.bagi(a,b))
        print(module_artematika_simpelnya.kali(a,b))
        print (module_artematika_simpelnya.kurang(a,b))
        print (module_artematika_simpelnya.tambah(a,b))
    main()