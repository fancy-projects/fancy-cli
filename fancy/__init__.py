"""
Folder Art with Neat Colors for You - FANCY
Use command 'fancy' in the terminal
"""
print('eee')
import click
import api

OS_FOLDER_ICON = api.get_folder_icon()


GREEN = "\e[32m"
CYAN = "\e[36m"

BOLD = "\e[1m"
END = "\e[0m"

@click.group()
def cli():
    pass


@cli.command()
@click.option('--folder', '-f', default=OS_FOLDER_ICON, type=click.Path(exists=True), help='Folder path.')
@click.option('--output-path', '-o', default='icon', type=str, help=("File path of "
                                                                     "output icon file including name of "
                                                                     "file."))
@click.option('--folder-color', '-c', type=str, help=("Color of folder. 'red', 'orange'"))
@click.argument('icon', type=click.Path(exists=True))
def fancy(folder, icon, output_path):
    api.overlay_icon(folder, icon, output_path)
    click.echo(f"{BOLD}Folder created!{END} {CYAN}It should be stored at {output_path}{END}")  # noqa
