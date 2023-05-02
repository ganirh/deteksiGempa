"""
Aplikasi deteksi gempa terkini
"""

def ekstrasi_data():
    """
    Tanggal     : 01 Mei 2023
    Waktu       : 10:20:12 WIB
    Magnitude   : 3.8
    Kedalaman   : 10 km
    Lokasi      : LS = 4.01 BT = 136.07
    Episentrum  : Pusat gempa berada di darat 12 km Timur Laut Dogiyai
    Testimoni   : Dirasakan (Skala MMI): II Dogiyai
    :return:
    """

    hasil = dict()
    hasil['tanggal'] = '01 Mei 2023'
    hasil['waktu'] = '10:20:12 WIB'
    hasil['magnitude'] = 3.8
    hasil['kedalaman'] = '10 Km'
    hasil['lokasi'] = {'ls' : 4.01, 'bt' : 136.07}
    hasil['episentrum'] = 'Pusat gempa berada di darat 12 km Timur Laut Dogiyai'

    return hasil

def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Magnitude {result['magnitude']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS = {result['lokasi']['ls']}, BT = {result['lokasi']['bt']}")
    print(f"Episentrum {result['episentrum']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
    result  = ekstrasi_data()
    tampilkan_data(result)