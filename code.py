import pandas as pd
file=open("ip_txt_file.txt","r")
a=file.readlines()
A=5
B=6
PC=0
R1 = 10
R0 = 20
R3 = 15
list=[]
for z in range(len(a)): 
    x = a[z].split(" ")
    list.append(x)
i=0  
while (i<len(list)):
    PC=i
    if list[i][1]=="CJNE":
        print(' '.join(list[i][1:]))                   
        data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
        df1=pd.DataFrame(data1,index = [""])
        print(df1)
        print("\n")  
        if (list[i][2]=='A' and list[i][4]=='B'):
            if (A!=B):
                for z in range(len(a)):
                    if list[i][-1][:5]==list[z][0][:5]:
                        i=z-1
    elif list[i][1]=="RR":
        if list[i][2]=="A\n":
            carry = A & 0x01  # Extract the least significant bit (carry)
            A = (A>>1)|(carry<<3)
            temp=A
            print(' '.join(list[i][1:]))
            data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
            df1=pd.DataFrame(data1,index = [""])
            print(df1)
            print("\n")
    elif list[i][1]=="RL":
        if list[i][2]=="A\n":
            carry = A & 0x8# Extract the most significant bit (carry)
            A = ((A << 1)|carry>>3)
            if (carry==8):
                A=A-16
            temp=A
            print(' '.join(list[i][1:]))
            data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
            df1=pd.DataFrame(data1,index = [""])
            print(df1)
            print("\n")
    elif  list[i][1]=="ADD":
        if list[i][2]=='A':
            if (list[i][4].startswith("#") and list[i][4].endswith("H\n") ):
                temp=list[i][4]
                temp=temp[1:3]
                A=A+int(temp,16)
                print(' '.join(list[i][1:]))
                data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
                df1=pd.DataFrame(data1,index = [""])
                print(df1)
                print("\n") 
    elif list[i][1] == "INC":
        if list[i][2] == "A\n":
            A = A+1
            temp = A
            print(' '.join(list[i][1:]))
            data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
            df1=pd.DataFrame(data1,index = [""])
            print(df1)
            print("\n")
    elif list[i][1] == "MOV":
        if list[i][2] == "A":
            if list[i][4] == "R0\n":
                A = R0
                temp = A
                temp1 = R0
                print(' '.join(list[i][1:]))
                data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
                df1 = pd.DataFrame(data1, index = [""])
                print(df1)
                print("\n")
    elif list[i][1] == "ORL":
        if list[i][2] == "A":
            if list[i][4] == "R0\n":
                A = A | R0
                temp = A
                temp1 = R0
                print(' '.join(list[i][1:]))
                data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
                df1 = pd.DataFrame(data1, index=[""])
                print(df1)
                print("\n")
    elif list[i][1] == "SUBB":
        if list[i][2] == "A":
            if list[i][4] == "R1\n":
                A = A - R1
                temp = A
                temp1 = R1
                print(' '.join(list[i][1:]))
                data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
                df1 = pd.DataFrame(data1, index=[""])
                print(df1)
                print("\n")
    elif list[i][1] == "DIV":
        temp3 = A
        A = int(A / B)
        temp = A
        B = temp3 % B
        temp1 = B
        print(' '.join(list[i][1:]))
        data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
        df1 = pd.DataFrame(data1, index=[""])
        print(df1)
        print("\n")
    elif list[i][1] == "XCH":
        if list[i][2] == "A":
            if list[i][4] == "R3\n":
                temp = R3
                R3 = A
                A = temp
                temp1 = A
                temp2 = R3
                print(' '.join(list[i][1:]))
                data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
                df1 = pd.DataFrame(data1, index=[""])
                print(df1)
                print("\n")
    elif list[i][1] == "XRL":
        if list[i][4] == "R1\n":
            A = A ^ R1
            temp = A
            temp1 = R1
            print(' '.join(list[i][1:]))
            data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
            df1 = pd.DataFrame(data1, index=[""])
            print(df1)
            print("\n")
    elif list[i][1] == "DEC":
        if list[i][2] == "A\n":
            A = A-1
            temp = A
            print(' '.join(list[i][1:]))
            data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
            df1=pd.DataFrame(data1,index = [""])
            print(df1)
            print("\n")
    elif list[i][1] == "MUL":
        if list[i][2] == "AR1\n":
            result = bin(A*R1)
            result=(8-(len(result)-2))*'0'+result[2:]
            result=int(result,2)
            A=result & 0xf0 
            A=A>>4
            B=result & 0x0f
            print(' '.join(list[i][1:]))
            data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
            df1=pd.DataFrame(data1,index = [""])
            print(df1)
            print("\n")
    elif list[i][1] == "CPL":
        A=15-A
        print(' '.join(list[i][1:]))
        data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
        df1=pd.DataFrame(data1,index = [""])
        print(df1)
        print("\n")
    elif list[i][1] == "ANL":
        A =A & R0
        
        print(' '.join(list[i][1:]))
        data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
        df1=pd.DataFrame(data1,index=[""])
        print(df1)
        print("\n")
    elif list[i][1] == "SETB":
        R3 = 1
        print(x[0] , x[1])
        data1={"Reg A":[hex(A)], "Reg B":[hex(B)], "Reg PC": [hex(PC)],"Reg R1":[hex(R1)],"Reg R0":[hex(R0)],"Reg R3":[hex(R3)]}
        df1=pd.DataFrame(data1,index=[""])
        print(df1)
        print("\n")  
    i+=1