def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 :",source,"->",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,":",source,"->",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)

n = int(input("Enter the number of disks: "))
TowerOfHanoi(n,'A','B','C') 