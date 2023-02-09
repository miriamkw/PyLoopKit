import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.colors import LinearSegmentedColormap

# Make a SEG like colormap
cmap=LinearSegmentedColormap.from_list('rg',[
    '#68AD32',
    '#A7E848',
    '#D7FE51',
    '#F0E84D',
    '#F3AD3C',
    '#E05927',
    '#BB261A',
    '#871910',
    '#480703'], N=256)

# Adjusts the amount of curve to use in normalizing bg values
bg_normalization_factor = 4

def normalize_bg(x):
    return np.power(np.log(x/600 + 1), 1.0/bg_normalization_factor)

def denormalize_bg(x):
    return (np.exp(np.power(x, bg_normalization_factor)) - 1) * 600

# Define grid
range = np.linspace(start=20, stop=600, num=100)
observed, predicted = np.meshgrid(range, np.flip(range))

# Normalize glucose values
observed = normalize_bg(observed)
predicted = normalize_bg(predicted)
target = normalize_bg(112)

# Amount of needed correction (in terms of normalized bg) for predicted and observed
correction = target - predicted
correction_ref = target - observed

# Difference in bg correction
correction_diff = correction - correction_ref

# Scale the difference relative to reference correction
scaled_correction = correction_diff / correction_ref

# Risk index
risk = np.abs(np.clip(scaled_correction, -1, 1))

plt.xlabel('observed')
plt.ylabel('predicted')
im = plt.imshow(risk, cmap=cmap, interpolation = 'none', extent=[20,600,20,600])
plt.colorbar(im)
plt.show()