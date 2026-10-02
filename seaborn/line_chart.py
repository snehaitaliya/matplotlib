import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# tips=sns.load_dataset('tips')
# sns.lineplot(data=tips,x='total_bill',y='size',dashes=True)
# plt.title('average total bill')
# plt.xlabel('day')
# plt.ylabel('bill')
# plt.show()

# 1
'''x=[1,2,3,4,5]
y=[10,20,30,40,50]
sns.lineplot(x=x,y=y)
plt.title('Simpole Line Plot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()'''

# 2
'''tips=sns.load_dataset("tips")

sns.lineplot(data=tips,x="day",y="total_bill",hue="sex",marker="o")
plt.title("Line Plot with Hue (Sex)")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()'''

# 3
'''tips = sns.load_dataset("tips")

sns.lineplot(data=tips,x="day",y="total_bill",style="smoker",marker="o",dashes=False)
plt.title("Line Plot with Style (Smoker)")
plt.xlabel("Day")
plt.ylabel("Total Bill($)")
plt.show()
'''

# 4
'''tips = sns.load_dataset("tips")

sns.lineplot(data=tips,x="day",y="total_bill",estimator="mean",errorbar=("ci", 95),marker="o")
plt.title("Line Plot with CI (95%)")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()'''

# 5
'''tips = sns.load_dataset("tips")

sns.lineplot(data=tips,x="day",y="total_bill",hue="sex",style="smoker",marker="o",dashes=True,linewidth=2)
plt.title("Customized Line Plot")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()'''



