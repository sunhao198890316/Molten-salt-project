import numpy as np
import matplotlib.pyplot as plt

# Function to read Quantum ESPRESSO bands.dat file
def read_bands_dat(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    k_points = []
    band_energies = []

    for line in lines:
        columns = line.split()
        if len(columns) > 1:
            # First column is the k-point distance, subsequent columns are the band energies
            k_points.append(float(columns[0]))  # k-point distance
            band_energies.append([float(e) for e in columns[1:]])  # band energies

    return np.array(k_points), np.array(band_energies)

# Load k-points and band energies from bands.dat
k_points, band_energies = read_bands_dat('bands.dat')

# Plotting the band structure
plt.figure(figsize=(8, 6))

# Loop through each band and plot it
for i in range(band_energies.shape[1]):
    plt.plot(k_points, band_energies[:, i], color='blue')

# Optionally, define and add high-symmetry points
# For example, if high-symmetry points are known:
# high_symmetry_labels = ['Γ', 'X', 'W', 'Γ']
# high_symmetry_positions = [0, 10, 19, 20]  # Replace with actual positions
# plt.xticks([k_points[pos] for pos in high_symmetry_positions], high_symmetry_labels)

# Formatting the plot
plt.axhline(0, color='black', lw=0.5, ls='--')  # Fermi level (adjust as necessary)
plt.ylabel('Energy (eV)')
plt.title('Band Structure')
plt.grid(True)
plt.tight_layout()

# Save the figure as an image file
plt.savefig('band_structure.png', dpi=300)  # Saves as PNG with 300 DPI
# You can also save as PDF: plt.savefig('band_structure.pdf')

print("Plot saved as band_structure.png")

