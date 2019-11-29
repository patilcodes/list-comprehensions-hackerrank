x = int(input("Enter num1:"))
y = int(input("Enter num2:"))
z = int(input("Enter num3:"))
n = int(input("Enter n:"))

print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n])