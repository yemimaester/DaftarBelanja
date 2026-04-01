import urllib.request
import json

def test_api():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        print("Menguji Koneksi API...")
        response = urllib.request.urlopen(url, timeout=5)
        data_json = response.read().decode('utf-8')
        data = json.loads(data_json)
        print("Berhasil Mengambil Data dari API! ")
        print("Menampilkan 3 Judul Pertama:\n ")
        for i, post in enumerate(data[:3], start=1):
            print(f"{i}.{post['title']}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}-{e.reason}")
    except urllib.error.URLError as e:
        print(f" URL Error: {e.reason}")
    except Exception as e:
        print(f" Error tak terduga: {e}")
            
if __name__ == "__main__":
    test_api()