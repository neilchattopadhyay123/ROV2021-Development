import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import psutil

start = time.time()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xax = []
yax = []

def animate(i, xax, yax):
    cpu = psutil.cpu_percent()
    xax.append(time.time()-start)
    yax.append(cpu)
    xax = xax[-100:]
    yax = yax[-100:]
    ax.clear()
    ax.plot(xax, yax)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('LAG TESTER')
    plt.ylabel('CPU USAGE')
    
ani = animation.FuncAnimation(fig, animate, fargs=(xax, yax), interval=1000)
plt.show()