# TODO: Program untuk mencetak bilangan ganjil dari 1 hingga 15
odd_numbers = []
for i in range(1, 16, 2):  # Mulai dari 1, sampai 15, step 2
    odd_numbers.append(i)

print("Bilangan ganjil dari 1 hingga 15:", odd_numbers)

# TODO: Program menghitung jumlah huruf vokal
word = input("Masukkan kata: ").lower()

vowels = "aiueo"  # Diperbaiki dari "aimeo" menjadi "aiueo"
count = 0

for char in word:
    if char in vowels:
        count += 1

print("Jumlah huruf vokal:", count)