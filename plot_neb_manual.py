import matplotlib.pyplot as plt

reaction_coords = list(range(9))
energies = [
    -177.501253,
    -178.826777,
    -178.916969,
    -178.994931,
    -179.492252,
    -179.559925,
    -179.620164,
    -179.621304,
    -179.618861
]

min_energy = min(energies)
relative_energies = [e - min_energy for e in energies]

plt.figure(figsize=(8, 6))
plt.plot(reaction_coords, relative_energies, marker='o')
plt.xlabel("Reaction Coordinate")
plt.ylabel("Relative Energy (eV)")
plt.title("NEB Energy Profile (Manual from log file)")
plt.grid(True)
plt.tight_layout()
plt.savefig("neb_manual_plot.png")

