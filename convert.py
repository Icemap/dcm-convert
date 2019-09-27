import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import os


def dcm_to_png(path, file_name, gray):
    image = sitk.ReadImage(path + os.sep + file_name)
    image_array = np.squeeze(sitk.GetArrayFromImage(image))
    if gray == "true":
        plt.imshow(image_array, "gray")
    else:
        plt.imshow(image_array)

    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

    save_path = path + os.sep + file_name.replace(".dcm", ".png")
    plt.savefig(save_path)
    return save_path
