import xarray as xr
import fsspec 
import s3fs
client_kwargs={'region_name':'us-east-1'}
config_kwargs = {'max_pool_connections': 30}

fs = s3fs.S3FileSystem(client_kwargs=client_kwargs, 
                       config_kwargs=config_kwargs, 
                       anon=True)  # public read

fs.ls('noaa-gfs-bdp-pds/gfs.20201027/00/')

fs.download('noaa-gfs-bdp-pds/gfs.20201027/00/gfs.t00z.pgrb2full.0p50.f027','gfs.t00z.pgrb2full.0p50.f027.grib2')

ds = xr.open_dataset('gfs.t00z.pgrb2full.0p50.f027.grib2', engine='cfgrib')
ds