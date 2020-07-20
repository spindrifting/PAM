import numpy as np

def PAM_Gr_op(gamma,G_amp,dt,pos):

    """This function returns the 4x4 homogenous coordinate expression for a gradient operator
    event with a specified gradient amplitude (G_amp) and duration (dt) acting on a spin at
    position (p) with a specific gyromagnetic ratio (gamma). 

    SYNTAX: dGr_op = PAM_Gr_op(gamma,G_amp,dt,pos) 

    INPUT : gamma - gyromagnetic ratio [Hz/T]
            G_amp - Gradient vector    [G/cm] (3x1)
            dt    - time step          [s]
            pos   - spin position      [cm]   (3x1)
 
    OUTPUT: dG_op - Gradient event operator [4x4]
    
    NOTES : ###As expected the rotation is X-handed...
 
    TO-DO : NEGATIVE sign on PHI and in MATRIX? Confirm.
            Better to call this dGr_op...and dB1_op?
            POSITION not defined nor used

    DBE@Stanford 2019.08.29"""

# Angle of rotation imparted on the spin by the gradient
    phi = -2*np.pi*gamma*(np.dot(G_amp,pos)/10000)*dt # Convert gauss to Tesla

# Homogeneous expression for the GRADIENT MATRIX
    dGr_op = np.array([[np.cos(np.deg2rad(phi)),  -np.sin(np.deg2rad(phi)), 0, 0], 
                      [np.sin(np.deg2rad(phi)),   np.cos(np.deg2rad(phi)), 0, 0], 
                      [0                      ,   0                      , 1, 0], 
                      [0                      ,   0                      , 0, 1]])

    return dGr_op