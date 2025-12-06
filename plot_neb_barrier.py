from ase.io import read
from ase.mep import NEBTools
import matplotlib.pyplot as plt
import numpy as np

# NEB sonucu traj dosyasını oku
images = read('neb_path.traj@0:')

# NEBTools'u kullanarak analiz et
nebtools = NEBTools(images)

# Enerjileri ve reaksiyon koordinatlarını al
rc, energies = nebtools.get_barrier()

# Enerjileri minimuma göre hizala
energies -= min(energies)

# Grafik çiz
plt.figure(figsize=(8, 5))
plt.plot(rc, energies, marker='o', linestyle='-', color='red')
plt.xlabel('Reaction Coordinate (Å)')
plt.ylabel('Relative Energy (eV)')
plt.title('NEB Reaction Path for H₂ Dissociation on Ni(111)')
plt.grid(True)
plt.tight_layout()
plt.savefig("neb_barrier_plot.png")
plt.show()

