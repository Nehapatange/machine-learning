import math
x = [15,12,8,8,7,7,7,6,5,3]
y = [10,25,17,11,13,17,20,13,9,15]
xBar = sum(x)/len(x)
yBar = sum(y)/len(y)
x = [a-xBar for a in x]
y = [a-yBar for a in y]
b1 = sum([a*b for a,b in zip(x,y)])/sum([a*a for a in x]);
b0 = yBar - b1*xBar;
print(b0+b1*10)
