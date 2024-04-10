
import regionmask
# This function gets a netcdf file, a geopandas dataframe and the zonal variable(s)
# and returns a pandas dataframe of the zonal statistics over the polygons
# in the geopandas
# User must check the crs of the netcdf file and make sure to input it in the model
# if that is different from the default WGS84.

def mask_with_regionMask(the_xrDataset, the_map, id_column, the_crs="EPSG:4326", 
                         longitude_name='lon', latitude_name= 'lat'):
    # Change the map crs to the Xarray crs
    the_map = the_map.to_crs(crs=the_crs)
    # Create mask of multiple regions from shapefile
    the_mask = regionmask.mask_3D_geopandas(
        the_map,
        the_xrDataset[longitude_name], # Later will make it general
        the_xrDataset[latitude_name], 
        drop=True,
        numbers= id_column
    )
    the_xrDataset = the_xrDataset.where(the_mask)
    return(the_xrDataset)


def zonal_stat(the_xrDataset, the_map, id_column, the_crs="EPSG:4326", 
               longitude_name='lon', latitude_name='lat', func='mean'):
    xr_masked = mask_with_regionMask(the_xrDataset, the_map, id_column, the_crs, 
                                     longitude_name=longitude_name, latitude_name=latitude_name)
    
    # Use getattr to dynamically call the aggregation function based on the func argument
    xr_agg = xr_masked.groupby('time').apply(lambda x: getattr(x, func)(dim=['lat', 'lon']))
    
    xr_df = xr_agg.to_dataframe().reset_index()

    return xr_df


