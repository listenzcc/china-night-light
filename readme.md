# 中国灯光数据

---
- [中国灯光数据](#中国灯光数据)
	- [数据来源](#数据来源)


## 数据来源

数据来自 An improved time-series DMSP-OLS-like data (1992-2022) in China by integrating DMSP-OLS and SNPP-VIIRS。其源信息为下表，这些信息用于将数据中的像素转换为其经纬度坐标

```python
# Read raw projection
from osgeo import gdal
ds = gdal.Open(path.as_posix())
ds.GetProjection()
```

```tsx
// Raw projection
PROJCS["WGS_1984_Albers",

	GEOGCS["WGS 84",
		DATUM["WGS_1984", SPHEROID["WGS 84",6378137,298.257223563, AUTHORITY["EPSG","7030"]], AUTHORITY["EPSG","6326"]],
		PRIMEM["Greenwich",0],
		UNIT["degree",0.0174532925199433, AUTHORITY["EPSG","9122"]],
		AUTHORITY["EPSG","4326"]
	],

	PROJECTION["Albers_Conic_Equal_Area"],

	PARAMETER["latitude_of_center",0],
	PARAMETER["longitude_of_center",105],
	PARAMETER["standard_parallel_1",25],
	PARAMETER["standard_parallel_2",47],
	PARAMETER["false_easting",0],
	PARAMETER["false_northing",0],

	UNIT["metre",1,AUTHORITY["EPSG","9001"]],

	AXIS["Easting",EAST],
	AXIS["Northing",NORTH]
]

// Info of WGS 84
// url: https://epsg.io/4326
GEOGCS["WGS 84",
    DATUM["WGS_1984",
        SPHEROID["WGS 84",6378137,298.257223563,
            AUTHORITY["EPSG","7030"]],
        AUTHORITY["EPSG","6326"]],
    PRIMEM["Greenwich",0,
        AUTHORITY["EPSG","8901"]],
    UNIT["degree",0.0174532925199433,
        AUTHORITY["EPSG","9122"]],
    AUTHORITY["EPSG","4326"]]
```

![Untitled](%E4%B8%AD%E5%9B%BD%E7%81%AF%E5%85%89%E6%95%B0%E6%8D%AE%2082686ac6a5804642ad278fab2414265a/Untitled.png)

[An improved time-series DMSP-OLS-like data (1992-2022) in China by integrating DMSP-OLS and SNPP-VIIRS](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GIYGJU)

[WGS 84 - WGS84 - World Geodetic System 1984, used in GPS  - EPSG:4326](https://epsg.io/4326)