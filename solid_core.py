# Nuclear Thermal Rocket Propulsion calculations
# Solid Core 1 bar H2 rocket.
from propellants import H2
from mach import *

g = 9.80655

# propellant info
prop = H2()
mdot_prop = 10 # kg s-1
T_prop0 = 60 # K

# reactor info
reactor_output = 150E6 # W
reactor_eff = 0.8 # efficiency

# thrust chamber info
expansion_ratio = 16 # exit area / throat area

Q_dot = reactor_output * reactor_eff # W
q_dot = Q_dot / mdot_prop # J kg-1 s-1

h2 = prop.get_h(T_prop0) + q_dot
T_c = prop.get_T_by_h(h2)

gamma = prop.get_gamma(T_c)
M_exit = calc_mach_num(expansion_ratio, gamma)
T_exit = (1 + (gamma-1)/2 * M_exit**2)**(-1) * T_c
V_exit = M_exit * prop.get_speed_of_sound(T_exit)

F_thrust = mdot_prop * V_exit

Isp = V_exit/g

print("- - - INPUTS - - -")
print("Reactor power:", reactor_output, "W")
print("Reactor efficiency:", reactor_eff)
print("Propellant:", prop.get_name())
print("Propellant feed rate:", mdot_prop, "kg/s")
print("Propellant feed temp:", T_prop0, "K")
print("Expansion ratio:", expansion_ratio)
print("")
print("- - - OUTPUTS - - -")
print("Propellant chamber end temp:", T_c, "K")
print("Exit Mach number:", M_exit)
print("Exit temp:", T_exit, "K") 
print("Exhaust vel:", V_exit, "m/s")
print("Thrust:", F_thrust, "N")
print("Isp:", Isp, "s")
