-- Select the band_name and calculate the lifespan of each band
SELECT 
    band_name, 
    -- If the band is still active (split is NULL), use 2022 as the end year
    -- Otherwise, use the year the band split
    CASE 
        WHEN split IS NULL THEN 2022 - formed 
        ELSE split - formed 
    END AS lifespan
FROM 
    bands -- This is the table containing the band data
-- Filter the bands to only include those with 'Glam rock' as their main style
WHERE 
    style = 'Glam rock'
-- Order the results by the lifespan column in descending order
-- This ranks the bands by their longevity
ORDER BY 
    lifespan DESC;