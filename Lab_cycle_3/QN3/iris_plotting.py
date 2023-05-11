import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import random

file_path = "Lab_cycle_3\QN3\Iris.csv"
df = pd.read_csv(file_path)

# bar plot


def bar_plot():
    categories = df['Species'].value_counts()
    categories.plot(kind="bar", xlabel="frequency",
                    ylabel="species", color=['r', 'g', 'b'])


def pcaAppliedGraph():
    print("\nPCA Graph")
    # plotting the principal analysis graph for two components
    X = df.iloc[:, 1:5].values
    X_std = StandardScaler().fit_transform(X)
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(X_std)
    principalDf = pd.DataFrame(data=principalComponents, columns=[
                               'principal component 1', 'principal component 2'])
    finalDf = pd.concat([principalDf, df['Species']], axis=1)

    fig = plt.figure(figsize=(10, 8))
    figx = fig.add_subplot(1, 1, 1)
    figx.set_xlabel('First Principle Component')
    figx.set_ylabel('Second Principal Component')
    figx.set_title('PCA Graph')
    targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    colors = ['r', 'g', 'b']
    for target, color in zip(targets, colors):
        indicesToKeep = finalDf['Species'] == target
        figx.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
                     finalDf.loc[indicesToKeep, 'principal component 2'], c=color, s=50)
    figx.legend(targets)
    plt.show()


# array to store items to print as histogram
hist_array = []
for i in df.columns:
    if i == "Id" or i == "Species":
        continue
    else:
        hist_array.append(i)
print(hist_array)
color_list = ['r', 'g', 'b', 'black']


def histPlot(category):
    # iterate through color and removes once chosen
    clr = random.choice(color_list)
    color_list.remove(clr)

    # graph details
    df[category].hist(color=clr)
    plt.xlabel(f"{category}")
    plt.ylabel("Frequency")
    plt.title(category)
    plt.show()


bar_plot()
pcaAppliedGraph()

for j in hist_array:
    histPlot(j)
