from PIL import Image
from platform import system, release
from pathlib import Path

file_path = str(Path(__file__).parent.resolve())


def get_folder_icon():
    if system() == "Darwin":
        folder_icon = f"{file_path}/folders/macos.icns"
    else:
        if release() == '11':
            folder_icon = f"{file_path}/folders/win11.icns"
        else:
            folder_icon = f"{file_path}/folders/win10.icns"
    return folder_icon


def change_hue_by(hue_change: float, image: Image.Image):
    image = image.convert('HSV')

    h, s, v = image.getchannel('h')

    # Increase Hue
    h = h.point(lambda hue: hue + hue_change)

    return Image.merge("HSV", (h, s, v))


def color_str_to_hue():
    pass


def overlay_icon(folder, icon, output_path, folder_color=None):
    if folder == f"{file_path}/folders/win10.icns":
        center = (200, 256)
    else:
        center = (256, 300)

    folder_img = Image.open(folder).resize((1024, 1024))
    icon_img = Image.open(icon).resize((512, 512))

    folder_img.paste(icon_img, center, mask=icon_img)
    folder_img.save(output_path)
