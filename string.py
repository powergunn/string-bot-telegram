#!/usr/bin/python3
# PowerGunn - String Telegram

import os
from time import sleep

POWERGUNN = """
  _____                        _____                   
 |  __ \                      / ____|                  
 | |__) |____      _____ _ __| |  __ _   _ _ __  _ __  
 |  ___/ _ \ \ /\ / / _ \ '__| | |_ | | | | '_ \| '_ \ 
 | |  | (_) \ V  V /  __/ |  | |__| | |_| | | | | | | |
 |_|   \___/ \_/\_/ \___|_|   \_____|\__,_|_| |_|_| |_|
"""


def spinner(task):
    if task == "tele":
        print("Memeriksa apakah Telethon sudah terinstal...")
    else:
        print("Memeriksa apakah Pyrogram sudah terinstal...")
    for _ in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)


def clear_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        # untuk platform Windows
        os.system("cls")


def get_api_id_and_hash():
    print(
        "Dapatkan API ID dan API HASH Anda dari my.telegram.org atau @ScrapperRoBot untuk melanjutkan.\n\n",
    )
    try:
        API_ID = int(input("Masukkan API ID Anda: "))
    except ValueError:
        print("API ID harus berupa bilangan bulat.\nKeluar...")
        exit(0)
    API_HASH = input("Masukkan API HASH Anda: ")
    return API_ID, API_HASH


def telethon_session():
    try:
        spinner("tele")
        import telethon
        x = "\bMenemukan instalasi Telethon yang sudah ada...\nBerhasil diimpor.\n\n"
    except ImportError:
        print("Menginstal Telethon...")
        os.system("pip uninstall telethon -y && pip install -U telethon")

        x = "\bSelesai. Telethon terinstal dan diimpor."
    clear_screen()
    print(POWERGUNN)
    print(x)

    # mengimpor modul

    from telethon.errors.rpcerrorlist import (
        ApiIdInvalidError,
        PhoneNumberInvalidError,
        UserIsBotError,
    )
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

    API_ID, API_HASH = get_api_id_and_hash()

    # masuk
    try:
        with TelegramClient(StringSession(), API_ID, API_HASH) as powergunn:
            print("Menghasilkan string session untuk •POWERGUNN•")
            try:
                powergunn.send_message(
                    "me",
                    f"**POWERGUNN** `SESSION`:\n\n`{powergunn.session.save()}`\n\n**Jangan bagikan ini di mana pun!**",
                )
                print(
                    "SESSION Anda telah dihasilkan. Periksa pesan tersimpan di Telegram Anda!"
                )
                return
            except UserIsBotError:
                print("Anda mencoba menghasilkan Session untuk Akun Bot Anda?")
                print("Inilah yang ada!\n{powergunn.session.save()}\n\n")
                print("CATATAN: Anda tidak dapat menggunakan itu sebagai Session Pengguna.")
    except ApiIdInvalidError:
        print(
            "Kombinasi API ID/API HASH Anda tidak valid. Harap periksa kembali.\nKeluar..."
        )
        exit(0)
    except ValueError:
        print("API HASH tidak boleh kosong!\nKeluar...")
        exit(0)
    except PhoneNumberInvalidError:
        print("Nomor telepon tidak valid!\nKeluar...")
        exit(0)
    except Exception as er:
        print("Error yang tidak diharapkan terjadi saat membuat sesi")
        print(er)
        print("Jika Anda menganggapnya sebagai Bug, Laporkan ke @UltroidSupportChat.\n\n")


def pyro_session():
    try:
        spinner("pyro")
        from pyrogram import Client

        x = "\bMenemukan instalasi Pyrogram yang sudah ada...\nBerhasil diimpor.\n\n"
    except BaseException:
        print("Menginstal Pyrogram...")
        os.system("pip install pyrogram tgcrypto")
        x = "\bSelesai. Pyrogram terinstal dan diimpor."
        from pyrogram import Client

    clear_screen()
    print(POWERGUNN)
    print(x)

    # menghasilkan sesi
    API_ID, API_HASH = get_api_id_and_hash()
    print("Masukkan nomor telepon saat diminta.\n\n")
    try:
        with Client(name="powergunn", api_id=API_ID, api_hash=API_HASH, in_memory=True) as pyro:
            ss = pyro.export_session_string()
            pyro.send_message(
                "me",
                f"`{ss}`\n\nDi atas adalah String Session Pyrogram Anda untuk @PowerGunn. **JANGAN BAGIKAN ini.**",
            )
            print("Sesi telah dikirim ke pesan tersimpan Anda!")
            exit(0)
    except Exception as er:
        print("Kesalahan yang tidak terduga terjadi saat membuat sesi, pastikan untuk memvalidasi input Anda.")
        print(er)


def main():
    clear_screen()
    print(POWERGUNN)
    try:
        type_of_ss = int(
            input(
                "\nPowerGunn mendukung sesi Telethon dan Pyrogram.\n\nSesi mana yang ingin Anda hasilkan?\n1. Sesi Telethon.\n2. Sesi Pyrogram.\n\nMasukkan pilihan:  "
            )
        )
    except Exception as e:
        print(e)
        exit(0)
    if type_of_ss == 1:
        telethon_session()
    elif type_of_ss == 2:
        pyro_session()
    else:
        print("Pilihan tidak valid.")
    x = input("Jalankan lagi? (Y/n)")
    if x.lower() in ["y", "yes"]:
        main()
    else:
        exit(0)


if __name__ == "__main__":
    main()
