import exifread


def get_exif(fn):
    tags = exifread.process_file(open(fn, 'rb'))
    return tags
