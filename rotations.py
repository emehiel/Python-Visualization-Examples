import numpy as np
import vpython as vp

def Cx(theta):
    st = np.sin(theta)
    ct = np.cos(theta)
    return np.matrix([[1, 0, 0],[0, ct, st,],[0, -st, ct]])

def Cy(theta):
    st = np.sin(theta)
    ct = np.cos(theta)
    return np.matrix([[ct, 0, -st],[0, 1, 0,],[st, 0, ct]])

def Cz(theta):
    st = np.sin(theta)
    ct = np.cos(theta)
    return np.matrix([[ct, st, 0],[-st, ct, 0,],[0, 0, 1]])

def np2vp(vpVec):
    return vp.vector(vpVec[0,0], vpVec[1,0], vpVec[2,0])