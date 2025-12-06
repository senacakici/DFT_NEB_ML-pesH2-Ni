from ase.io import read, write
from ase import Atoms

# Slab'ı oku
slab = read('ni111.traj')

# Yüzey merkezi
x_center = slab.get_cell()[0, 0] / 2
y_center = slab.get_cell()[1, 1] / 2
z_top = slab.get_positions()[:,2].max()

# Ayrışmış iki H atomu (örneğin 1 Å aralıkla)
h1 = Atoms('H', positions=[[x_center - 0.5, y_center, z_top + 1.0]])
h2 = Atoms('H', positions=[[x_center + 0.5, y_center, z_top + 1.0]])

# Sistemi birleştir
system = slab + h1 + h2

# Kaydet
write('dissociated_H2.traj', system)
print("Dissociative geometri dosyası oluşturuldu: dissociated_H2.traj")

