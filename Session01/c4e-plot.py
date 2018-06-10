import matplotlib

matplotlib.use("TkAgg")

from matplotlib import pyplot

#1. Prepare data
labels = ["iOs", "Android", "Web", "React Native"]
values = [20, 15, 40, 25]
colors = ["red", "green", "gold", "purple"]
explode = [0, 0, 0, 0.2]

#2. Plot
pyplot.pie(values,
            labels=labels, 
            colors=colors,
            explode=explode
            )
pyplot.axis("equal")

#3. Show
pyplot.show()