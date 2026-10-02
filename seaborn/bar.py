import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# tips = sns.load_dataset("tips")
# sns.barplot(data=tips,x="day",y="total_bill")
# plt.title("Average Total Bill by Day")
# plt.xlabel("Day")
# plt.ylabel("Total Bill ($)")
# plt.show()

# 1
'''tips=sns.load_dataset("tips")
sns.barplot(data=tips, x="day", y="total_bill")
plt.title("Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()'''

# 2
'''tips=sns.load_dataset("tips")
sns.barplot(data=tips, x="day", y="total_bill", hue="sex")
plt.title("Total Bill by Day and Sex")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()'''

# 3
'''tips=sns.load_dataset("tips")
sns.barplot(data=tips, y="day", x="total_bill", orient="h")
plt.title("Total Bill by Day (Horizontal)")
plt.xlabel("Total Bill ($)")
plt.ylabel("Day")
plt.show()'''

# 4
'''tips = sns.load_dataset("tips")
sns.barplot(data=tips,x="day",y="total_bill",estimator=sum,errorbar=None)
plt.title("Sum of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()'''

# 5
'''tips = sns.load_dataset("tips")
order = ["Sun","Sat","Fri","Thur"]
palette = "coolwarm"
sns.barplot(data=tips,x="day",y="total_bill",order=order,palette=palette)
plt.title("Total Bill by Day (Custom)")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()'''

# 6
"""iris=sns.load_dataset("iris")
sns.barplot(data=iris,x="species",y="sepal_length")
plt.title("Average Sepal Length By Species")
plt.xlabel("Sepal Length(cm)")
plt.ylabel("Species")
plt.show()"""