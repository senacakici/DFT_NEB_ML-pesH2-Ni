from ase.io import read, write
from gpaw import GPAW

images = read('neb_path.traj@0:')

# GPAW'dan enerji hesaplayıcıyı her imaja set et
for atoms in images:
    calc = GPAW(txt=None)  # Sadece cache'i okur
    atoms.calc = calc
    atoms.get_potential_energy()

# Enerji bilgili yeni traj dosyası yaz
write('neb_path_with_energy.traj', images)

