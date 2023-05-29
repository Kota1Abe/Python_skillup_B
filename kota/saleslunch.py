import sys
args = sys.argv

num_karaage=int(args[1])
num_curry=int(args[2])

karaage=760
curry=850

sales=karaage*num_karaage+curry*num_curry
print(sales,end="")
