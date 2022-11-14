import data
import matplotlib.pyplot as plt
x=['January','February','March','April','May','June','July','August','September','October','November','December']
y=data.getdate(int(input("Year:")))
todel=[i for i in range(len(y)) if y[i]==0]
for i in todel:
    x.pop(i)
    y.pop(i)
def dis():
    plt.pie(y,labels=x)
    plt.title('Number of Videos Watched Per Month')
    plt.show()
