from cryptography.fernet import Fernet
key = "nSKofJjmrBpNqoU0SrhsE6PU1M7T8UpZXHFxkPb3ovs="
system_information_e = "e_system.txt"
clipboard_information_e = "e_clipboard.txt"
keys_information_e = "e_keys_logged.txt"

encrypted_files = [system_information_e, clipboard_information_e, keys_information_e]
count = 0

for decrypting_file in encrypted_files:
    with open("C:\\Users\\hardi\\Downloads\\noname (1)", 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(encrypted_files[count], 'wb') as f:
        f.write(decrypted)

    count += 1
