# Exif-extractor

This is an package that is used to extract meta data and Exif information from images. This package is published in PyPI as named <a href="https://pypi.org/project/Exif-python/">Exif-extractor</a>.

# Installing

    pip install Exif-extractor

# Usage
`get_exif_for_file()` takes an image as argument and return meta information as dictionary\
`get_exif()` takes list of images as argument and return meta information as list

    >>> import Exif
    >>> imagename = "image.jpg"
    >>> Exif.get_exif_for_file(imagename)
    >>> Exif.get_exif(imagename)