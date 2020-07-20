import matplotlib.pyplot as plt
import PAM_config as PAM

def PAM_plot_mag(t,M):

    """This function plots the components of the magnetization. 

    SYNTAX: dRlx_op = PAM_Rlx_op(T1,T2,dt,M0)

    INPUT:  t - Time point vector [1,n] {s}
            M - Bulk magnetization vector [3,n] or [4,n] {a.u}
            
    OUTPUT: H - Graphics handle to figure
    
    NOTES:  None

    TO-DO:  None

    DBE@Stanford 2019.09.02"""
    
    H = plt.figure()
    plt.plot(t,M[0,:],color=PAM.color_Gx,linewidth=2)
    plt.plot(t,M[1,:],color=PAM.color_Gy,linewidth=2)
    plt.plot(t,M[2,:],color=PAM.color_Gz,linewidth=2)

    plt.xlabel('Time [s]')
    plt.ylabel('Magnetization [a.u]')
    plt.legend(['M_x','M_y','M_z'])
#    plt.savefig('PAM_Rlx_Example.pdf')  # Must place before plt.show()
    plt.show()
    
    return H