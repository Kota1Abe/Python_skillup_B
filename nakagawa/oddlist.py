list = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]

#listで奇数の添え字の要素のみ出力する
oddlist = []
for i in range(len(list)):
    if i % 2 != 0:
        oddlist.append(list[i])
print(oddlist, end="")