import database

def tambah_item(nama): 
    daftar = database.baca_data() 
    daftar.append(nama)
    database.tulis_data(daftar) 
    return f" '{nama}' berhasil ditambahkan."

def semua_item(): 
    return database.baca_data()

def hapus_item(no): 
    daftar = database.baca_data() 
    if 1 <= no <= len(daftar): 
        item = daftar.pop(no - 1) 
        database.tulis_data(daftar) 
        return f" '{item}' dihapus." 
    else: 
            return " Nomor tidak valid."

def edit_item(no, nama_baru): 
    """Mengedit item pada nomor urut tertentu.""" 
    daftar = database.baca_data() 
    if 1 <= no <= len(daftar): 
        item_lama = daftar[no - 1] 
        daftar[no - 1] = nama_baru 
        database.tulis_data(daftar)
        return f" '{item_lama}' diubah menjadi '{nama_baru}'." 
    else: 
            return " Nomor tidak valid."

def cari_item(kata_kunci): 
    """Mengembalikan daftar item yang mengandung kata_kunci (case-insensitive).""" 
    daftar = database.baca_data() 
    hasil = [item for item in daftar if kata_kunci.lower() in item.lower()] 
    return hasil

def saran_bahan():
    """ Mengambil 5 resep acak dari TheMealDB dan menampilkan nama resep beserta bahan-bahannya. """
    
    import urllib.request 
    import json
    import random

    # Endpoint untuk mengambil resep acak
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    saran_list = []

    try:
        # Ambil 5 resep acak (panggil API sebanyak 5 kali)
        for _ in range(5):
            response = urllib.request.urlopen(url, timeout=5)
            data_json = response.read().decode('utf-8')
            data = json.loads(data_json)
        
            if data['meals']:
                meal = data['meals'][0]
                nama_resep = meal['strMeal']
                # Kumpulkan bahan yang tidak kosong
                bahan = []
                for i in range(1, 21):
                    ingredient = meal.get(f'strIngredient{i}')
                    measure = meal.get(f'strMeasure{i}')
                    if ingredient and ingredient.strip():
                        bahan.append(f"{measure} {ingredient}".strip())
                # Gabungkan resep dengan bahan-bahannya
                saran_list.append(f"{nama_resep} (bahan: {', '.join(bahan[:3])}...)")
        return saran_list if saran_list else ["Tidak ada saran saat ini."]

    except Exception as e:
        return [f" Gagal mengambil saran: {e}"]