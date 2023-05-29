import os
import qrcode
#os.path.joinを利用して相対パスを生成する
#相対パス（"../files/xxxxxx.png"）となる

# qr1 = "https://github.com/Kota1Abe/Python_skillup_B"

# qr2 = "https://papago.naver.com/"

# qr3 = "https://www.naver.com/"

# li = [qr1,qr2,qr3]

# for i in li:

#     img = qrcode.make(i)

#     path = os.path.join(f"files",  "{i}.png") 
# # path = os.path.join( "","", "files",  "xxxxxx.png") 
# #png ファイルの生成

#     img.save(path)

with open('./qrlist.txt','r') as file:

    lines = file.readlines() # 파일의 모든 내용 추출 
    
    i=0
    for line in lines:
        
        line = line.strip() #  출력된 모든 파일의 줄을 앞뒤로 공백을 제거하고 저장 
        i +=1
       
        img = qrcode.make(line) 
        # path = os.path.join("C:/Users/s12300013/Desktop/PYTHON","xxxxx.png")

        os.makedirs("C:/Users/s12300013/Desktop/PYTHON/qrcode/",exist_ok=True)
        # 지정 경로에 폴더를 만듬 . exist_ok = True는 지정 경로에 폴더가 있어도 오류가 발생하지 않도록

        path = os.path.join("C:/Users/s12300013/Desktop/PYTHON/qrcode/",  f"{i}.png") 
        img.save(path)
      
file.close()