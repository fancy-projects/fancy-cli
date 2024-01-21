"""
Folder Art with Neat Colors for You - FANCY
Use command 'fancy' in the terminal
"""
from platform import system, release
import click
from PIL import Image

FILE_PATH = __file__.removesuffix("/__init__.py").removesuffix("\__init__.py")

if system() == "Darwin":
    folder_icon = f"{FILE_PATH}/folders/macos.icns"
else:
    if release() == '11':
        folder_icon = f"{FILE_PATH}/folders/win11.icns"
    else:
        folder_icon = f"{FILE_PATH}/folders/win10.icns"


def change_hue_by(hue_change, image):
    image = image.convert('HSV')

    h, s, v = image.getchannel('h')

    # Increase Hue
    h = h.point(lambda hue: hue + hue_change)

    return Image.merge("HSV", (h, s, v))


@click.group()
def cli():
    pass


@cli.command()
@click.option('--folder', '-f', default=folder_icon, type=click.Path(exists=True), help='Folder path.')
@click.option('--output-path', '-o', default='icon', type=str, help=("File path of "
                                                                     "output icon file including name of "
                                                                     "file. Do not include file extension."))
@click.argument('icon', type=click.Path(exists=True))
def fancy(folder, icon, output_path):
    if folder == f"{FILE_PATH}/folders/win10.icns":
        center = (200, 256)
    else:
        center = (256, 300)

    folder = folder.replace("\\", "/")
    icon = icon.replace("\\", "/")

    folder = Image.open(folder).resize((1024, 1024))
    icon = Image.open(icon).resize((512, 512))

    folder.paste(icon, center, mask=icon)
    folder.save(f'{output_path}.icns')