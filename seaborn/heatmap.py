import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# data=np.array([[10,20,30,40],[30,40,50,60],[50,60,70,80],[70,80,90,100]])
# sns.heatmap(data,annot=True,fmt='d',cmap='YlGnBu',cbar=True)
# plt.title("heatmap example")
# plt.xlabel("Features")
# plt.ylabel("Sample")
# plt.show()

# 1
'''data=np.array([[10,20,30,40],[30,40,50,60],[50,60,70,80],[70,80,90,100]])
sns.heatmap(data,annot=True,fmt='d',cmap='Blues',cbar=True)
plt.title("heatmap example")
plt.xlabel("Features")
plt.ylabel("Sample")
plt.show()'''

# 2
'''data=np.array([[10,20,30,40],[30,40,50,60],[50,60,70,80],[70,80,90,100]])
sns.heatmap(data,annot=True,fmt='d',cmap='YlOrRd',cbar=True)
plt.title("heatmap example")
plt.xlabel("Features")
plt.ylabel("Sample")
plt.show()'''

# 3
'''data=np.array([[10,20,30,40],[30,40,50,60],[50,60,70,80],[70,80,90,100]])
sns.heatmap(data,annot=True,fmt='d',cmap='viridis',cbar=True)
plt.title("heatmap example")
plt.xlabel("Features")
plt.ylabel("Sample")
plt.show()'''

# 4
'''data=np.array([[10,20,30,40],[30,40,50,60],[50,60,70,80],[70,80,90,100]])
sns.heatmap(data,annot=True,fmt='d',cmap='magma',cbar=False)
plt.title("heatmap example")
plt.xlabel("Features")
plt.ylabel("Sample")
plt.show()'''

# 5
'''data=np.array([[10,20,30,40],[30,40,50,60],[50,60,70,80],[70,80,90,100]])
sns.heatmap(data,annot=True,fmt='d',xticklabels=['A','B','C','D'],yticklabels=['W','X','Y','Z'],cmap='GnBu',cbar=True)
plt.title("heatmap example")
plt.xlabel("Features")
plt.ylabel("Sample")
plt.show()'''

# 6
'''data=np.array([[10,20,30,40],[30,40,50,60],[50,60,70,80],[70,80,90,100]])
mask=np.triu(np.ones_like(data,dtype=bool))
sns.heatmap(data,mask=mask,annot=True,cmap='coolwarm',cbar=True)
plt.title("heatmap example")
plt.xlabel("Features")
plt.ylabel("Sample")
plt.show()'''n