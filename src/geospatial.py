# A personal library for different geospatial needs I might have

# Returns the descriptive statistics (mean, median, min, max, percentiles)
# The input (flattened_variable) must a flattened variable from an xarray
def describe_flattened_xarray(flattened_variable):
    description = np.nanmin(flattened_variable), np.nanmax(flattened_variable), \
                  np.nanmean(flattened_variable), np.nanmedian(flattened_variable), \
                  np.nanstd(flattened_variable), \
                  np.nanpercentile(flattened_variable, 5), \
                  np.nanpercentile(flattened_variable, 25), \
                  np.nanpercentile(flattened_variable, 50), \
                  np.nanpercentile(flattened_variable, 75), \
                  np.nanpercentile(flattened_variable, 95)
    
    # Round the descriptive statistics to three decimal places
    rounded_description = tuple(round(value, 3) for value in description)
    
    # Print the rounded result
    print("Minimum:", rounded_description[0])
    print("Maximum:", rounded_description[1])
    print("Mean:", rounded_description[2])
    print("Median:", rounded_description[3])
    print("Standard Deviation:", rounded_description[4])
    print("5th Percentile:", rounded_description[5])
    print("25th Percentile:", rounded_description[6])
    print("50th Percentile (Median):", rounded_description[7])
    print("75th Percentile:", rounded_description[8])
    print("95th Percentile:", rounded_description[9])