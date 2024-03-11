import matplotlib.pyplot as plt
import numpy as np
import pickle

##------------------------------------------------------------------------------
## Script to plot SASA for multiple runs
##------------------------------------------------------------------------------

# open pickled files
files = ["C88_single_MD_SASA", "C88_single_85C_MD_SASA", "C108_single_MD_SASA"]
labels = ["bC8$_8$ (RT)", "bC8$_8$ (85 °C)", "bC8$_{10}$ (RT)"]
data = []

# plot
plt.rc('xtick', labelsize=25)
plt.rc('ytick', labelsize=25)
plt.rc('lines', linewidth=3)
plt.rc('legend', fontsize=20, loc="upper right")
# fig, axs = plt.subplots(3, sharex=True, sharey=True, figsize=(15, 11))
# axs[0].set_ylim([0.6,1.2])
# axs[0].set_xlim([-5,305])
# axs[0].set_yticks([0.7, 0.85, 1, 1.15])

fig = plt.figure(dpi=300, figsize=(15,11))
ax1 = fig.add_subplot(111)

ax1.set_ylim([0.6,1.2])
ax1.set_xlim([-5,305])
ax1.set_yticks([0.7, 0.85, 1, 1.15])

for file in files:
    data.append(pickle.load(open("../data/"+file+".p", "rb")))

# axs[2].set(xlabel="Time (ps)")
# fig.suptitle("SASA", weight="bold")
# for i, ax in enumerate(axs.flat):
#     ax.set(ylabel=labels[i])

x_ticks = [i/10 for i, x in enumerate(data[0])]


# print(x_ticks)

# axs[0].plot(x_ticks, [i/data[0][0] for i in data[0]], 'darkorange', label=labels[0])
# axs[1].plot(x_ticks, [i/data[1][0] for i in data[1]], 'maroon', label=labels[1])
# axs[2].plot(x_ticks, [i/data[2][0] for i in data[2]], 'dimgray', label=labels[2])

ax1.plot(x_ticks, [i/data[0][0] for i in data[0]], 'indianred', marker='^', alpha=0.4, label=labels[0])
ax1.plot(x_ticks, [i/data[1][0] for i in data[1]], 'maroon', marker='^', alpha=0.4, label=labels[1])
ax1.plot(x_ticks, [i/data[2][0] for i in data[2]], 'steelblue', marker='^', alpha=0.4, label=labels[2])

# leg1 = axs[0].legend()
# leg2 = axs[1].legend()
# leg3 = axs[2].legend()
# leg1.get_lines()[0].set_linewidth(6)
# leg2.get_lines()[0].set_linewidth(6)
# leg3.get_lines()[0].set_linewidth(6)

leg1 = ax1.legend()
leg1.get_lines()[0].set_linewidth(6)



# plt.show()
plt.savefig("../figs/individual_SASA.png", transparent=True, bbox_inches='tight')
