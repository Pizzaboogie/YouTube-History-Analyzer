import data
import matplotlib.pyplot as plt
x=['January','February','March','April','May','June','July','August','September','October','November','December']
def dis():
    plt.plot(x,data.getdate(int(input("enter year:"))))
    plt.xlim(0,11)
    plt.ylim(ymin=0.0)
    plt.ylabel('Number of videos watched')
    plt.title('Number of Videos Watched Per Month')
    plt.show()