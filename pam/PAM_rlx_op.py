import numpy as np
    
def PAM_Rlx_op(T1,T2,dt,M0):

    """This function returns the 4x4 homogenous coordinate expression for the relaxation operator
    event with a specified longitudinal magnetization relaxtion time (T1), transverse magnetization 
    relaxation time (T2), time step (dt), and an equilibrium Mz magnetization value (M0). 

    SYNTAX: dRlx_op = PAM_Rlx_op(T1,T2,dt,M0)

    INPUT:  T1 - longitudinal magnetization relaxtion time [s]
            T2 - transverse magnetization relaxtion time [s]
            dt - time step [s]
            M0 - Bulk magnetization equilibrium value [a.u.]
            
    OUTPUT: dRlx_op - Relaxation operator [4x4]
    
    NOTES:  None

    TO-DO:  Add default M0=1 value?

    DBE@Stanford 2019.09.02"""
    
# Define homogenous coordinate expression for the relaxation operator event
    dRlx_op = np.array([[np.exp(-dt/T2), 0             , 0             , 0                     ], 
                        [0             , np.exp(-dt/T2), 0             , 0                     ],
                        [0             , 0             , np.exp(-dt/T1), M0*(1-np.exp(-dt/T1)) ],
                        [0             , 0             , 0             , 1                     ]])

    return dRlx_op