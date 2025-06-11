import os

def get_folder_size(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total += os.path.getsize(fp)
    return total

maildir_path = "/home/user/Maildir"
size_bytes = get_folder_size(maildir_path)
print(f"Total Maildir size: {size_bytes / (1024*1024):.2f} MB")
