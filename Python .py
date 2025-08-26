import pandas as pd
import matplotlib.pyplot as plt
data : {"Name":["bunny","minny","sweety","charan","akshay","surya"],"Gender":["female","female ","female ","male","male","male"]}
df=pd.DataFrame(data)
df["Gender"].hist(color="yellow",edgecolor="black")
plt.title("Gender distribution")
plt.xlabel("Gender")
plt.ylabel("count")
plt.show()
