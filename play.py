import os
import platform
import threading

def _play(url):
    try:
        os.system(f"mpv --no-video --quiet '{url}' > /dev/null 2>&1")
    except Exception as e:
        print(f"[!] Gagal muter musik: {e}")

def play_music(url="https://pomf2.lain.la/f/cknnu1h2.mp3"):
    # Deteksi OS
    if platform.system() in ["Linux", "Darwin", "Windows"]:
        t = threading.Thread(target=_play, args=(url,))
        t.daemon = True
        t.start()
    else:
        print("[!] Sistem lo gak support audio player.")
