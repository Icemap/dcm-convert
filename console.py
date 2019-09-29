import itk
import sys

if len(sys.argv) < 3:
    print('Usage: ' + sys.argv[0] + ' inputFile.dcm outputFile.png')
    sys.exit(1)

#
# Reads a 2D image in with signed short (16bits/pixel) pixel type
# and save it as unsigned char (8bits/pixel) pixel type
#
InputImageType = itk.Image.SS2
OutputImageType = itk.Image.UC2

reader = itk.ImageFileReader[InputImageType].New()
writer = itk.ImageFileWriter[OutputImageType].New()

filter = itk.RescaleIntensityImageFilter[InputImageType, OutputImageType].New()
filter.SetOutputMinimum(0)
filter.SetOutputMaximum(255)

filter.SetInput(reader.GetOutput())
writer.SetInput(filter.GetOutput())

reader.SetFileName(sys.argv[1])
writer.SetFileName(sys.argv[2])

writer.Update()
