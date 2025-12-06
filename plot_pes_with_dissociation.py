import os
import re
import matplotlib.pyplot as plt

# Referans enerjileri
with open("slab_energy.txt") as f:
    E_slab = float(f.read().strip())

with open("h2_gas_energy.txt") as f:
    E_h2 = float(f.read().strip())

# Moleküler adsorpsiyon dosyaları (sadece sayı içerenler)
files = []
for f in os.listdir():
    if f.startswith("calc_") and f.endswith(".txt"):
        try:
            float(f.replace("calc_", "").replace(".txt", ""))
            files.append(f)
        except ValueError:
            continue

files.sort(key=lambda x: float(x.replace("calc_", "").replace(".txt", "")))

distances = []
ads_energies = []

for file in files:
    z = float(file.replace("calc_", "").replace(".txt", ""))
    with open(file) as f:
        content = f.read()
        match = re.search(r"Extrapolated:\s*(-?\d+\.\d+)", content)
        if match:
            E_total = float(match.group(1))
            E_ads = E_total - E_slab - E_h2
            distances.append(z)
            ads_energies.append(E_ads)

# Normalize
min_E = min(ads_energies)
ads_energies = [e - min_E for e in ads_energies]

# Dissociative noktayı al
with open("dissociated_energy.txt") as f:
    E_diss = float(f.read().strip())
E_diss_ads = E_diss - E_slab - E_h2
E_diss_ads_norm = E_diss_ads - min_E

# Plot
plt.figure(figsize=(8,6))
plt.plot(distances, ads_energies, marker='o', label="Molecular Adsorption")
plt.axhline(E_diss_ads_norm, color='r', linestyle='--', label="Dissociative Adsorption")
plt.xlabel("H–H Distance (Å)")
plt.ylabel("Relative Adsorption Energy (eV)")
plt.title("PES with Molecular and Dissociative Adsorption")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("pes_with_dissociation.png")
plt.show()

