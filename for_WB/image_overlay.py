import os
from PIL import Image


def get_list_from_str(string: str, delim):
    split_str = string.split(delim)

    for word in split_str:
        word.strip()

    return split_str


def infographic_overlay(mockup_path, infographic_path):
    if not infographic_path or not mockup_path:
        return ""

    if not (os.path.isfile(mockup_path) and os.path.isabs(mockup_path)):
        print(f"No such file or it's not abs path: {mockup_path}")
        return ""

    if not (os.path.isfile(infographic_path) and os.path.isabs(infographic_path)):
        print(f"No such file or it's not abs path: {infographic_path}")
        return ""

    tmp_file_name = os.path.splitext(os.path.basename(mockup_path))[0] + "_tmp.png"
    tmp_file_path = os.path.join(os.path.dirname(infographic_path), tmp_file_name)

    if os.path.isfile(tmp_file_path):
        print(f"Removing tmp file {tmp_file_path} before begin")
        os.remove(tmp_file_path)

    with Image.open(mockup_path) as mockup, Image.open(infographic_path) as infographic:

        info_resized = infographic.resize(mockup.size)

        mockup.paste(info_resized, (0, 0), info_resized)

        mockup.save(tmp_file_path)

    return tmp_file_path



if __name__ == "__main__":
    pass

path_mocku = 'D:\python/for_WB\img'
mocku = sorted(os.listdir(path_mocku))
path_infograph = "D:\python/for_WB\line/black"
infograph = sorted(os.listdir(path_infograph))

for i in infograph:
    for k in mocku:
        moc = f'D:\\python\\for_WB\\img\\{k}'
        infogr = f'D:\\python\\for_WB\\line\\black\\{i}'
        infographic_overlay(moc, infogr)


print(mocku)
print(infograph)
#infographic_overlay(mocku, infograph)

