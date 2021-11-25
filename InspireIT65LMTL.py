#เกมทายตัวเลข
import random 
#สุ่มตัวเลข 1-10
my_random = random.randrange(1,11)
x = 1 #x= จำนวนครั้งที่ตอบ
print("เกมทายตัวเลขตั้งแต่1-10")
print("คุณมีโอกาสตอบ 5 ครั้งนะครับ \n")

#loop กรอกคำตอบ
while True :
    number = int(input("คำตอบของคุณ = ")) 
    correct = (number==my_random) #เช็คคำตอบ

    if not correct :
        if(number > my_random):
            print("น้อยกว่านี้")
        else :
            print("มากกว่านี้")

    if correct :
        print("ถูกต้องนะครับ")
        break

    if number <= 0 or x==5 :
        break 
        x+=1

if not correct :
    print("ผิดนะครับ")
    print("เฉลย", my_random)