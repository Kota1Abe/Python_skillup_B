list=["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]
print_list=[]

for i in range(len(list)):
    if i%2!=0:
        print_list.append(list[i])

print(print_list)
