import datetime

LOG_FILE = "aplikasi.log"

def tulis_log(pesan): 
    """Menulis pesan log dengan timestamp ke file.""" 
    with open(LOG_FILE, "a") as f: 
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{waktu}] {pesan}\n")