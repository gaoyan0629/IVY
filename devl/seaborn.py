import matplotlib.pyplot as plt
import pandas
import seaborn as sns
import numpy as np

data = pandas.DataFrame({"x": [1, 2, 4],
                        "y": [10,20,40],
                        "s": [10,10,10]}) # I increased your errors so I could see them

# Create a figure instance, and the two subplots
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

# Tell pointplot to plot on ax1 with the ax argument
sns.pointplot(x="x", y="y", data=data, ax=ax1)

# Plot the errorbar directly on ax1
ax1.errorbar(np.arange(len(data["x"])), data["y"], yerr=data["s"])

# Tell the factorplot to plot on ax2 with the ax argument
# Also store the FacetGrid in 'g'
g=sns.factorplot(x="x", y="y", data=data, ax=ax2)

# Close the FacetGrid figure which we don't need (g.fig)
plt.close(g.fig)

plt.show()


"""
import seaborn as sns
iris = sns.load_dataset('iris')
# plt.subplots() will generate new handler of figure
# while sns.subplots() will not
length_fig, length_ax = plt.subplots()
sns.barplot(x='sepal_length', y='species', data=iris, ax=length_ax)
length_fig.savefig('ex1.pdf')

width_fig, width_ax = plt.subplots()
sns.barplot(x='sepal_width', y='species', data=iris, ax=width_ax)
width_fig.savefig('ex2.pdf')
"""
