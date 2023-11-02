import matplotlib.pyplot as plt             # plotting date
import matplotlib.gridspec as gridspec      # setting up the graph
import matplotlib.animation as animation    # make the animation
import numpy as np                          # working with array

# setting up the duration of the animation

t_start = 0     #[hrs]
t_end = 2       #[hrs]
t_step = 0.005  #[hrs]

# array that rappresent the time 

t = np.arange(t_start,t_end+t_step,t_step) #[hrs]

# array that rappresent the distance travelled x-coordinate

speed = 800     #[km/hrs]

x = t*speed

# array that rappresent the heigth y-coordinate

height = 2     #[km]

y = np.ones(len(t))*height   #[km]


# setting up the animation

# frame amount 
frame_amount = len(t)

def update_plot(num):
    plane_trajectory.set_data(x[0:num],y[0:num])

    return plane_trajectory,

fig = plt.figure(figsize=(16,9), dpi=120, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)

# subplot 1 

ax0 = fig.add_subplot(gs[0:],facecolor=(0.9,0.9,0.9))
plane_trajectory, = ax0.plot([],[],'g',linewidth=2)
ax0.set_xlim(x[0],x[-1])
ax0.set_ylim(y[0],y[-1])

# plane animation

plane_animation = animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=True,blit=True)

plt.show()
