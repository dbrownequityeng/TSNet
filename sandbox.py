import tsnet
import numpy as np 
# Open an example network and create a transient model
inp_file = './examples/networks/sandbox.inp'
valve_name =  "3-2"  
node_name = "3"
# inp_file = './examples/networks/sandbox.inp'
# valve_name =  "2A-2"  
# node_name = "2"
# Set valve closure
tc = 0.6 # valve closure period [s]
ts = 0 # valve closure start time [s]
se = 0 # end open percentage [s]
m = 1 # closure constant [dimensionless]
valve_op = [tc,ts,se,m]
#%%
tm = tsnet.network.TransientModel(inp_file)

# Set wavespeed
tm.set_wavespeed(1200.) # m/s
# Set time options
dt = 0.1  # time step [s], if not given, use the maximum allowed dt
tf = 60   # simulation period [s]
n = 6
tm.set_time_N(tf,n)

# Set valve closure
tm.valve_closure(valve_name, valve_op)

# Initialize steady state simulation
t0 = 0. # initialize the simulation at 0 [s]
engine = 'DD' # demand driven simulator
# tm = tsnet.simulation.Initializer(tm, t0, engine)
tm = tsnet.simulation.Initializer(tm,t0)
print("I AM HERE!")
# Transient simulation
tm = tsnet.simulation.MOCSimulator(tm)


node = node_name
head1 = tm.get_node(node).head

print(head1)