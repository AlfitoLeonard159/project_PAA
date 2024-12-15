import random
import timeit
import matplotlib.pyplot as plt

# Fungsi untuk membuat array dengan elemen unik atau tidak unik
def generate_array(jumlah_elemen, batas_nilai, seed=42):
    random.seed(seed)
    return [random.randint(1, batas_nilai) for _ in range(jumlah_elemen)]

# Fungsi untuk menentukan apakah semua elemen dalam array unik
def cek_keunikan(array):
    return len(array) == len(set(array))

# Fungsi untuk mengukur waktu eksekusi rata-rata dan terburuk menggunakan timeit
def ukur_waktu(list_n, batas_nilai):
    waktu_terburuk = []
    waktu_rata_rata = []

    for jumlah_elemen in list_n:
        array = generate_array(jumlah_elemen, batas_nilai)

        # Waktu untuk kasus terburuk (banyak pengulangan pengecekan)
        waktu_buruk = timeit.timeit(lambda: cek_keunikan(array), number=100) / 100
        waktu_terburuk.append(waktu_buruk)

        # Waktu untuk kasus rata-rata (pengulangan lebih sedikit)
        waktu_rata = timeit.timeit(lambda: cek_keunikan(array), number=50) / 50
        waktu_rata_rata.append(waktu_rata)

    return waktu_terburuk, waktu_rata_rata

# Fungsi untuk menyimpan hasil pengujian ke file
def simpan_ke_file(nama_file, list_n, waktu_buruk, waktu_rata):
    try:
        with open(nama_file, "w") as file:
            file.write("Jumlah Elemen (n), Waktu Kasus Terburuk (s), Waktu Rata-rata (s)\n")
            for n, buruk, rata in zip(list_n, waktu_buruk, waktu_rata):
                file.write(f"{n}, {buruk:.6f}, {rata:.6f}\n")
    except IOError as error:
        print(f"Gagal menyimpan file: {error}")

# Fungsi untuk membuat grafik hasil pengujian
def buat_plot(list_n, waktu_buruk, waktu_rata, file_output):
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(list_n, waktu_buruk, label="Kasus Terburuk", marker="o", color="red")
        plt.plot(list_n, waktu_rata, label="Kasus Rata-rata", marker="o", color="blue")
        plt.title("Analisis Kompleksitas Waktu")
        plt.xlabel("Jumlah Elemen (n)")
        plt.ylabel("Waktu Eksekusi (s)")
        plt.legend()
        plt.grid()
        plt.savefig(file_output)
        plt.show()
    except Exception as error:
        print(f"Gagal membuat grafik: {error}")

if __name__ == "__main__":
    try:
        # Input tiga digit terakhir dari stambuk
        tiga_digit_akhir = int(input("Masukkan 3 digit terakhir dari stambuk Anda: "))
        batas_nilai = 250 - tiga_digit_akhir

        if batas_nilai <= 0:
            raise ValueError("Batas nilai maksimum harus lebih besar dari 0.")

        # Daftar jumlah elemen untuk pengujian
        list_n = [100, 150, 200, 250, 300, 350, 400, 500]

        # Hitung waktu untuk kasus terburuk dan rata-rata
        waktu_terburuk, waktu_rata_rata = ukur_waktu(list_n, batas_nilai)

        # Simpan hasil pengujian ke file
        simpan_ke_file("hasil_pengujian.txt", list_n, waktu_terburuk, waktu_rata_rata)

        # Buat grafik dan simpan
        buat_plot(list_n, waktu_terburuk, waktu_rata_rata, "grafik_kompleksitas_waktu.jpg")

        print("Program selesai. Silakan periksa file 'hasil_pengujian.txt' dan 'grafik_kompleksitas_waktu.jpg'.")
    except ValueError as ve:
        print(f"Kesalahan input: {ve}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
