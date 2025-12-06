from ase.io import read
from ase import Atoms
from ase.mep import NEB
from ase.optimize import BFGS
from gpaw import GPAW, PW
import os

# Başlangıç (moleküler H2 yukarıda) ve bitiş (dissosiyatif yapı) yapıları
initial = read('h2_2.5.traj')
final = read('dissociated_H2.traj')

# Ara yapılar (örneğin 3 tane ara yapı)
images = [initial]
for i in range(3):
    image = initial.copy()
    images.append(image)
images.append(final)

# NEB nesnesi oluştur
neb = NEB(images)

# Ara yapıları doğrusal şekilde interpolasyonla yerleştir
neb.interpolate()

# Her image için farklı bir GPAW hesaplayıcısı tanımla
for i, image in enumerate(images):
    image.calc = GPAW(mode=PW(300),
                      xc='PBE',
                      kpts=(1, 1, 1),
                      txt=f'neb_calc_{i}.txt')

# Optimizer ayarla
optimizer = BFGS(neb, trajectory='neb_path.traj', logfile='neb_opt.log')
optimizer.run(fmax=0.1)

