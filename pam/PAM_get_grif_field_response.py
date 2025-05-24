# This function gets the field response from a measured GIRF
#
# dbe@stanford.edu
# mloecher@stanford.edu

def PAM_get_grif_field_response(g, H, pad_zeros=True, return_padded=False):
    """Convolves g with H in the frequency domain.
    
    Parameters
    ----------
    g : array_like
        The input gradient waveform to be convolved with the GIRF.
    H : array_like
        The GTF/filter to be applied in the frequency domain.
    pad_zeros : bool, optional
        If True, pads g with zeros to match the size of H.
        Default is True.
    return_padded : bool, optional
        If True, returns the padded version of g.
        Default is False.
    """
    if g.size < H.size and pad_zeros:
        N_pad = H.size - g.size
        pad_before = int(N_pad * 0.1)
        pad_after = N_pad - pad_before
        g = np.pad(g, (pad_before, pad_after), mode='constant')
    
    X = np.fft.fftshift(np.fft.fft(g))
    Y = X*H
    y = np.real(np.fft.ifft(np.fft.ifftshift(Y)))
    
    if pad_zeros and not return_padded:
        y = y[pad_before:-pad_after]

    return y