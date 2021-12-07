
import requests
from bs4 import BeautifulSoup

def ekstraksi_data():
    """
    Tanggal : 29 November 2021, 22:25:44 WIB
    Magnitudo : 4.6
    Kedalaman : 16 km
    Lokasi : LS=1.25 BT=99.79
    Pusat Gempa : Pusat gempa berada di laut 72 km Barat Daya Padang
    Dirasakan: Dirasakan (Skala MMI): II-III Padang, II Pariaman, I Padang Panjang
    """
    
    try :
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        # date time extract
        dateTime = soup.find('span', {'class':'waktu'})
        dateTime = dateTime.text.split(', ')
        tanggal = dateTime[0]
        waktu = dateTime[1]
        
        #  magnitudo extract
        result= soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        dirasakan = None
        lokasi = None
        
        for res in result:
            # print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
                
            i += 1
        
        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['pusat'] = lokasi
        hasil['dirasakan'] = dirasakan
        return  hasil
    else :
        return None


def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menemukan data gempa terkini")
        return
    
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi LS: {result['koordinat']['ls']} BT: {result['koordinat']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")
