def slope(x,y,n):
    num = (n * sum([x[i]*y[i] for i in range(n)])) - sum(x)*sum(y)
    den = (n * sum([x[i]**2 for i in range(n)])) - sum(x)**2
    return num/den

phy = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
his = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15] 
print(round(slope(phy,his,len(phy)),3))
