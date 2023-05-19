"""
File: data.py
Author: Chuncheng Zhang
Date: 2023-05-19
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Read data form the 'dataverse_files' directory,
    the data is downloaded from the url: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GIYGJU

Functions:
    1. Pending
    2. Pending
    3. Pending
    4. Pending
    5. Pending
"""


# %% ---- 2023-05-19 ------------------------
# Pending
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

from tqdm.auto import tqdm
from pathlib import Path
from geotiff import GeoTiff


# %% ---- 2023-05-19 ------------------------
# Pending
folder = Path(__file__).parent.joinpath('dataverse_files')


def _year(path):
    return int(path.name.split('.tif')[0][-4:])


found = [e for e in folder.iterdir() if 'DMSP-like' in e.name]

files = dict()
for path in found:
    files[_year(path)] = path

files


# %% ---- 2023-05-19 ------------------------
# Pending
lst = []
for key in tqdm(files, 'Read tif files'):
    obj = GeoTiff(files[key], crs_code=4326)
    try:
        arr = np.array(obj.read())
    except:
        print(f'Failed to read {key}')
        continue
    lst.append(arr)

mat = np.array(lst)
mat.shape

# %%


def imshow(arr, ax=None, show_flag=True):

    if ax is None:
        fig, ax = plt.subplots(1, 1)

    im = ax.imshow(arr)
    plt.colorbar(im)

    fig.tight_layout()

    if show_flag:
        plt.show()


std = np.std(mat, axis=0)
mean = np.mean(mat, axis=0)

imshow(std)
imshow(mean)


# %%
box = np.array(obj.tif_bBox)
print(box)
converted = box / 1000 * 0.0174532925199433
converted[:, 0] += 105
converted[:, 1] /= 2
converted


# %% ---- 2023-05-19 ------------------------
# Pending

# %% ---- 2023-05-19 ------------------------
# Pending
m = mat.ravel()
m = m[m > 0]
print(m.shape)
plt.hist(m)

# %%
px.imshow(std).show()
px.imshow(mean).show()

# %%
