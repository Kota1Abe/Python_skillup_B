from datetime import date
from database import session
from make_transport import Transport_make
import sys

args = sys.argv
input_date=args[1]
input_seq=int(args[2])
input_departure=args[3]
input_arrival=args[4]
input_via=args[5]
input_amount=args[6]

year=int(input_date[0:4])
month=int(input_date[4:6])
day=int(input_date[6:8])

#seq取り出し
seq_list=session.query(Transport_make.seq).filter_by(data=date(year,month,day)).all()
#seq_list=session.query(Attendnum.seq).all()
#print(seq_list)
#print(seq_list[0],seq_list[1])

#seqリストが空の時
if not seq_list:
    transport=Transport_make(
    data=date(year,month,day),
    seq=1,
    departure=input_departure,
    arrival=input_arrival,
    via=input_via,
    amount=input_amount,
    )

    print("交通費精算テーブルにデータを作成しました")

    session.add(transport)
    session.commit()



#seqリストがすでに存在するとき
else:
    """
    print(seq_list)
    seq_count=(max(seq_list)[0])
    print(seq_count)

    attendnum=Attendnum(
    entry_date=date(year,month,day),
    seq=seq_count+1,
    adult=adults,
    child=children
    )
    """
    print("error:交通費清算テーブルにデータを登録できませんでした")

