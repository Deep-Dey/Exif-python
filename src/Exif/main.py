from PIL import Image
from PIL.ExifTags import TAGS
from typing import List, Dict


def get_exif_for_file(file_path: str) -> Dict:
    # read the image data using PIL and extract other basic metadata
    image: Image = Image.open(file_path)
    info_dict: Dict = {
        "FileName": image.filename,
        "ImageSize": image.size,
        "ImageHeight": image.height,
        "ImageWidth": image.width,
        "ImageFormat": image.format,
        "ImageMode": image.mode,
        "IsAnimated": getattr(image, "is_animated", False),
        "NoOfFrames": getattr(image, "n_frames", 1)
    }

    # extract EXIF data
    exifdata: List = image.getexif()
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes
        if isinstance(data, bytes):
            data = data.decode()

        info_dict[tag] = data
    return info_dict


def get_exif(file_name: str or List) -> Dict or List:
    '''
	put file_name as arugument and return the Exif data as dictionary 
	'''
    if file_name is None:
        raise ValueError('file_name cannot be None')
    elif file_name == [] or file_name == '':
        raise ValueError('file_name cannot be empty string or empty list')

    if type(file_name) == str:
        return get_exif_for_file(file_name)
    else:
        image_info: List = []
        for file in file_name:
            image_info.append(get_exif_for_file(file))
        return image_info
