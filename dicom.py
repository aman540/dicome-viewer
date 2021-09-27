import pydicom as dicom
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
from pydicom.pixel_data_handlers.util import apply_color_lut


from pydicom import dcmread
from pydicom.data import get_testdata_file




data_set=dicom.read_file("D://My Django projects//dicome viewer//MRBRAIN.DCM")

pat_name = data_set.PatientName
display_name = pat_name.family_name + ", " + pat_name.given_name
print(data_set.pixel_array)
print(data_set.Rows)
print(data_set.Columns)
print(data_set.PatientPosition)
print(data_set)

print(f"Patient's Name...: {display_name}")
print(f"Patient ID.......: {data_set.PatientID}")
print(f"Modality.........: {data_set.Modality}")
print(f"Study Date.......: {data_set.StudyDate}")
print(f"Image size.......: {data_set.Rows} x {data_set.Columns}")
print(f"Pixel Spacing....: {data_set.PixelSpacing}")

arr = data_set.pixel_array

# use .get() if not sure the item exists, and want a default value if missing
print(f"Slice location...: {data_set.get('SliceLocation', '(missing)')}")

plt.imshow(data_set.pixel_array,plt.cm.gray)
plt.show()




