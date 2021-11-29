"""
Aplikasi deteksi gempa terkini
Modularisasi dengan function
"""


def ekstraksi_data():
    """
    Tanggal : 29 November 2021, 22:25:44 WIB
    Magnitudo : 4.6
    Kedalaman : 16 km
    Lokasi : LS=1.25 BT=99.79
    Pusat Gempa : Pusat gempa berada di laut 72 km Barat Daya Padang
    Dirasakan: Dirasakan (Skala MMI): II-III Padang, II Pariaman, I Padang Panjang
    """

    hasil = dict()
    hasil['tanggal'] = '29 November 2021'
    hasil['waktu'] = '22:25:44 WIB'
    hasil['magnitudo'] = 4.6
    hasil['kedalaman'] = '16 km'
    hasil['lokasi'] = {'ls': 1.25, 'bt': 99.79}
    hasil['pusat'] = 'Pusat gempa berada di laut 72 km Barat Daya Padang'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II-III Padang, II Pariaman, I Padang Panjang'

    return  hasil


def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi LS: {result['lokasi']['ls']} BT: {result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print("Aplikasi utama")
    result = ekstraksi_data()
    tampilkan_data(result)