list_buku = [
    "citadel book",
    "paladin book",
    "ancient book"
]

def menu():
    print("1. cari buku")
    print("2. tambah buku")
    print("3. pinjam buku")
    print("4. kembalikan buku")
    input_user = int(input("masukan pilihan: "))
    if input_user == 1:
        cari_buku()
    elif input_user == 2:
        tambah_buku()
    elif input_user == 3:
        pinjam_buku()
    elif input_user == 4:
        kembalikan_buku()
def cari_buku():
    input_user1 = input("masukan buku yang ingin dicari: ")
    if input_user1 in list_buku:
        print("buku ditemukan")
    else:
        print("buku tidak ditemukan")
    
def tambah_buku():
        input_user2 = input("masukan buku yang ingin ditambahkan: ")
        list_buku.append(input_user2)
        print(list_buku,"buku berhasil ditambahkan")
    
def pinjam_buku():
        input_user3 = input("masukan buku yang ingin dipinjam: ")
        if input_user3 in list_buku:
            list_buku.remove(input_user3)
            print(list_buku,"buku berhasil dipinjam")
        else:
            print("buku tidak di temukan")
    
def kembalikan_buku():
        input_user4 = input("masukan buku yang ingin dikembalikan: ")
        list_buku.append(input_user4)
        list_buku.sort()
        print(list_buku,"buku berhasil di kembalikan")  




while True:
    menu()
    break