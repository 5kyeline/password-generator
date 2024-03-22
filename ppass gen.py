import random

letter="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
letter_list=letter.split(',')
nums='1,2,3,4,5,6,7,8,9,0'
nums_list=nums.split(',')
letter_cap=letter.upper()
letter_cap_list=letter_cap.split(',')
alphanum=letter_list+letter_cap_list+nums_list


t=int(input("enter how long you need your alphanumeric password to be: "))
password="".join((random.choice(alphanum) for i in range(t)))

print(password)

with open('pass.txt',"a") as f:
    print("selected length of the code is: ",t,file=f)
    print("your alphanumeric password is: ",password,file=f)



