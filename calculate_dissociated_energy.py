from ase.io import read
from gpaw import GPAW, PW

# Yapıyı oku
atoms = read('dissociated_H2.traj')

# GPAW hesaplayıcısı tanımla
calc = GPAW(mode=PW(400), xc='PBE', kpts=(2, 2, 1), txt='calc_dissociated.txt')
atoms.calc = calc

# Enerjiyi hesapla
energy = atoms.get_potential_energy()
print(f'Dissociated H2 energy: {energy:.6f} eV')

