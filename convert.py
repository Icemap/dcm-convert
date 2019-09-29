import itk
import os


def dcm_to_png(path, file_name):
    input_image_type = itk.Image.SS2
    output_image_type = itk.Image.UC2

    reader = itk.ImageFileReader[input_image_type].New()
    writer = itk.ImageFileWriter[output_image_type].New()

    img_filter = itk.RescaleIntensityImageFilter[input_image_type, output_image_type].New()
    img_filter.SetOutputMinimum(0)
    img_filter.SetOutputMaximum(255)

    img_filter.SetInput(reader.GetOutput())
    writer.SetInput(img_filter.GetOutput())

    save_path = path + os.sep + file_name.replace(".dcm", ".png").replace(".DCM", ".png")
    reader.SetFileName(path + os.sep + file_name)
    writer.SetFileName(save_path)

    writer.Update()
    return save_path

