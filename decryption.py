import pyAesCrypt
import os

# funkcja deszyfrowanie plików
def decryption(file, password):

    #rozmiar buforu
    buffer_size = 512 * 1024

    #wywołujemy metode deszyfrowania
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size,
    )

    #wyświetlami komunikat o imieniu deszyfrowanego pliku
    print("[Plik ' " + str(os.path.splitext(file)[0]) + "' deszyfrowan")

    #usuwamy początkowy plik
    os.remove(file)

# funkcyja skanowania katalogów
def walking_by_dirs(dir, password):
    #sprawdzamy wszystkie podkatalogi w zaznaczonym katalogu
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        #jeżeli znajdziemy plik - deszyfrujemy
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        #jeżeli nachodzimy katalog - powtarzamy cykl w poszukiwaniu plików
        else:
            walking_by_dirs(path,password)

password = input("Hasło: ")
walking_by_dirs("C:/Users/Hladkyi Dmytro/Desktop/PYTHON", password)