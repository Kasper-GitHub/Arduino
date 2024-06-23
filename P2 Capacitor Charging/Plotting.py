import numpy as np
import matplotlib.pyplot as plt

# Initialization & Constants
r = 120000.0
c = 1E-06
tau = r * c
v_o = 5.0
voltage_expt = []
voltage_theo= []

# Importing Data & Handling
data_expt = np.genfromtxt('\Data_Capacitor_Charging.txt',delimiter='\t')
# Column Separation
time_data = data_expt[:,0]/1000     # Conversion from milisecond to second
voltage_data = data_expt[:,1]

# Storing experimental & theoritical voltages across capacitor
for i in range(len(time_data)):
    v_t_expt = voltage_data[i]
    v_t_theo = v_o - v_o * (np.exp((-time_data[i])/(tau)))
    voltage_expt.append(v_t_expt)
    voltage_theo.append(v_t_theo)

# Plotting
plt.figure(1)
plt.title("Case Study : Charging of Capacitor in R-C Circuit")
plt.grid(color='r',ls='--',lw=0.2)
plt.plot(time_data,voltage_theo,"g--",lw=1.5,label='Theoretical')
plt.plot(time_data,voltage_data,'b-',lw=1,label='Experimental')
# X-Axis (Time)
plt.xlabel('Time (s)')
plt.xlim(0,max(time_data)/30)       # Focussing on initial charging state
# Y-Axis (Voltage)
plt.ylabel('Voltage across capacitor (V)')
plt.ylim(0,5.5)
# Checkpoint : 63.2% voltage at tau
plt.vlines(tau,0,0.632*v_o,colors="black",ls="--",lw=0.7)
plt.hlines(0.632*v_o,0,tau,colors="black",ls="--",lw=0.7)
# Checkpoint : 99.3% voltage at 5*tau
plt.vlines(5*tau,0,0.993*v_o,colors="black",ls="--",lw=0.7)
plt.hlines(0.993*v_o,0,5*tau,colors="black",ls="--",lw=0.7)
# Display
plt.legend(loc=4)
plt.show()
