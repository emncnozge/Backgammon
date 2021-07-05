import os.path
import random

table = {
    "A1": "5Y",
    "B1": "--",
    "C1": "--",
    "D1": "--",
    "E1": "3X",
    "F1": "--",
    "G1": "5X",
    "H1": "--",
    "I1": "--",
    "J1": "--",
    "K1": "--",
    "L1": "2Y",
    "A2": "5X",
    "B2": "--",
    "C2": "--",
    "D2": "--",
    "E2": "3Y",
    "F2": "--",
    "G2": "5Y",
    "H2": "--",
    "I2": "--",
    "J2": "--",
    "K2": "--",
    "L2": "2X",
}
xbroken = 0
ybroken = 0
dice1 = 0
dice2 = 0
turn = ""
xflake = 0
yflake = 0
dices = []


def rollDice():
    global dice1
    global dice2
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)


def printTable():
    global turn
    print(
        "  |----A----|----B----|----C----|----D----|----E----|----F----||----G----|----H----|----I----|----J----|----K----|----L----|")
    print("1 |    " + table["A1"] + "   " + "|    " + table["B1"] + "   " + "|    " + table["C1"] + "   " + "|    " +
          table["D1"] + "   " + "|    " + table["E1"] +
          "   " + "|    " + table["F1"] + "   " + "|"
          + "|    " + table["G1"] + "   " + "|    " + table["H1"] + "   " + "|    " + table["I1"] + "   " + "|    " +
          table["J1"] + "   " + "|    " + table["K1"] + "   " + "|    " + table["L1"] + "   " + "| 1")
    print(
        "  |---------|---------|---------|---------|---------|---------||---------|---------|---------|---------|---------|---------|")
    print("  |---------|---------|---------|---------|Brkn.X: " + str(xbroken) + "|Dice 1: " + str(
        dice1) + "||Dice 2: " + str(dice2) + "|Brkn.Y: " + str(
        ybroken) + "| Turn: " + turn + " |---------|---------|---------|")
    print(
        "  |---------|---------|---------|---------|---------|---------||---------|---------|---------|---------|---------|---------|")
    print("2 |    " + table["A2"] + "   " + "|    " + table["B2"] + "   " + "|    " + table["C2"] + "   " + "|    " +
          table["D2"] + "   " + "|    " + table["E2"] +
          "   " + "|    " + table["F2"] + "   " + "|"
          + "|    " + table["G2"] + "   " + "|    " + table["H2"] + "   " + "|    " + table["I2"] + "   " + "|    " +
          table["J2"] + "   " + "|    " + table["K2"] + "   " + "|    " + table["L2"] + "   " + "| 2")
    print(
        "  |---------|---------|---------|---------|---------|---------||---------|---------|---------|---------|---------|---------|")


def printLog():
    f = open("Log.dat", "a")
    f.write(turn + " " + str(dice1) + " " + str(dice2) + "\n")
    f.close()


def printToFile():
    global turn
    f = open("Table.dat", "w")
    f.write(
        "  |----A----|----B----|----C----|----D----|----E----|----F----||----G----|----H----|----I----|----J----|----K----|----L----|\n"
        "1 |    " + table["A1"] + "   " + "|    " + table["B1"] + "   " + "|    " + table["C1"] + "   " + "|    " +
        table["D1"] + "   " + "|    " + table["E1"] +
        "   " + "|    " + table["F1"] + "   " + "|"
        + "|    " + table["G1"] + "   " + "|    " + table["H1"] + "   " + "|    " + table["I1"] + "   " + "|    " +
        table["J1"] + "   " + "|    " + table["K1"] + "   " + "|    " + table["L1"] + "   " + "| 1\n" +
        "  |---------|---------|---------|---------|---------|---------||---------|---------|---------|---------|---------|---------|\n" +
        "  |---------|---------|---------|---------|Brkn.X: " + str(
            xbroken) + "|Dice 1: " + str(
            dice1) + "||Dice 2: " + str(dice2) + "|Brkn.Y: " + str(
            ybroken) + "| Turn: " + turn + " |---------|---------|---------|\n" +
        "  |---------|---------|---------|---------|---------|---------||---------|---------|---------|---------|---------|---------|\n"
        "2 |    " + table["A2"] + "   " + "|    " +
        table["B2"] + "   " + "|    " + table["C2"] + "   " + "|    " +
        table["D2"] + "   " + "|    " + table["E2"] +
        "   " + "|    " + table["F2"] + "   " + "|"
        + "|    " + table["G2"] + "   " + "|    " + table["H2"] + "   " + "|    " + table["I2"] + "   " + "|    " +
        table["J2"] + "   " + "|    " + table["K2"] + "   " + "|    " + table["L2"] + "   " + "| 2\n" +
        "  |---------|---------|---------|---------|---------|---------||---------|---------|---------|---------|---------|---------|\n")
    f.close()


def printToFileContinue():
    if os.path.exists('Continue.dat'):
        f = open("Continue.dat", "w")
        f.write(
            table["A1"] + "\n" +
            table["B1"] + "\n" +
            table["C1"] + "\n" +
            table["D1"] + "\n" +
            table["E1"] + "\n" +
            table["F1"] + "\n" +
            table["G1"] + "\n" +
            table["H1"] + "\n" +
            table["I1"] + "\n" +
            table["J1"] + "\n" +
            table["K1"] + "\n" +
            table["L1"] + "\n" +
            table["A2"] + "\n" +
            table["B2"] + "\n" +
            table["C2"] + "\n" +
            table["D2"] + "\n" +
            table["E2"] + "\n" +
            table["F2"] + "\n" +
            table["G2"] + "\n" +
            table["H2"] + "\n" +
            table["I2"] + "\n" +
            table["J2"] + "\n" +
            table["K2"] + "\n" +
            table["L2"] + "\n" +
            turn + "\n" +
            str(xbroken) + "\n" +
            str(ybroken) + "\n" +
            str(xflake) + "\n" +
            str(yflake) + "\n" +
            str(dice1) + "\n" +
            str(dice2) + "\n"
        )
        f.close()
        f = open("Continue.dat", "a")
        if len(dices) == 1:
            f.write(str(dices[0]) + "\n")
        elif len(dices) == 2:
            f.write(
                str(dices[0]) + "\n" +
                str(dices[1]) + "\n"
            )
        elif len(dices) == 3:
            f.write(
                str(dices[0]) + "\n" +
                str(dices[1]) + "\n" +
                str(dices[2]) + "\n"
            )
        elif len(dices) == 4:
            f.write(
                str(dices[0]) + "\n" +
                str(dices[1]) + "\n" +
                str(dices[2]) + "\n" +
                str(dices[3]) + "\n"
            )
        f.close()
    else:
        print("Kayıtlı oyun bulunamadı. Oyundan çıkış yapılıyor.")
        exit()


def toplamaX():
    global xbroken
    toplam = 0
    for flake in table:
        if table[flake][-1:] == "X" and not (
                flake == "G1" or flake == "H1" or flake == "I1" or flake == "J1" or flake == "K1" or flake == "L1"):
            toplam += int(table[flake][:-1])
    if toplam == 0 and xbroken == 0:
        return True
    else:
        return False


def toplamaY():
    toplam = 0
    for flake in table:
        if table[flake][-1:] == "Y" and not (
                flake == "G2" or flake == "H2" or flake == "I2" or flake == "J2" or flake == "K2" or flake == "L2"):
            toplam += int(table[flake][:-1])
    if toplam == 0:
        return True
    else:
        return False


def moveX(flake, dice):
    global xbroken
    if table[flake][-1:] == "X" or xbroken > 0:  # Başlangıç konumunda oynanabilecek taş kontrolü
        # Başlangıç konumunun adresinin sadece harfini ayırıyor.
        loc = ord(flake[:-1])
        if xbroken > 0:
            loc = ord("M")
            target = chr(loc - dice) + "2"
        elif ord(flake[:-1]) - 65 - dice >= 0 and flake[-1:] == "2":
            target = chr(loc - dice) + "2"  # 2. satırdaysa sola doğru devam
        elif flake[-1:] == "1":
            target = chr(loc + dice) + "1"  # 1. satırdaysa sağa doğru devam
        else:
            target = (chr(abs(ord(flake[:-1]) - 65 - dice + 1) + 65) + '1')
        if target[:-1] < "M":

            if table[target][-1:] == "X":  # Hedef konumda taş varsa 1 artırılıyor.
                table[target] = str(int(table[target][:-1]) + 1) + "X"
                # Başlangıç konumunda birden fazla taş varsa bir eksilecek.
                if xbroken == 0:
                    if table[flake] != "1X":
                        table[flake] = str(int(table[flake][:-1]) - 1) + "X"
                    else:
                        # Başlangıç konumunda 1 taş varsa sıfırlanacak.
                        table[flake] = "--"
                if xbroken > 0:
                    xbroken -= 1
                return True
            elif table[target][-1:] == "-":
                # Hedef konumda taş yoksa 1X yazdırılacak.
                table[target] = "1X"
                if xbroken == 0:
                    # Başlangıç konumunda birden fazla taş varsa bir eksilecek.
                    if table[flake] != "1X":
                        table[flake] = str(int(table[flake][:-1]) - 1) + "X"
                    else:
                        # Başlangıç konumunda 1 taş varsa sıfırlanacak.
                        table[flake] = "--"
                if xbroken > 0:
                    xbroken -= 1
                return True
            elif table[target] == "1Y":
                # Hedef konumda rakibin 1 taşı varsa oraya yerleştir ve rakibin kırık taş miktarını 1 artır.
                table[target] = "1X"
                global ybroken
                ybroken += 1

                # Başlangıç konumunda birden fazla taş varsa bir eksilecek.
                if xbroken == 0:
                    if table[flake] != "1X":
                        table[flake] = str(int(table[flake][:-1]) - 1) + "X"
                    else:
                        # Başlangıç konumunda 1 taş varsa sıfırlanacak.
                        table[flake] = "--"
                if xbroken > 0:
                    xbroken -= 1
                return True
            else:
                print("Buraya hamle yapamazsınız.")
                return False

        else:
            print("Buraya hamle yapamazsınız.")
            return False
    else:
        print("Buradan oynayamazsınız.")
        return False


def moveY(flake, dice):
    global ybroken

    if table[flake][-1:] == 'Y' or ybroken > 0:  # Başlangıç konumunda oynanabilecek taş kontrolü
        # Başlangıç konumunun adresinin sadece harfini ayırıyor.
        loc = ord(flake[:-1])
        if ybroken > 0:
            loc = ord("M")
            target = chr(loc - dice) + "1"
        elif ord(flake[:-1]) - 65 - dice >= 0 and flake[-1:] == "1":
            target = chr(loc - dice) + "1"  # 1. satırdaysa sola doğru devam

        elif flake[-1:] == "2":
            target = chr(loc + dice) + "2"  # 2. satırdaysa sağa doğru devam
        else:
            target = (chr(abs(ord(flake[:-1]) - 65 - dice + 1) + 65) + '2')
        if target[:-1] < "M":
            if table[target][-1:] == "Y":  # Hedef konumda taş varsa 1 artırılıyor.
                table[target] = str(int(table[target][:-1]) + 1) + "Y"
                # Başlangıç konumunda birden fazla taş varsa bir eksilecek.
                if ybroken == 0:
                    if table[flake] != "1Y":
                        table[flake] = str(int(table[flake][:-1]) - 1) + "Y"
                    else:
                        # Başlangıç konumunda 1 taş varsa sıfırlanacak.
                        table[flake] = "--"
                if ybroken > 0:
                    ybroken -= 1
                return True

            elif table[target][-1:] == "-":
                # Hedef konumda taş yoksa 1Y yazdırılacak.
                table[target] = "1Y"
                if ybroken == 0:
                    # Başlangıç konumunda birden fazla taş varsa bir eksilecek.
                    if table[flake] != "1Y":
                        table[flake] = str(int(table[flake][:-1]) - 1) + "Y"
                    else:
                        # Başlangıç konumunda 1 taş varsa sıfırlanacak.
                        table[flake] = "--"
                if ybroken > 0:
                    ybroken -= 1
                return True

            elif table[target] == "1X":
                # Hedef konumda rakibin 1 taşı varsa oraya yerleştir ve rakibin kırık taş miktarını 1 artır.
                table[target] = "1Y"
                global xbroken
                xbroken += 1
                # Başlangıç konumunda birden fazla taş varsa bir eksilecek.
                if ybroken == 0:
                    if table[flake] != "1Y":
                        table[flake] = str(int(table[flake][:-1]) - 1) + "Y"
                    else:
                        # Başlangıç konumunda 1 taş varsa sıfırlanacak.
                        table[flake] = "--"
                if ybroken > 0:
                    ybroken -= 1
                return True

            else:
                print("Buraya oynayamazsınız")
                return False
        else:
            print("Buraya oynayamazsınız")
            return False

    else:
        print("Buradan oynayamazsınız.")
        return False


start = input("1-Yeni oyun\n2-Önceki oyundan devam et")
while start != "1" and start != "2":
    print("Hatalı giriş yaptınız.")
    start = input("1-Yeni oyun\n2-Önceki oyundan devam et")
if start == "1":
    while str(dice1) == str(dice2):
        rollDice()
    print("X: " + str(dice1) + " Y: " + str(dice2) + "\n")
    f = open("Log.dat", "w")
    f.write(str(dice1) + "\n" + str(dice2) + "\n")
    f.close()
    if dice1 > dice2:
        turn = "X"
        print("X başlıyor" + "\n")
    else:
        turn = "Y"
        print("Y başlıyor" + "\n")
elif start == "2":
    if os.path.exists('Continue.dat'):
        with open('Continue.dat') as f:
            my_list = [x.rstrip() for x in f]
        f.close()
        table = {
            "A1": my_list[0],
            "B1": my_list[1],
            "C1": my_list[2],
            "D1": my_list[3],
            "E1": my_list[4],
            "F1": my_list[5],
            "G1": my_list[6],
            "H1": my_list[7],
            "I1": my_list[8],
            "J1": my_list[9],
            "K1": my_list[10],
            "L1": my_list[11],
            "A2": my_list[12],
            "B2": my_list[13],
            "C2": my_list[14],
            "D2": my_list[15],
            "E2": my_list[16],
            "F2": my_list[17],
            "G2": my_list[18],
            "H2": my_list[19],
            "I2": my_list[20],
            "J2": my_list[21],
            "K2": my_list[22],
            "L2": my_list[23],
        }
        turn = my_list[24]
        xbroken = int(my_list[25])
        ybroken = int(my_list[26])
        xflake = int(my_list[27])
        yflake = int(my_list[28])
        dice1 = int(my_list[29])
        dice2 = int(my_list[30])
        if len(my_list) == 32:
            dices.append(int(my_list[31]))
        if len(my_list) == 33:
            dices.append(int(my_list[31]))
            dices.append(int(my_list[32]))
        if len(my_list) == 34:
            dices.append(int(my_list[31]))
            dices.append(int(my_list[32]))
            dices.append(int(my_list[33]))
        if len(my_list) == 35:
            dices.append(int(my_list[31]))
            dices.append(int(my_list[32]))
            dices.append(int(my_list[33]))
            dices.append(int(my_list[34]))
    else:
        print("Kayıtlı oyun bulunamadı. Oyundan çıkış yapılıyor.")
        exit()
if start != "2":
    rollDice()
    if dice1 == dice2: #Farklı zar kontrolü
        dices = [1, 1, 1, 1]
    else:
        dices = [1, 2]
while xflake != 15 and yflake != 15:
    print(turn + " turu")
    if dice1 == dice2 and start == 1:
        dices = [1, 1, 1, 1]
    elif dice1 != dice2 and start == 1:
        dices = [1, 2]
    if turn == "X" and dice1 != dice2:
        i = 0
        j = len(dices)
        while i < j:
            if yflake == 15 or xflake == 15: #Oyun bittiyse döngüden çık
                i += 2
                break
            printTable()
            printToFile()
            printToFileContinue()
            if xbroken > 0:
                flake = "A1" #Sadece ilk değer ataması olması için verildi önemsiz.
                dice = input("Kaç oynamak istiyorsunuz?")
                if dice.upper() == "PAS":
                    i += 1
                    printToFile()
                    printToFileContinue()
                elif dice.upper() == "Q":
                    print("Oyun bitti.")
                    exit()
                else:
                    if dice == "1" or dice == "2" or dice == "3" or dice == "4" or dice == "5" or dice == "6":
                        while (int(dice) not in [dice1, dice2]) and i < j:
                            print("Böyle bir zar yok.")
                            dice = input("Kaç oynamak istiyorsunuz?")
                            if dice.upper() == "PAS":
                                i += 1
                                printToFile()
                                printToFileContinue()
                            elif dice.upper() == "Q":
                                print("Oyun bitti.")
                                exit()
                        if moveX(flake, int(dice)):
                            i += 1
                            if int(dice) == dice1:
                                dices.remove(1)
                            elif int(dice) == dice2:
                                dices.remove(2)
                            printToFile()
                            printToFileContinue()
                        else:
                            print("Bu hamleyi yapamazsın.")
                    else:
                        print("Hatalı giriş yaptınız.")
            else: #Eğer kırık taşı yoksa
                flake = input("Hangi taşı oynamak istiyorsunuz?").upper()

                if flake == "PAS":
                    i += 1
                    printToFile()
                    printToFileContinue()
                    print("Pas!")
                elif flake == "Q":
                    print("Oyun bitti.")
                    exit()
                else:
                    while flake[0] < "A" or flake[0] > "L" or flake[1] < "1" or flake[1] > "2": #Hatalı input kontrolü
                        if flake == "PAS":
                            break
                        if flake == "Q":
                            print("Oyun bitti.")
                            exit()
                        print("Hatalı giriş yaptınız.")
                        flake = input("Hangi taşı oynamak istiyorsunuz?").upper()
                while flake == "PAS" and i < 2:
                    flake = input("Hangi taşı oynamak istiyorsunuz?").upper()

                    if flake == "PAS":
                        i += 1
                        printToFile()
                        printToFileContinue()
                        print("Pas!")
                    elif flake == "Q":
                        print("Oyun bitti.")
                        exit()
                    else:
                        while flake[0] < "A" or flake[0] > "L" or flake[1] < "1" or flake[1] > "2":
                            if flake == "PAS":
                                break
                            if flake == "Q":
                                print("Oyun bitti.")
                                exit()
                            print("Hatalı giriş yaptınız.")
                            flake = input("Hangi taşı oynamak istiyorsunuz?").upper()
                if flake != "PAS":
                    dice = input("Kaç oynamak istiyorsunuz?")
                    if dice.upper() == "PAS":
                        i += 1
                        printToFile()
                        printToFileContinue()
                    elif dice.upper() == "Q":
                        print("Oyun bitti.")
                        exit()
                    else:
                        if dice == "1" or dice == "2" or dice == "3" or dice == "4" or dice == "5" or dice == "6":
                            while (int(dice) not in [dice1, dice2]):
                                print("Böyle bir zar yok.")
                                dice = input("Kaç oynamak istiyorsunuz?")
                            if int(dice) == dice1:
                                if 1 in dices:
                                    if toplamaX() and xbroken == 0: #Toplama şartı sağlanıyorsa ve kırık taşı yoksa
                                        # Eğer zar ile toplanabiliyorsa topluyor.
                                        if chr(ord(flake[0]) + int(dice)) == 'M':
                                            if table[flake] == "1X":
                                                table[flake] = "--"
                                                xflake += 1
                                            else:
                                                table[flake] = str(int(table[flake][:-1]) - 1) + "X"
                                                xflake += 1
                                            i += 1
                                            dices.remove(1)
                                            printToFile()
                                            printToFileContinue()
                                        # Eğer kendinden önce taş yoksa
                                        elif (table[chr(ord(flake[:-1]) - 1) + "1"][-1:] != "X" and
                                              table[chr(ord(flake[:-1]) - 2) + "1"][-1:] != "X" and
                                              table[chr(ord(flake[:-1]) - 3) + "1"][-1:] != "X" and
                                              table[chr(ord(flake[:-1]) - 4) + "1"][-1:] != "X" and
                                              table[chr(ord(flake[:-1]) - 5) + "1"][-1:] != 'X'):
                                            # Toplaması için gerekenden küçük zar atarsa
                                            if chr(ord(flake[0]) + int(dice)) <= 'L':
                                                if moveX(flake, int(dice)):
                                                    i += 1
                                                    dices.remove(1)
                                                    printToFile()
                                                    printToFileContinue()

                                                else:
                                                    print("Bu hamle yapılamıyor.")
                                            else:
                                                # Toplaması için gereken zarı atarsa

                                                if table[flake] == "1X":
                                                    table[flake] = "--"
                                                    xflake += 1
                                                else:
                                                    table[flake] = str(int(table[flake][:-1]) - 1) + "X"
                                                    xflake += 1
                                                i += 1
                                                dices.remove(1)
                                                printToFile()
                                                printToFileContinue()

                                        else:
                                            if chr(ord(flake[0]) + int(dice)) <= 'L':
                                                if moveX(flake, int(dice)):
                                                    i += 1
                                                    dices.remove(1)
                                                    printToFile()
                                                    printToFileContinue()

                                                else:
                                                    print("Bu hamle yapılamıyor.")
                                            else:
                                                print("Bu taşı toplayamazsınız.")

                                    elif moveX(flake, int(dice)):
                                        i += 1
                                        dices.remove(1)
                                        printToFile()
                                        printToFileContinue()

                                else:
                                    print("Bu zarı zaten oynadınız.")
                            elif int(dice) == dice2:
                                if 2 in dices:
                                    if toplamaX() and xbroken == 0:

                                        if chr(ord(flake[0]) + int(dice)) == 'M':
                                            if table[flake] == "1X":
                                                table[flake] = "--"
                                                xflake += 1
                                            else:
                                                table[flake] = str(int(table[flake][:-1]) - 1) + "X"
                                                xflake += 1
                                            i += 1
                                            dices.remove(2)
                                            printToFile()
                                            printToFileContinue()

                                        elif (table[chr(ord(flake[:-1]) - 1) + "1"][-1:] != "X" and
                                              table[chr(ord(flake[:-1]) - 2) + "1"][-1:] != "X" and
                                              table[chr(ord(flake[:-1]) - 3) + "1"][-1:] != "X" and
                                              table[chr(ord(flake[:-1]) - 4) + "1"][-1:] != "X" and
                                              table[chr(ord(flake[:-1]) - 5) + "1"][-1:] != 'X'):
                                            if chr(ord(flake[0]) + int(dice)) <= 'L':
                                                if moveX(flake, int(dice)):
                                                    i += 1
                                                    dices.remove(2)
                                                    printToFile()
                                                    printToFileContinue()

                                                else:
                                                    print("Bu hamle yapılamıyor.")
                                            else:

                                                if table[flake] == "1X":
                                                    table[flake] = "--"
                                                    xflake += 1
                                                else:
                                                    table[flake] = str(int(table[flake][:-1]) - 1) + "X"
                                                    xflake += 1
                                                i += 1
                                                dices.remove(2)
                                                printToFile()
                                                printToFileContinue()

                                        elif int(ord(flake[:-1])) - 65 + int(dice) < 12:
                                            if moveX(flake, int(dice)):
                                                i += 1
                                                dices.remove(2)
                                                printToFile()
                                                printToFileContinue()

                                        else:
                                            if chr(ord(flake[0]) + int(dice)) <= 'L':
                                                if moveX(flake, int(dice)):
                                                    i += 1
                                                    dices.remove(2)
                                                    printToFile()
                                                    printToFileContinue()

                                                else:
                                                    print("Bu hamle yapılamıyor.")
                                            else:
                                                print("Bu taşı toplayamazsınız.")
                                    elif moveX(flake, int(dice)):
                                        i += 1
                                        dices.remove(2)
                                        printToFile()
                                        printToFileContinue()

                                else:
                                    print("Bu zarı zaten oynadınız.")
                        else:
                            print("Hatalı giriş yaptınız.")
    elif turn == "X" and dice1 == dice2:
        if start == 1:
            dices = [1, 1, 1, 1]
        i = 0
        j = len(dices)
        while i < j:
            if yflake == 15 or xflake == 15:
                i += 2
                break
            printTable()
            printToFile()
            printToFileContinue()
            if xbroken > 0:
                flake = "A1"
                dice = dice1
            else:
                flake = input("Hangi taşı oynamak istiyorsunuz?").upper()

                if flake == "PAS":
                    i += 1

                    printToFile()
                    printToFileContinue()
                    print("Pas!")
                elif flake == "Q":
                    print("Oyun bitti.")
                    exit()
                else:
                    while flake[0] < "A" or flake[0] > "L" or flake[1] < "1" or flake[1] > "2":
                        if flake == "PAS":
                            break
                        if flake == "Q":
                            print("Oyun bitti.")
                            exit()
                        print("Hatalı giriş yaptınız.")
                        flake = input("Hangi taşı oynamak istiyorsunuz?").upper()
                while flake == "PAS" and i < 2:
                    flake = input("Hangi taşı oynamak istiyorsunuz?").upper()

                    if flake == "PAS":
                        i += 1
                        printToFile()
                        printToFileContinue()
                        print("Pas!")
                    elif flake == "Q":
                        print("Oyun bitti.")
                        exit()
                    else:
                        while flake[0] < "A" or flake[0] > "L" or flake[1] < "1" or flake[1] > "2":
                            if flake == "PAS":
                                break
                            if flake == "Q":
                                print("Oyun bitti.")
                                exit()
                            print("Hatalı giriş yaptınız.")
                            flake = input("Hangi taşı oynamak istiyorsunuz?").upper()
                if flake != "PAS":
                    dice = dice1
                    if toplamaX() and xbroken == 0:
                        if chr(ord(flake[0]) + dice) == 'M': #Toplanması için gereken zarı attıysa
                            if table[flake] == "1X":
                                table[flake] = "--"
                                xflake += 1
                            else:
                                table[flake] = str(int(table[flake][:-1]) - 1) + "X"
                                xflake += 1
                            i += 1
                            dices.remove(1)
                            printToFile()
                            printToFileContinue()

                        elif (table[chr(ord(flake[:-1]) - 1) + "1"][-1:] != "X" and
                              table[chr(ord(flake[:-1]) - 2) + "1"][-1:] != "X" and
                              table[chr(ord(flake[:-1]) - 3) + "1"][-1:] != "X" and
                              table[chr(ord(flake[:-1]) - 4) + "1"][-1:] != "X" and
                              table[chr(ord(flake[:-1]) - 5) + "1"][-1:] != 'X'): #Kendinden önce taşı olmaması
                            if chr(ord(flake[0]) + dice) <= 'L': #Hareket etme durumu
                                if moveX(flake, int(dice)):
                                    i += 1
                                    dices.remove(1)
                                    printToFile()
                                    printToFileContinue()

                                else:
                                    print("Bu hamle yapılamıyor.")
                            else: #Toplama durumu

                                if table[flake] == "1X":
                                    table[flake] = "--"
                                    xflake += 1
                                else:
                                    table[flake] = str(int(table[flake][:-1]) - 1) + "X"
                                    xflake += 1
                                i += 1
                                dices.remove(1)
                                printToFile()
                                printToFileContinue()

                        elif int(ord(flake[:-1])) - 65 + dice < 12:
                            if moveX(flake, int(dice)):
                                i += 1
                                dices.remove(1)
                                printToFile()
                                printToFileContinue()
                        else:
                            if chr(ord(flake[0]) + int(dice)) <= 'L':
                                if moveX(flake, int(dice)):
                                    i += 1
                                    dices.remove(1)
                                    printToFile()
                                    printToFileContinue()
                                else:
                                    print("Bu hamle yapılamıyor.")
                            else:
                                print("Bu taşı toplayamazsınız.")
                    elif moveX(flake, int(dice)):
                        i += 1
                        dices.remove(1)
                        printToFile()
                        printToFileContinue()
    if turn == "Y" and dice1 != dice2:
        i = 0
        j = len(dices)
        while i < j:
            if yflake == 15 or xflake == 15:
                i += 2
                break
            printTable()
            printToFile()
            printToFileContinue()
            if ybroken > 0:
                flake = "A1"
                dice = input("Kaç oynamak istiyorsunuz?")
                if dice.upper() == "PAS":
                    i += 1
                    printToFile()
                    printToFileContinue()
                elif dice.upper() == "Q":
                    print("Oyun bitti.")
                    exit()
                elif dice == "1" or dice == "2" or dice == "3" or dice == "4" or dice == "5" or dice == "6":
                    while (int(dice) not in [dice1, dice2]) and i < j:
                        print("Böyle bir zar yok.")
                        dice = input("Kaç oynamak istiyorsunuz?")
                        if dice.upper() == "PAS":
                            i += 1
                            printToFile()
                            printToFileContinue()
                        elif dice.upper() == "Q":
                            print("Oyun bitti.")
                            exit()
                    if moveY(flake, int(dice)):
                        i += 1
                        printToFile()
                        printToFileContinue()
                        if int(dice) == dice1:
                            dices.remove(1)
                        elif int(dice) == dice2:
                            dices.remove(2)
                    else:
                        print("Bu hamleyi yapamazsın.")
                else:
                    print("Hatalı giriş yaptınız.")
            else:
                flake = input("Hangi taşı oynamak istiyorsunuz?").upper()
                if flake == "PAS":
                    i += 1
                    printToFile()
                    printToFileContinue()
                    print("Pas!")
                elif flake == "Q":
                    print("Oyun bitti.")
                    exit()
                else:
                    while flake[0] < "A" or flake[0] > "L" or flake[1] < "1" or flake[1] > "2":
                        if flake == "PAS":
                            break
                        if flake == "Q":
                            print("Oyun bitti.")
                            exit()
                        print("Hatalı giriş yaptınız.")
                        flake = input("Hangi taşı oynamak istiyorsunuz?").upper()
                while flake == "PAS" and i < 2:
                    flake = input("Hangi taşı oynamak istiyorsunuz?").upper()
                    if flake == "PAS":
                        i += 1
                        printToFile()
                        printToFileContinue()
                        print("Pas!")
                    elif flake == "Q":
                        print("Oyun bitti.")
                        exit()
                    else:
                        while flake[0] < "A" or flake[0] > "L" or flake[1] < "1" or flake[1] > "2":
                            if flake == "PAS":
                                break
                            if flake == "Q":
                                print("Oyun bitti.")
                                exit()
                            print("Hatalı giriş yaptınız.")
                            flake = input("Hangi taşı oynamak istiyorsunuz?").upper()
                if flake != "PAS":
                    dice = input("Kaç oynamak istiyorsunuz?")
                    if dice == "1" or dice == "2" or dice == "3" or dice == "4" or dice == "5" or dice == "6":
                        while int(dice) not in [dice1, dice2]:
                            print("Böyle bir zar yok.")
                            dice = input("Kaç oynamak istiyorsunuz?")
                        if int(dice) == dice1:
                            if 1 in dices:
                                if toplamaY() and ybroken == 0:
                                    if chr(ord(flake[0]) + int(dice)) == 'M':
                                        if table[flake] == "1Y":
                                            table[flake] = "--"
                                            yflake += 1
                                        else:
                                            table[flake] = str(int(table[flake][:-1]) - 1) + "Y"
                                            yflake += 1
                                        i += 1
                                        dices.remove(1)
                                        printToFile()
                                        printToFileContinue()

                                    elif (table[chr(ord(flake[:-1]) - 1) + "2"][-1:] != "Y" and
                                          table[chr(ord(flake[:-1]) - 2) + "2"][-1:] != "Y" and
                                          table[chr(ord(flake[:-1]) - 3) + "2"][-1:] != "Y" and
                                          table[chr(ord(flake[:-1]) - 4) + "2"][-1:] != "Y" and
                                          table[chr(ord(flake[:-1]) - 5) + "2"][-1:] != 'Y'):
                                        if chr(ord(flake[0]) + int(dice)) <= 'L':
                                            if moveY(flake, int(dice)):
                                                i += 1
                                                dices.remove(1)
                                                printToFile()
                                                printToFileContinue()

                                            else:
                                                print("Bu hamle yapılamıyor.")
                                        else:

                                            if table[flake] == "1Y":
                                                table[flake] = "--"
                                                yflake += 1
                                            else:
                                                table[flake] = str(int(table[flake][:-1]) - 1) + "Y"
                                                yflake += 1
                                            i += 1
                                            dices.remove(1)
                                            printToFile()
                                            printToFileContinue()

                                    elif int(ord(flake[:-1])) - 65 + int(dice) < 12:
                                        if moveY(flake, int(dice)):
                                            i += 1
                                            dices.remove(1)
                                            printToFile()
                                            printToFileContinue()

                                    else:
                                        if chr(ord(flake[0]) + int(dice)) <= 'L':
                                            if moveY(flake, int(dice)):
                                                i += 1
                                                dices.remove(1)
                                                printToFile()
                                                printToFileContinue()

                                            else:
                                                print("Bu hamle yapılamıyor.")
                                        else:
                                            print("Bu taşı toplayamazsınız.")
                                elif moveY(flake, int(dice)):
                                    i += 1
                                    dices.remove(1)
                                    printToFile()
                                    printToFileContinue()

                            else:
                                print("Bu zarı zaten oynadınız.")
                        elif int(dice) == dice2:
                            if 2 in dices:
                                if toplamaY() and ybroken == 0:
                                    if chr(ord(flake[0]) + int(dice)) == 'M':
                                        if table[flake] == "1Y":
                                            table[flake] = "--"
                                            yflake += 1
                                        else:
                                            table[flake] = str(int(table[flake][:-1]) - 1) + "Y"
                                            yflake += 1
                                        i += 1
                                        dices.remove(2)
                                        printToFile()
                                        printToFileContinue()

                                    elif (table[chr(ord(flake[:-1]) - 1) + "2"][-1:] != "Y" and
                                          table[chr(ord(flake[:-1]) - 2) + "2"][-1:] != "Y" and
                                          table[chr(ord(flake[:-1]) - 3) + "2"][-1:] != "Y" and
                                          table[chr(ord(flake[:-1]) - 4) + "2"][-1:] != "Y" and
                                          table[chr(ord(flake[:-1]) - 5) + "2"][-1:] != 'Y'):
                                        if chr(ord(flake[0]) + int(dice)) <= 'L':
                                            if moveY(flake, int(dice)):
                                                i += 1
                                                dices.remove(2)
                                                printToFile()
                                                printToFileContinue()

                                            else:
                                                print("Bu hamle yapılamıyor.")
                                        else:
                                            if table[flake] == "1Y":
                                                table[flake] = "--"
                                                yflake += 1
                                            else:
                                                table[flake] = str(int(table[flake][:-1]) - 1) + "Y"
                                                yflake += 1
                                            i += 1
                                            dices.remove(2)
                                            printToFile()
                                            printToFileContinue()

                                    elif int(ord(flake[:-1])) - 65 + int(dice) < 12:
                                        if moveY(flake, int(dice)):
                                            i += 1
                                            dices.remove(2)
                                            printToFile()
                                            printToFileContinue()

                                    else:
                                        if chr(ord(flake[0]) + int(dice)) <= 'L':
                                            if moveY(flake, int(dice)):
                                                i += 1
                                                dices.remove(2)
                                                printToFile()
                                                printToFileContinue()

                                            else:
                                                print("Bu hamle yapılamıyor.")
                                        else:
                                            print("Bu taşı toplayamazsınız.")
                                elif moveY(flake, int(dice)):
                                    i += 1
                                    dices.remove(2)
                                    printToFile()
                                    printToFileContinue()

                            else:
                                print("Bu zarı zaten oynadınız.")
                    else:
                        print("Hatalı giriş yaptınız.")
    elif turn == "Y" and dice1 == dice2:
        if start == 1:
            dices = [1, 1, 1, 1]
        i = 0
        j = len(dices)
        while i < j:
            if yflake == 15 or xflake == 15:
                i += 2
                break
            printTable()
            printToFile()
            printToFileContinue()
            if ybroken > 0:
                flake = "A1"
                dice = dice1
            else:
                flake = input("Hangi taşı oynamak istiyorsunuz?").upper()
                if flake == "PAS":
                    i += 1
                    printToFile()
                    printToFileContinue()
                    print("Pas!")
                elif flake == "Q":
                    print("Oyun bitti.")
                    exit()
                else:
                    while flake[0] < "A" or flake[0] > "L" or flake[1] < "1" or flake[1] > "2":
                        if flake == "PAS":
                            break
                        if flake == "Q":
                            print("Oyun bitti.")
                            exit()
                        print("Hatalı giriş yaptınız.")
                        flake = input("Hangi taşı oynamak istiyorsunuz?").upper()
                while flake == "PAS" and i < 2:
                    flake = input("Hangi taşı oynamak istiyorsunuz?").upper()

                    if flake == "PAS":
                        i += 1
                        printToFile()
                        printToFileContinue()
                        print("Pas!")
                    elif flake == "Q":
                        print("Oyun bitti.")
                        exit()
                    else:
                        while flake[0] < "A" or flake[0] > "L" or flake[1] < "1" or flake[1] > "2":
                            if flake == "PAS":
                                break
                            if flake == "Q":
                                print("Oyun bitti.")
                                exit()
                            print("Hatalı giriş yaptınız.")
                            flake = input("Hangi taşı oynamak istiyorsunuz?").upper()
                if flake != "PAS":
                    dice = dice1
                    if toplamaY() and ybroken == 0:
                        if chr(ord(flake[0]) + dice) == 'M':
                            if table[flake] == "1Y":
                                table[flake] = "--"
                                yflake += 1
                            else:
                                table[flake] = str(int(table[flake][:-1]) - 1) + "Y"
                                yflake += 1
                            i += 1
                            dices.remove(1)
                            printToFile()
                            printToFileContinue()

                        elif (table[chr(ord(flake[:-1]) - 1) + "2"][-1:] != "Y" and
                              table[chr(ord(flake[:-1]) - 2) + "2"][-1:] != "Y" and
                              table[chr(ord(flake[:-1]) - 3) + "2"][-1:] != "Y" and
                              table[chr(ord(flake[:-1]) - 4) + "2"][-1:] != "Y" and
                              table[chr(ord(flake[:-1]) - 5) + "2"][-1:] != 'Y'):
                            if chr(ord(flake[0]) + dice) <= 'L':
                                if moveY(flake, int(dice)):
                                    i += 1
                                    dices.remove(1)
                                    printToFile()
                                    printToFileContinue()

                                else:
                                    print("Bu hamle yapılamıyor.")
                            else:
                                if table[flake] == "1Y":
                                    table[flake] = "--"
                                    yflake += 1
                                else:
                                    table[flake] = str(int(table[flake][:-1]) - 1) + "Y"
                                    yflake += 1
                                i += 1
                                dices.remove(1)
                                printToFile()
                                printToFileContinue()

                        elif int(ord(flake[:-1])) - 65 + dice < 12:
                            if moveY(flake, int(dice)):
                                i += 1
                                dices.remove(1)
                                printToFile()
                                printToFileContinue()
                        else:
                            if chr(ord(flake[0]) + int(dice)) <= 'L':
                                if moveY(flake, int(dice)):
                                    i += 1
                                    dices.remove(1)
                                    printToFile()
                                    printToFileContinue()

                                else:
                                    print("Bu hamle yapılamıyor.")
                            else:
                                print("Bu taşı toplayamazsınız.")
                    elif moveY(flake, int(dice)):
                        i += 1
                        print(j)
                        print(dices)
                        dices.remove(1)
                        printToFile()
                        printToFileContinue()
    printLog()
    if turn == "X":
        turn = "Y"
    else:
        turn = "X"
    rollDice()
    if dice1 != dice2:
        dices = [1, 2]
    elif dice1 == dice2:
        dices = [1, 1, 1, 1]
    printToFile()
    printToFileContinue()
    printToFileContinue()
    if xflake == 15 or yflake == 15:
        break
printTable()
if xflake == 15:
    print("X kazandı.")
elif yflake == 15:
    print("Y kazandı.")
