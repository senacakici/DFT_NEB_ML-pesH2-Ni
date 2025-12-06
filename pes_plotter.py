import os
import re
import matplotlib.pyplot as plt

# Slab ve H2 gaz fazı enerji referanslarını oku
with open("slab_energy.txt", "r") as f:
    slab_energy = float(f.read().strip())

with open("h2_gas_energy.txt", "r") as f:
    h2_gas_energy = float(f.read().strip())

# Hesaplanmış enerji dosyalarını sırala
energy_files = sorted(
    [f for f in os.listdir() if f.startswith("calc_") and f.endswith(".txt")],
    key=lambda x: float(x.replace("calc_", "").replace(".txt", ""))
)

distances = []
adsorption_energies = []

for file_name in energy_files:
    distance = float(file_name.replace("calc_", "").replace(".txt", ""))
    with open(file_name, "r") as file:
        content = file.read()
        match = re.search(r"Extrapolated:\s*(-?\d+\.\d+)", content)
        if match:
            total_energy = float(match.group(1))
            E_ads = total_energy - slab_energy - h2_gas_energy
            distances.append(distance)
            adsorption_energies.append(E_ads)
        else:
            print(f"Warning: No energy found in {file_name}.")

# Normalize to minimum
min_E = min(adsorption_energies)
normalized = [e - min_E for e in adsorption_energies]

# Plot
plt.figure(figsize=(8, 6))
plt.plot(distances, normalized, marker='o')
plt.xlabel("H–H Distance (Å)")
plt.ylabel("Relative Adsorption Energy (eV)")
plt.title("Corrected PES of H₂ on Ni(111)")
plt.grid(True)
plt.tight_layout()
plt.savefig("corrected_pes_plot.png")
plt.show()

