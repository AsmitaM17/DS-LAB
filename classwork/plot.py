import matplotlib.pyplot as plt 
x = [1,2,3,4,5]
y1 = [5,15,25,35,45]
y2 = [10,30,20,40,50]
plt.plot (x, y1, marker = 'o', linestyle = '--', color = 'b', label = "line1")
plt.plot (x, y2, marker = '*', linestyle = '-', color = 'r', label = "line2")
plt.xlabel ("X-axis")
plt.ylabel ("Y-axis")
plt.title("Two line plot")
plt.legend()
plt.show()