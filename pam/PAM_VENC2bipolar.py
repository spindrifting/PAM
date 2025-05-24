# Design a simpe bipolar gradient waveform given the VENC and system hardware.
#
#
# dbe@stanford.edu
import numpy as np

def PAM_VENC2bipolar(venc, sys):
    """
    Generate a bipolar gradient waveform for a given VENC using system constraints.

    Parameters:
        venc : float
            Velocity encoding in cm/s.
        sys : dict
            Dictionary with system parameters:
                'gamma' : gyromagnetic ratio [Hz/T]
                'gmax'  : maximum gradient amplitude [T/m]
                'smax'  : maximum slew rate [T/m/s]
                'dt'    : time step [s]

    Returns:
        gg : ndarray
            Bipolar gradient waveform [T/m]
    """
    # Convert VENC to m/s
    venc_mps = venc / 100.0

    # Extract system parameters
    gamma = sys['gamma']
    gmax = sys['gmax']
    smax = sys['smax']
    dt = sys['dt']

    # Compute required M1
    M1_target = np.pi / (gamma * venc_mps)  # [T·s²/m]

    # Generate basic triangular gradient lobe
    ramp_time = gmax / smax  # [s]
    ramp_samples = int(np.ceil(ramp_time / dt))

    # Triangular lobe: ramp up and ramp down
    ramp_up = np.linspace(0, gmax, ramp_samples, endpoint=False)
    ramp_down = np.linspace(gmax, 0, ramp_samples, endpoint=False)
    lobe = np.concatenate((ramp_up, ramp_down))

    # Bipolar: positive lobe followed by negative lobe
    gg = np.concatenate((lobe, -lobe))

    # Compute M1 of this waveform
    time = np.arange(len(gg)) * dt
    M1_actual = np.sum(gg * time) * dt

    # Scale to achieve target M1
    scaling = M1_target / M1_actual
    gg *= scaling

    # Safety check
    if np.max(np.abs(gg)) > gmax:
        raise ValueError("Required VENC cannot be achieved within gmax/smax limits.")

    return gg