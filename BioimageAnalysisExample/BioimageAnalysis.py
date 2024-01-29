import skimage.measure
from skimage import io, filters 
import pandas as pd
url = 'https://github.com/sugan89/Introduction_To_Docker/blob/main/RPE.tif?raw=true'
image = io.imread(url)
thresholded_image = skimage.filters.threshold_otsu(image)
binary = image > thresholded_image
perimeter = skimage.measure.perimeter(binary, neighbourhood=4)
print(f'The perimeter of the binary object is {perimeter}')