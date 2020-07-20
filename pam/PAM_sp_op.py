import numpy as np
    
def PAM_sp_op():

    """This function returns the 4x4 homogenous coordinate expression for a spoiler operator
    event. Perfect transverse magnetization spoiling is enforced by zeroing-out the transverse
    magnetization components.

    SYNTAX: PAM_sp_op

    INPUT : None
 
    OUTPUT: dSP    - Transverse magnetization spoiler event operator [4x4]
    
    NOTES : None
 
    TO-DO : None

    DBE@Stanford 2019.08.29"""

# Homogeneous expression for a spoiler operator
    dsp_op = np.array([[0,  0, 0, 0],
                       [0,  0, 0, 0], 
                       [0,  0, 1, 0], 
                       [0,  0, 0, 1]])

    return dsp_op
