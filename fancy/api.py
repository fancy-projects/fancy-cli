from PIL import Image
from platform import system, release
from pathlib import Path
import numpy as np

file_path = Path(__file__).parent.resolve()


def get_folder_icon() -> str:
    if system() == "Darwin":
        folder_icon = f"{file_path}/folders/macos.icns"
    else:
        if release() == '11':
            folder_icon = f"{file_path}/folders/win11.icns"
        else:
            folder_icon = f"{file_path}/folders/win10.icns"
    return folder_icon


def change_hue_to(folder_hue: float | str, folder_image: Image.Image) -> Image.Image:
    if isinstance(folder_hue, str):
        folder_hue = color_str_to_hue(folder_hue)

    folder_image_alpha = folder_image.getchannel('A')
    folder_image = folder_image.convert('HSV')

    image_array = np.array(folder_image)

    # [..., 0] means first item (0) of last dimension (...)
    hue_channel = image_array[..., 0]
    hue_channel = hue_channel + folder_hue
    image_array[..., 0] = hue_channel

    folder_image = Image.fromarray(image_array, 'HSV').convert('RGBA')
    folder_image.putalpha(folder_image_alpha)

    return folder_image


def color_str_to_hue(color_str: str) -> int:
    color_dict = {
        'default': 0,
        'windows': -110,
        'red': -140,
        'orange': -120,
        'yellow': -100,
        'green': -30,
        'blue': 15,
        'indigo': 30,
        'violet': 60,
        'purple': 60,
        'pink': 90,
    }

    return color_dict[color_str]


def overlay_icon(folder_path: Path, icon: Path, output_path: Path, folder_color: str = None, size_percent: float = 50):
    folder_img = Image.open(folder_path).resize((1024, 1024))

    icon_px = int(1024 * (size_percent / 100))
    icon_img = Image.open(icon).resize((icon_px, icon_px))

    if folder_color is not None:
        folder_img = change_hue_to(folder_color, folder_img)

    if folder_path == Path(f"{file_path}/folders/win10.icns"):
        center = ((folder_img.width - icon_img.width) // 2 - 50, (folder_img.height - icon_img.height) // 2)
    else:
        center = ((folder_img.width - icon_img.width) // 2, (folder_img.height - icon_img.height) // 2 + 50)

    folder_img.paste(icon_img, center, mask=icon_img)
    folder_img.save(output_path)