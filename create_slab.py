from ase.build import fcc111
from ase.io import write

slab = fcc111('Ni', size=(3, 3, 3), vacuum=10.0)
write('ni111.traj', slab)


