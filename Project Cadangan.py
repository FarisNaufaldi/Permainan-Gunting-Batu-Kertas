def permainan():
    skor_pemain_pertama = 0
    skor_pemain_kedua = 0
    x = input("Sebagai Pemain Satu Silahkan anda memilih nama untuk digunakan dalam permainan ini = ")
    y = input("Sebagai Pemain Kedua Silahkan anda memilih nama untuk digunakan dalam permainan ini = ")
    while skor_pemain_pertama < 4 and skor_pemain_kedua < 4:
        Pemain_Pertama = input(f"{x}, Pilihlah Gunting atau batu atau kertas, tulis hanya dengan g/b/k = ").lower()
        Pemain_Kedua = input(f"{y}, Pilihlah Gunting atau batu atau kertas, tulis hanya dengan g/b/k = ").lower()
        try:
            if (Pemain_Pertama == "g" and Pemain_Kedua == "k") or \
               (Pemain_Pertama == "b" and Pemain_Kedua == "g") or \
               (Pemain_Pertama == "k" and Pemain_Kedua == "b"):
                skor_pemain_pertama += 1
                print(f"Skor sementara adalah {x} memegang {skor_pemain_pertama} point dan {y} memegang {skor_pemain_kedua} point")
            elif (Pemain_Pertama == "g" and Pemain_Kedua == "g") or \
                 (Pemain_Pertama == "b" and Pemain_Kedua == "b") or \
                 (Pemain_Pertama == "k" and Pemain_Kedua == "k"):
                skor_pemain_pertama += 1
                skor_pemain_kedua += 1
                print(f"Skor sementara adalah {x} memegang {skor_pemain_pertama} point dan {y} memegang {skor_pemain_kedua} point")
            elif (Pemain_Pertama == "k" and Pemain_Kedua == "g") or \
                 (Pemain_Pertama == "g" and Pemain_Kedua == "b") or \
                 (Pemain_Pertama == "b" and Pemain_Kedua == "k"):
                skor_pemain_kedua +=1
                print(f"Skor sementara adalah {x} memegang {skor_pemain_pertama} point dan {y} memegang {skor_pemain_kedua} point")
            else:
                print("Hmmm sepertinya salah satu dari anda salah memasukkan input silahkan mencoba lagi")
            

        except:
            Pemain_Pertama = input(f"{x}, Pilihlah Gunting atau batu atau kertas, tulis hanya dengan g/b/k = ").lower()
            Pemain_Kedua = input(f"{y}, Pilihlah Gunting atau batu atau kertas, tulis hanya dengan g/b/k = ").lower()
    if skor_pemain_pertama == 4 and skor_pemain_kedua < 4:
        print(f"Pemenang dari permainan ini adalah {x}, selamat untuk {x} karena telah memenangkan permainan ini")
    elif skor_pemain_kedua == 4 and skor_pemain_pertama <4:
        print(f"Pemenang dari permainan ini adalah {y}, selamat untuk {y} telah memenangkan permainan ini")
    else:
        print("Maaf permainan berakhir seri")                
permainan()                
                