import matplotlib.pyplot as plt
import math

pi = math.pi
spin = 1

R = 2000
V = 90

dD = 1/500 #this is in mm/mm
Deq = 11.8 * V*V/R #this is in mm
L = Deq / dD / 1000 #this is divided by 1000 to convert from mm to m
A = math.sqrt(R * L) # in m
n = 10000
dS = L/n
x0 = 0
y0 = 0
s0 = 0
a0 = 0 #the start angle
sn = 0
x_cd = []
y_cd = []

circ_x_cd = []
circ_y_cd = []

a = 2*A*A
x = x0
y = y0
for i in range(0,n+1):
    dx = dS * math.cos(spin * sn*sn/a + a0)
    dy = dS * math.sin(spin * sn*sn/a + a0)
    sn += math.sqrt(dx*dx + dy*dy)
    
    x += dx
    y += dy
    x_cd.append(x)
    y_cd.append(y)
    
    r = A*A/sn #the radius at curve length s
    

    
    if r <= R: #starts at a large radius of r when straight line

        if dy > 0:
            offset_x_direction = -spin
        else:
            offset_x_direction = spin
                
        final_gradient = dy/dx
        final_normal = -1/final_gradient 
        circ_offset_x = offset_x_direction * R/math.sqrt(final_normal*final_normal + 1) 
        circ_offset_y = final_normal * circ_offset_x       
        circ_x0 = circ_offset_x + x
        circ_y0 = circ_offset_y + y
        
        for i in range(0,360):
            angle = (2 * pi) / 360 * i
            circ_x = circ_x0 + R*math.cos(angle) 
            circ_y = circ_y0 + R*math.sin(angle)
            circ_x_cd.append(circ_x)
            circ_y_cd.append(circ_y)
        break

fig= plt.figure()

axes= fig.add_axes([0,0,1,1])

axes.plot(x_cd,y_cd, color='purple', linewidth=3)
axes.plot(circ_x_cd,circ_y_cd, color='green', linewidth=2)
plt.axis('square')
plt.show()

# plt.plot(x_cd, y_cd, circ_x_cd, circ_y_cd)
# plt.axis('square')
# plt.show()
