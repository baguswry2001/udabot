import speedtest

def test_speed():
    # Membuat objek speedtest
    st = speedtest.Speedtest()

    # Melakukan pengukuran kecepatan unduh
    download_speed = st.download() / 1_000_000  # Mengkonversi ke Mbps

    # Melakukan pengukuran kecepatan unggah
    upload_speed = st.upload() / 1_000_000  # Mengkonversi ke Mbps

    return download_speed, upload_speed

if __name__ == "__main__":
    # Menjalankan tes kecepatan
    download_speed, upload_speed = test_speed()

    # Menampilkan hasil
    print(f"Kecepatan unduh: {download_speed:.2f} Mbps")
    print(f"Kecepatan unggah: {upload_speed:.2f} Mbps")
