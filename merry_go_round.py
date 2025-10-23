import vpython as vp
import numpy as np
import rotations as rot

Rp = np.matrix('.2; 0; 0')
Rn = np.matrix('2; 0; 0')
rm = np.matrix('-3; 1; 0')

n = 400
theta, alpha = 0, 0
dtheta = 2*np.pi/n
dalpha = 50*np.pi/n

rp = rm + Rn + Rp
point = vp.sphere(radius=.1, make_trail=True, retain=50, pos=rot.np2vp(rp))
you = vp.cone(axis=vp.vector(0,0,1), radius=0.25, pos=vp.vector(0,0,-.5), color=vp.color.cyan)
m = vp.cylinder(color=vp.color.blue, radius= 2.2, pos=rot.np2vp(rm-np.matrix('0;0;.5')), axis=vp.vector(0,0,.1))
b = vp.box(color=vp.color.red, pos=rot.np2vp(rm+np.matrix('1;0;-.25')), size=vp.vector(2,.1,.5))
mgr = vp.compound([m, b])

while True:
    vp.rate(20)
    theta += dtheta
    alpha += dalpha
    rp = rm + rot.Cz(theta).transpose()*Rn + rot.Cz(theta).transpose()*rot.Cy(alpha).transpose()*Rp
    point.pos = rot.np2vp(rp)

    mgr.rotate(dtheta, axis=vp.vector(0,0,1))