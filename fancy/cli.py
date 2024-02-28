"""
Folder Art with Neat Colors for You - FANCY
Use command 'fancy' in the terminal
"""

from pathlib import Path

from rich import print  # noqa
from rich.panel import Panel  # noqa

from typer import Typer, Argument, Option
from typing_extensions import Annotated

from fancy import api

app = Typer()

parameter_data = {
    'icon': Annotated[Path, Argument(help="Icon file path.", exists=True)],
    'output_path': Annotated[Path, Argument(help="Output icon file path.")],
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
        icon: parameter_data['icon'],  # noqa
        output_path: parameter_data['output_path'] = './icon.icns',  # noqa
        folder: parameter_data['folder'] = api.get_folder_icon(),  # noqa
        icon_size_percent: parameter_data['icon_size_percent'] = 60,  # noqa
        folder_color: parameter_data['folder_color'] = 'default',  # noqa
):
    api.overlay_icon(folder, icon, output_path, folder_color, icon_size_percent)
    print(Panel(
        f"[bold red]Folder created![/bold red] It should be stored at [cyan]{output_path}[/cyan]",
        title_align='left',
        title='Success',
        border_style='green'
    )
    )


if __name__ == "__main__":
    app()
