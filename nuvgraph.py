import data
watsubs=data.watchedsubs()
import matplotlib.pyplot as plt

def dis():
    plt.bar([i[1] for i in watsubs],[i[0] for i in watsubs],color=['#0096FF','#6495ED','#1434A4','#191970','#4169E1','green','black'])
    plt.xlabel('Channels')
    plt.ylabel('Number of videos watched')
    plt.title('Most Watched Subcribers')
    plt.show()
