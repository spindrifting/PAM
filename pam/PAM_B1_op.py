import numpy as np
    
def PAM_B1_op(gamma,B1_amp,dt,theta):

    """This function returns the 4x4 homogenous coordinate expression for an RF operator
    event with a specified B1 amplitude (B1_amp), duration (dt), and phase (theta) for a 
    specific gyromagnetic ratio (gamma). 

    SYNTAX: dB1_op = PAM_B1_op(gamma,B1_amp,dt,theta)

    INPUT:  gamma  - gyromagnetic ratio [Hz/T]
            B1_amp - B1 amplitude       [T]
            dt     - time step          [s]
            theta  - phase angle        [radians]
            
    OUTPUT: dB1_op - RF (B1) pulse operator [4x4]
    
    NOTES:  THETA=0 is phased about the X-axis and THETA=90 is phased about the Y-axis.

    TO-DO:  Update to accept complex pairs, rather than phase angle...
            Naming convention...dRF vs dB1?
            Allow for inputs to be a vector? Therefore make a waveform?
            ****TRIPLE CHECK UNITS ESPECIALLY ALPHA BEFORE USE****

    DBE@Stanford 2019.08.25"""
    
# Define the incremental flip angle [degrees] in time dt [s]
    alpha = 2*np.pi*gamma*B1_amp*dt

# Define the homogenous RF operator
# Change of basis
    R_theta = np.array([[np.cos(-np.deg2rad(theta)),  -np.sin(-np.deg2rad(theta)), 0, 0], 
                        [np.sin(-np.deg2rad(theta)),   np.cos(-np.deg2rad(theta)), 0, 0], 
                        [0                         ,   0                         , 1, 0], 
                        [0                         ,   0                         , 0, 1]])

# Flip angle rotation
    R_alpha = np.array([[1,  0                        , 0                        , 0], 
                        [0,  np.cos(np.deg2rad(alpha)), np.sin(np.deg2rad(alpha)), 0],
                        [0, -np.sin(np.deg2rad(alpha)), np.cos(np.deg2rad(alpha)), 0],
                        [0,  0                        , 0                        , 1]])

# Composite homogeneous expression for RF MATRIX
    dB1_op = R_theta.transpose()@R_alpha@R_theta

    return dB1_op