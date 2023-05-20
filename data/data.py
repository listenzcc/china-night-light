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
import io
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

std = np.std(mat, axis=0)
mean = np.mean(mat, axis=0)

# %%


def imshow(arr, ax=None, title='title'):
    if ax is None:
        fig, ax = plt.subplots(1, 1)
    else:
        fig = None

    im = ax.imshow(arr)
    ax.set_title(title)
    ax.set_axis_off()
    plt.colorbar(im)

    return fig, im


fig, axes = plt.subplots(2, 1, figsize=(6, 8), dpi=120)

_, im = imshow(std, ax=axes[0], title='Std')
_, im = imshow(mean, ax=axes[1], title='Mean')

fig.tight_layout()
plt.show()
print(mat.shape, mean.shape, std.shape)

# %%


# %%

# %%
box = np.array(obj.tif_bBox)
print(box)
converted = box / 1000 * 0.0174532925199433
converted[:, 0] += 105
converted[:, 1] /= 2
print(converted)


# %% ---- 2023-05-19 ------------------------
# Pending

# %% ---- 2023-05-19 ------------------------
# Pending
# m = mat.ravel()
# m = m[m > 0]
# print(m.shape)
# plt.hist(m)

# # %%
# px.imshow(std).show()
# px.imshow(mean).show()

# %%
