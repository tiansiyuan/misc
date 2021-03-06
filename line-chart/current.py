from matplotlib.pylab import  * 
filename = "d:\\wei\\exp\\current.dat"
X = load(filename)
dp = X[:, 0]
i_mea = X[:, 1]
i_mea_err = X[:, 2]
i_cal = X[:, 3]
i_cal_err = X[:, 4]
width = 3
h1 = bar(dp, i_mea, width, color='r', yerr=i_mea_err)
h2 = bar(dp+width, i_cal, width, color='b', yerr=i_cal_err)
xlabel('Particle diameter (nm)', fontsize=16)
xticks(dp+width, dp)
ylabel('Signal current (nA)', fontsize=16)
title('Measured current vs. calculated current')
legend((h1[0], h2[0]), ('measured current', 'calculated current'), loc=2)
savefig('current.png', dpi=75)
show()
