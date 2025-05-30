# Design a simpe bipolar gradient waveform given the VENC and system hardware.
#
#
# dbe@stanford.edu
import numpy as np

def PAM_VENC2bipolar(venc, sys):
    """
    Generate a bipolar gradient waveform in T/m for a given VENC using system constraints.

    Parameters:
        venc : float
            Velocity encoding in cm/s.
        sys : dict
            Dictionary with system parameters:
                'sys['gamma']' : gyromagnetic ratio [Hz/T]
                'sys['gmax']'  : maximum gradient amplitude [T/m]
                'sys['smax']'  : maximum slew rate [T/m/s]
                'sys['dt']'    : time step [s]

    Returns:
        g_bipolar : ndarray
            Bipolar gradient waveform [T/m]
    """
    venc_mps = venc / 100.0  # Convert to [m/s]

    # Required first moment [s·m/T]
    M1_target = np.pi / (sys['gamma'] * venc_mps)

    # Design g_ramp time and samples
    ramp_time = sys['gmax'] / sys['smax']  # time to g_ramp to sys['gmax'] in [s]
    ramp_samples = int(np.ceil(ramp_time / sys['dt']))  # Number of samples on ramp [#]
    t_ramp = np.linspace(0, ramp_time, ramp_samples, endpoint=False)  # Times that accord with ramp steps [s]
    g_ramp = (sys['smax'] * t_ramp)  # Linear gradient ramp, g_ramp: g [T/m] = S_max [T/m/s] * t [s]

    # Initial g_lobe with g_ramp up and g_ramp down
    g_lobe = np.concatenate((g_ramp, g_ramp[::-1]))  # [T/m]

    # Bipolar waveform: positive g_lobe then negative g_lobe
    g_bipolar = np.concatenate((g_lobe, -g_lobe))

    # Time vector for current g_bipolar
    time = np.arange(len(g_bipolar)) * sys['dt']  # [s]
    M1 = np.sum(g_bipolar * time) * sys['dt']     # [s·m/T]

    # If M1 is too small, extend with flat top
    if M1 < M1_target:
        # Estimate flat-top duration needed
        remaining_M1 = M1_target - M1
        # Use sys['gmax'] to get time needed for flat top
        # For flat top, M1_flat = g * t_flat * (offset_time + 0.5*t_flat)
        t_flat = remaining_M1 / (sys['gmax'] * (time[-1] + 0.5 * sys['dt']))  # rough estimate
        flat_samples = int(np.ceil(t_flat / sys['dt']))
        flat = np.ones(flat_samples) * sys['gmax']

        # New g_lobe with flat top
        g_lobe = np.concatenate((g_ramp, flat, g_ramp[::-1]))
        g_bipolar = np.concatenate((g_lobe, -g_lobe))

        # Recompute M1 of extended g_lobe
    #    time = np.arange(len(g_bipolar)) * sys['dt']
    #    M1 = np.sum(g_bipolar * time) * sys['dt']

    # Time vector for bipolar
    time = np.arange(len(g_bipolar)) * sys['dt']
    M1_actual = np.sum(g_bipolar * time) * sys['dt']

    # Scale waveform to match exact target M1
    scale = M1_target / M1_actual
    g_bipolar *= scale

    # Final check
    if np.max(np.abs(g_bipolar)) > sys['gmax'] + 1e-6:
        raise ValueError(f"Gradient exceeds sys['gmax']: {np.max(np.abs(g_bipolar)):.4f} > {sys['gmax']} T/m")

    return g_bipolar