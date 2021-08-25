number_of_row=n=int(input("Please enter the number of rows you want : "))
Khayyam_Pascal_triangle=[[None for i in range(n)]for j in range(n)]
for i in range(n):
    Khayyam_Pascal_triangle[i][0]=1
    Khayyam_Pascal_triangle[i][i]=1
for i in range(2,n):
    for j in range(1,i):
        Khayyam_Pascal_triangle[i][j]=Khayyam_Pascal_triangle[i-1][j]+Khayyam_Pascal_triangle[i-1][j-1]
for i in range(n):
    for j in range(i+1):
        print(Khayyam_Pascal_triangle[i][j],end='\t')
    for j in range(i+1,n):
        Khayyam_Pascal_triangle[i][j]="*"
        print(Khayyam_Pascal_triangle[i][j],end='\t')
    print()