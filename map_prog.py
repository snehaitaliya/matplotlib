import matplotlib.pyplot as plt

# 1
'''x=[1,2,3,4,5,6]
y=[12,45,32,87,48,50]

plt.plot(x,y,color='green')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Line Graph")
plt.show()'''

# 2
"""x=['Amit','Neha','Rahul','Priya','Karan']
y=[75, 82, 68, 90, 80]

plt.plot(x, y, label='Marks', color='blue')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.title('Student Marks')
plt.legend()
plt.show()"""

# 3
'''x=['03-10-2016','04-10-2016','05-10-2016','06-10-2016','07-10-2016']
y=[700,600,577,499,900]

plt.plot(x,y,color='blue')
plt.title('Alphabet Inc. Stock Price')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()'''

# 4
'''x=[1,2,3,4,5]

y1=[2,4,6,8,10]
y2=[1,3,5,7,9]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")
plt.title('2 line graph on same plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()'''

# 5
'''x=[1,2,3,4,5]

y1=[2,4,6,8,10]
y2=[1,3,5,7,9]

plt.plot(x,y1,color='red',linewidth=3,label='Line 1')
plt.plot(x,y2,color='blue',linewidth=5,label='Line 2')
plt.title('Different width')
plt.legend()
plt.show()'''

# 6
'''x=[1,2,3,4,5]

y1=[2,4,6,8,10]
y2=[1,3,5,7,9]

plt.plot(x, y1,linestyle='-.', label='Dashed line',color='green')
plt.plot(x, y2,linestyle=':', label='Dotted line',color='blue')
plt.title('Different Style Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()'''

# 7
'''x=[1,2,3,4,5]

y1=[2,4,6,8,10]
y2=[1,3,5,7,9]

plt.plot(x, y1, marker="o", label="Circle Marker",color='magenta')
plt.plot(x, y2, marker="s", label="Square Marker",color='green')
plt.title('Marker Style Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()'''

# 8
'''x=[1,2,3,4,5]
y=[10,20,30,40,50]

plt.plot(x, y)
plt.axis([0,6,0,60])
plt.title('Add New Axis')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()'''

# 9
'''x=[1,2,3,4,5]
y=[5,10,15,20,25]

plt.plot(x,y)
plt.title('Line Graph')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()'''

# 10
'''x=['Python','Java','C','C++','JavaScript']
y=[90,15,65,60,5]

plt.bar(x,y,color=['pink','green','blue','orange','red'])
plt.title("Popularity of Programming Languages")
plt.xlabel('Programming Languages')
plt.ylabel('Popularity(%)')
plt.show()'''