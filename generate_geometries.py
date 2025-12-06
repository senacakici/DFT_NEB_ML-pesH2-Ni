from ase.io import read, write
from ase import Atoms
import numpy as np
import os

# Ni slab dosyasını okuyoruz
slab = read('ni111.traj')

# H2 molekülü: 0.74 Å bağ uzunluğu (yaklaşık)
h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])

# Yüzeyin tam ortasına yerleştirmek için slab merkezini bul
x_center = slab.get_cell()[0, 0] / 2
y_center = slab.get_cell()[1, 1] / 2

# Eklemek istediğin yeni uzaklıklar:
heights = [9.0, 11.0, 13.0, 15.0, 17.0, 19.0]


for h in heights:
    fname = f'h2_{h:.1f}.traj'
    
    # Eğer dosya zaten varsa, atla
    if os.path.exists(fname):
        print(f'{fname} zaten var, atlanıyor.')
        continue

    # H2 molekülünü slab üstüne yerleştir
    h2_translated = h2.copy()
    h2_translated.translate([x_center, y_center, slab.get_positions()[:,2].max() + h])
    system = slab + h2_translated
    
    # Yeni dosyayı kaydet
    write(fname, system)
    print(f'Yazıldı: {fname}')

