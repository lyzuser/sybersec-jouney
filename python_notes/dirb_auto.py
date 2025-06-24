# dirb_auto.py
# 目录爆破实战脚本【加入进度条版本】

import requests
import threading
from tqdm import tqdm  # 用于显示进度条

# 基本配置
target_url = "http://fakebank.thm"
wordlist_file = "./wordlist.txt"  # 实际爆破词表
threads = 10  # 并发线程数

# 结果存储
found_urls = []
lock = threading.Lock()

def dirb_worker(paths, thread_id):
    # 每个线程使用不同的 tqdm 进度条 position
    for path in tqdm(paths, desc=f"Thread-{thread_id}", position=thread_id):
        url = f"{target_url}/{path.strip()}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code in [200, 301, 302]:
                with lock:
                    print(f"[+] Found: {url} (Status: {response.status_code})")
                    found_urls.append((url, response.status_code))
        except requests.RequestException:
            pass

def run_dirb():
    with open(wordlist_file, "r") as f:
        lines = f.readlines()

    chunk_size = len(lines) // threads
    thread_list = []

    for i in range(threads):
        chunk = lines[i*chunk_size : (i+1)*chunk_size] if i < threads - 1 else lines[i*chunk_size:]
        t = threading.Thread(target=dirb_worker, args=(chunk, i))  # 添加线程编号
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    # 结果导出
    with open("dirb_result.txt", "w") as f:
        for url, code in found_urls:
            f.write(f"{url} -> {code}\n")

if __name__ == "__main__":
    print("[*] Starting directory brute-force with progress bar...")
    run_dirb()
    print("[*] Scan complete. Results saved to dirb_result.txt")
