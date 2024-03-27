from PIL import Image
from pathlib import Path
from platform import system, release
from re import search

file_path = Path(__file__).parent.resolve()


def get_folder_icon() -> Path:
    if system() == "Darwin":
        folder_icon = f"{file_path}/assets/folders/macos.icns"
    else:
        if release() == '11':
            folder_icon = f"{file_path}/assets/folders/win11.icns"
        else:
            folder_icon = f"{file_path}/assets/folders/win10.icns"
    return Path(folder_icon).resolve()


def prepare_images(folder_path, icon, folder_hue, size_percent):
    folder_hue = color_str_to_hue(folder_hue)

    folder_img = Image.open(folder_path)
    alpha = folder_img.getchannel("A")

    h, s, v = folder_img.resize((1024, 1024)).convert('HSV').split()
    h = Image.eval(h, lambda pixel_hue: (pixel_hue + folder_hue) % 360)
    folder_img = Image.merge("HSV", (h, s, v))

    icon_dim = int(1024 * (size_percent / 100))
    icon_img = Image.open(icon).resize((icon_dim, icon_dim))

    folder_img = folder_img.convert('RGBA')
    folder_img.putalpha(alpha)

    return folder_img, icon_img


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


def overlay_icon(folder_path: Path, icon_path: Path, output_path: Path,
                 folder_color: str = None, size_percent: float = 65,
                 config_file: Path = None):
    folder_img, icon_img = prepare_images(folder_path, icon_path, folder_color, size_percent)

    if folder_path == Path(f"{file_path}/assets/folders/win10.icns"):
        center = ((folder_img.width - icon_img.width) // 2 - 50,
                  (folder_img.height - icon_img.height) // 2)
    else:
        center = ((folder_img.width - icon_img.width) // 2,
                  (folder_img.height - icon_img.height) // 2 + 50)

    folder_img.paste(icon_img, center, mask=icon_img)

    try:
        folder_img.save(output_path)
    except OSError as error:
        if search("cannot write mode RGBA as .*", str(error)):
            folder_img.convert('RGB').save(output_path)
        else:
            raise error

    if config_file is not None:
        config_data = {
            "config_file": config_file,

            "icon_path": icon_path,
            "output_path": output_path,

            "folder_path": folder_path,
            "folder_color": folder_color,
            "size_percent": size_percent,
        }
        config_file.write_text(config_data, encoding="utf-8")


# overlay_icon(Path('./folders/macos.icns'),
#                   Path('/Users/Zhisen/Pictures/Downloaded Pictures/Icons/html.icns'),
# Path('./example.icns'), 'red', 70)
