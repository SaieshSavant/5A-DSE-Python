a=65
n=5
for i in range(n):
        print(" "*(n-i-1),end=" ")
        for j in range(0,i+1):
            print(chr(a),end=" ")
            a+=1
        print("\n")
        a=65    
            