#membuat kalkulator sederhana
def tambah(x, y):
    return x + y
def kurang(x, y):
    return x - y
def kali(x, y):
    return x * y
def bagi(x, y):
    return x / y

print("Pilih operasi:")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")

choice = input("Masukkan pilihan(1/2/3/4): ")

num1 = float(input("Masukkan bilangan pertama: "))
num2 = float(input("Masukkan bilangan kedua: "))
if choice == '1':
    print(num1,"+",num2,"=", tambah(num1,num2))