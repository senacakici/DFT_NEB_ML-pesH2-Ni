from ase.io import read
from gpaw import GPAW, PW
import numpy as np

heights = [9.0, 11.0, 13.0, 15.0, 17.0, 19.0]


energies = []

for h in heights:
    fname = f'h2_{h:.1f}.traj'
    atoms = read(fname)
    
    calc = GPAW(mode=PW(400),  # dalga seti
                xc='PBE',       # fonksiyonel
                kpts=(2, 2, 1), # k-uzayı örneklemesi
                txt=f'calc_{h:.1f}.txt')  # çıktı dosyası

    atoms.set_calculator(calc)
    energy = atoms.get_potential_energy()
    
    energies.append((h, energy))
    print(f"{fname}: {energy:.6f} eV")

# Verileri dosyaya yaz
with open("pes_data.csv", "w") as f:
    f.write("height,energy\n")
    for h, e in energies:
        f.write(f"{h},{e}\n")

