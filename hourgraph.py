import data
import matplotlib.pyplot as plt
x=["7AM","8AM","9AM","10AM","11AM","12PM","1PM","2PM","3PM","4PM","5PM","6PM","7PM","8PM","9PM","10PM","11PM","12PM"]
def dis():
    plt.bar(x,data.gettime())
    plt.ylabel('Number of videos watched')
    plt.title('Number of Videos Watched Per Month')
    plt.show()