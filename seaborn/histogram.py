import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# tips = sns.load_dataset("tips")
# sns.histplot(tips["total_bill"])
# plt.title("Histogram of Total Bill")
# plt.xlabel("Total Bill ($)")
# plt.ylabel("Count")
# plt.show()

# 2
'''tips = sns.load_dataset("tips")
sns.histplot(tips["total_bill"],bins=20,kde=false)
plt.title("Histogram of Total Bill")
plt.xlabel("Total Bill ($)")
plt.ylabel("Count")
plt.show()'''

# 3
'''tips = sns.load_dataset("tips")
sns.histplot(tips["total_bill"],kde=True)
plt.title("Histogram of Total Bill")
plt.xlabel("Total Bill ($)")
plt.ylabel("Count")
plt.show()'''

# 4
'''tips = sns.load_dataset("tips")
sns.histplot(data=tips,x='total_bill',hue='sex',kde=True,palette='Set2')
plt.title("Histogram of Total Bill")
plt.xlabel("Total Bill ($)")
plt.ylabel("Count")
plt.show()'''

# 5
'''tips = sns.load_dataset("tips")
sns.histplot(tips["total_bill"],log_scale=True)
plt.title("Histogram of Total Bill")
plt.xlabel("Total Bill ($)")
plt.ylabel("Count")
plt.show()'''

# 6----iris
'''iris=sns.load_dataset("iris")
sns.histplot(iris['sepal_length'],kde=True)
plt.title("Sepal Length Distribution")
plt.xlabel("Sepal Length(cm)")
plt.ylabel("Species")
plt.show()'''