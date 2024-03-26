"""
Folder Art with Neat Colors for You - FANCY
Use command 'fancy' in the terminal
"""

from pathlib import Path

from rich import print
from rich.panel import Panel

from typer import Typer, Argument, Option
from typing_extensions import Annotated

from fancy import api

app = Typer()

parameter_data = {
    'icon_path': Annotated[Path, Argument(help="Icon file path.", exists=True)],
    'output_path': Annotated[Path, Argument(help="Output icon file path.")],
    'output_path_option': Annotated[Path, Option('--output-path', '-o',
                                                 help="Output icon file path.")],

    'folder': Annotated[Path, Option('--folder', '-f', exists=True, help="Folder path.")],
    'icon_size_percent': Annotated[float, Option('--icon-size-percent', '-s',
                                                 help="Size of icon in proportion to folder.")],

    'folder_color': Annotated[str, Option('--folder-color', '-c',
                                          help='Color of folder. Can be '
                                               '"default", "windows", "red", '
                                               '"orange", "yellow", "green", '
                                               '"blue", "indigo", "violet", '
                                               'or "pink". "purple" is also '
                                               'allowed, but it is just an '
                                               'alias for "violet".')]
}


@app.command()
def fancy(
        icon_path: parameter_data['icon_path'],  # noqa: F821
        output_path: parameter_data['output_path'] = './icon.icns',  # noqa: F821
        output_path_option: parameter_data['output_path_option'] = './icon.icns',  # noqa: F821
        folder: parameter_data['folder'] = api.get_folder_icon(),  # noqa: F821
        icon_size_percent: parameter_data['icon_size_percent'] = 60,  # noqa: F821
        folder_color: parameter_data['folder_color'] = 'default',  # noqa: F821
):
    if output_path_option != Path('icon.icns'):
        output_path = output_path_option
    api.overlay_icon(folder, icon_path, output_path, folder_color, icon_size_percent)

    print(Panel(
        f"[bold red]Folder created![/bold red] It should be stored at [cyan]{output_path}[/cyan]",
        title_align='left',
        title='Success',
        border_style='green'
    )
    )


if __name__ == "__main__":
    app()
