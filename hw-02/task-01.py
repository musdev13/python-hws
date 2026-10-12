def displayLine(char, callback):
    callback(char)


def drawHorizontal(char):
    print(char * 20)


def drawVertical(char):
    for _ in range(10):
        print(char)


def main():
    symbol = input("Введіть символ для лінії: ")
    pick = input("Яку лінію малювати? (h - горизонтальну, v - вертикальну): ").lower()

    if pick == "h":
        displayLine(symbol, drawHorizontal)
    elif pick == "v":
        displayLine(symbol, drawVertical)
    else:
        print("Невірний вибір.")


if __name__ == "__main__":
    main()
