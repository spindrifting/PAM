import numpy as np
"""This file defines several configuration constants and variables for PAM
 
    SYNTAX: import PAM_config as PAM

    INPUT:  None
            
    OUTPUT: Many
    
    NOTES:  None

    DBE@Stanford 2019.09.08"""

# Physics -- https://en.wikipedia.org/wiki/Gyromagnetic_ratio
gamma_1H    =  42.577478518e6     # [MHz/T]
gamma_13C   =  10.7084e6
gamma_17O   =  -5.772e6
gamma_19F   =  40.052e6
gamma_23Na  =  11.262e6
gamma_31P   =  17.235e6
gamma_129Xe = -11.777e6

# Define 
eps = np.spacing(1)        # Epsilon used for floating point calculations

# Unit conversions
# Magnetic field strength
Gauss2Tesla=1/10000        # [Tesla/Gauss]
Tesla2Gauss=10000          # [Gauss/Tesla]

# Magnetic field gradient
# Gpcm_2mTpm =
# mTpm_2Gpcm =

# Magnetic field slew rate
# Tpmps_2mTpmpms = 
# mTpmpms_2Tpmps = 

# Boltzmann constant -- https://en.wikipedia.org/wiki/Boltzmann_constant
k_B = 1.38064852e-23 # [m^2.kg.s^-2.K^-1] = [J.K^-1]

# Planck's constant -- https://en.wikipedia.org/wiki/Planck_constant
h = 6.62607015e-34      # [m^2.kg.s^-1.cycle^-1] = [J.s.cycle^-1]
h_bar = 1.054571817e-34 # [m^2.kg.s^-1] = [J.s]



# mu=4*pi*1e-7;         % Permeability of free space [T.m/A]
# mu=1.25643*1e-6;      % Permeability of water [T.m/A]


# Graphics
color_Gx     = [0.81650, 0.40825, 0.40825]    # Red (G_x)
color_Gy     = [0.40825, 0.81650, 0.40825]    # Green (G_y)
color_Gz     = [0.40825, 0.40825, 0.81650]    # Blue (G_z)
color_B1     = [0.74278, 0.55709, 0.37139]    # Orange (RF)
color_Yellow = [0.66667, 0.66667, 0.33333]    # Yellow
color_Purple = [0.55709, 0.37139, 0.74278]    # Purple
color_Cyan   = [0.33333, 0.66667, 0.66667]    # Cyan