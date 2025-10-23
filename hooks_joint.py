import numpy as np
import vpython as vp

vp.scene.width = 1400
vp.scene.height = 800
#vp.scene.fullscreen = True

x_axis = vp.arrow(axis=vp.vector(1,0,0), round=True, color=vp.color.red)
y_axis = vp.arrow(axis=vp.vector(0,1,0), round=True, color=vp.color.green)
z_axis = vp.arrow(axis=vp.vector(0,0,1), round=True, color=vp.color.blue)

alpha = 20*vp.pi/180.0

h1 = vp.cylinder(pos=vp.vec(0,0,0), axis=vp.vec(2,0,0), radius=.1)
h2 = vp.cylinder(pos=vp.vec(2,0,-1), axis=vp.vec(0,0,2), radius=.1)
h3 = vp.cylinder(pos=vp.vec(2,0,-1), axis=vp.vec(1,0,0), radius=.1)
h4 = vp.cylinder(pos=vp.vec(2,0,1), axis=vp.vec(1,0,0), radius=.1)
ring1 = vp.ring(pos=vp.vector(3.2,0,-1), axis=vp.vector(0,0,1), color=vp.color.blue)
ring2 = vp.ring(pos=vp.vector(3.2,0,1), axis=vp.vector(0,0,1), color=vp.color.red, radius=.2, thikness=.1)
ring1.radius = .2
ring1.thickness = .1
ring2.radius = .2
ring2.thickness = .1
hook2 = vp.compound([h1, h2, h3, h4, ring1, ring2])

c1 = vp.cylinder(pos=vp.vec(3.2,0,-1), axis=vp.vec(0,0,2), radius=.1)
c2 = vp.cylinder(pos=vp.vec(3.2,1,0), axis=vp.vec(0,-2,0), radius=.1)
cross = vp.compound([c1, c2])

h1 = vp.cylinder(pos=vp.vec(0,0,0), axis=vp.vec(2,0,0), radius=.1)
h2 = vp.cylinder(pos=vp.vec(2,0,-1), axis=vp.vec(0,0,2), radius=.1)
h3 = vp.cylinder(pos=vp.vec(2,0,-1), axis=vp.vec(1,0,0), radius=.1)
h4 = vp.cylinder(pos=vp.vec(2,0,1), axis=vp.vec(1,0,0), radius=.1)
ring1 = vp.ring(pos=vp.vector(3.2,0,-1), axis=vp.vector(0,0,1), color=vp.color.blue)
ring2 = vp.ring(pos=vp.vector(3.2,0,1), axis=vp.vector(0,0,1), color=vp.color.red, radius=.2, thikness=.1)
ring1.radius = .2
ring1.thickness = .1
ring2.radius = .2
ring2.thickness = .1
hook3 = vp.compound([h1, h2, h3, h4, ring1, ring2])

hook3.rotate(vp.pi/2, vp.vec(1,0,0))
hook3.rotate(vp.pi, vp.vec(0,1,0), origin=vp.vec(3.2,0,0))
hook3.rotate(alpha, vp.vec(0,1,0), origin=vp.vec(3.2,0,0))

vp.scene.camera.pos=vp.vec(3.2,-5,0)
vp.scene.camera.axis=vp.vec(0,1,0)
vp.scene.camera.up=vp.vec(0,0,1)

x_c = vp.arrow(pos=vp.vector(3.2,0,0), axis=vp.vector(1.5,0,0), round=True, color=vp.color.red, make_trail=True)
point_x_c = vp.sphere(radius=.01, make_trail=True, retain=100, pos=x_c.pos + x_c.axis, color=vp.color.red)
y_c = vp.arrow(pos=vp.vector(3.2,0,0), axis=vp.vector(0,1.5,0), round=True, color=vp.color.green)
point_y_c = vp.sphere(radius=.01, make_trail=True, retain=200, pos=y_c.pos + y_c.axis, color=vp.color.green)
z_c = vp.arrow(pos=vp.vector(3.2,0,0), axis=vp.vector(0,0,1.5), round=True, color=vp.color.blue)
point_z_c = vp.sphere(radius=.01, make_trail=True, retain=200, pos=z_c.pos + z_c.axis, color=vp.color.blue)

x_3 = vp.arrow(pos=vp.vector(3.2,0,0), axis=vp.vector(1.5,0,0), round=True, color=vp.color.red)
x_3.rotate(alpha, vp.vec(0,1,0))

theta_i = 0
theta_old = 0
beta = -alpha
beta_old = beta
dtheta_i = .01
while True:
    vp.rate(50)

    hook2.rotate(dtheta_i, vp.vec(1,0,0))
    #cross.rotate(dtheta_i, vp.vec(1,0,0))
    #cross.rotate(beta, vp.vec(1,0,0))
    theta_i += dtheta_i
    cb = vp.sqrt(1-vp.sin(alpha)**2 * vp.cos(theta_i)**2)
    y = vp.sin(theta_i)
    x = vp.cos(alpha)*vp.cos(theta_i)
    theta_o = vp.atan2(y/cb, x/cb)
    dtheta_o = theta_o - theta_old
    theta_old = theta_o
    beta = vp.atan2(-vp.sin(alpha)*vp.cos(theta_i), vp.sin(theta_i)/vp.sin(theta_o))
    dbeta = beta - beta_old
    beta_old = beta

    x_c.rotate(dtheta_o, x_3.axis)
    y_c.rotate(dtheta_o, x_3.axis)
    z_c.rotate(dtheta_o, x_3.axis)

    x_c.rotate(dbeta, y_c.axis)
    y_c.rotate(dbeta, y_c.axis)
    z_c.rotate(dbeta, y_c.axis)

    point_x_c.pos = x_c.pos + x_c.axis
    point_y_c.pos = y_c.pos + y_c.axis
    point_z_c.pos = z_c.pos + z_c.axis

    cross.rotate(dtheta_o, x_3.axis)
    cross.rotate(dbeta, y_c.axis)
   
    hook3.rotate(dtheta_o, vp.rotate(vp.vec(1,0,0), alpha, vp.vec(0,1,0)))