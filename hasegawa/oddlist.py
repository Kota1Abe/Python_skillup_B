# 苗字のリストmenber_listを定義

menber = [
    "Kurita", 
    "Tanaka", 
    "Kaneda", 
    "Noda", 
    "Koyama", 
    "Adachi", 
    "Kuriyama", 
    "Ohyama", 
    "Kishida"
    ]
# リストの要素を0から数えて奇数番目の要素をodd_member_listに代入
odd_menber_list = menber[1::2]

print(odd_menber_list,end="")