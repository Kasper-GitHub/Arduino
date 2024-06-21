import numpy as np
import matplotlib.pyplot as plt

# Importing Data & Handling
data = np.genfromtxt("\Data_Oscillation.txt")
# Column Separation
timing = data[:250,0]
voltage = data[:250,1]
# Offset Adjustment
timing = timing - 15.8
voltage = voltage * 5

# Plotting
plt.figure(1)
plt.title('Plot of Voltage Output of Tracking Sensor')
plt.plot(timing, voltage, "b-", lw=0.5)
plt.grid(color='r',ls='--',lw=0.2)
# X-Axis (Time)
plt.xlabel('Time elapsed (s)')
plt.xlim([0,25.2])
plt.xticks(np.arange(0, 25.2))
# Y-Axis (Voltage)
plt.ylabel('Voltage (V)')
plt.ylim([0,5.2])
plt.yticks([0,5])
# Display
plt.show()
