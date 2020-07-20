import PAM_config as PAM

def PAM_hard_RF_grad_amp(alpha,rf_dur):
    """This function returns ... 

    SYNTAX: GMax = PAM_hard_RF_grad_amp(alpha,rf_dur)

    INPUT:  
            
    OUTPUT: 
    
    NOTES:  

    TO-DO:  

    DBE@Stanford 2019.09.09"""

    GMax = (alpha/360)/(PAM.gamma_1H*rf_dur)

    return GMax