import os
import mimetypes
import arrow


ADDITIONAL_FILE_TYPES = {".md": "text/markdown"}


def datetimeformat(date_str):
    dt = arrow.get(date_str)
    return dt.humanize()


def file_type(key):
    file_info = os.path.splitext(key)
    file_extension = file_info[1]
    try:
        return mimetypes.types_map[file_extension]
    except KeyError:
        filetype = "Unknown"
        if file_info[0].startswith(".") and file_extension == "":
            filetype = "text"

        if file_extension in ADDITIONAL_FILE_TYPES.keys():
            filetype = ADDITIONAL_FILE_TYPES[file_extension]

        return filetype
