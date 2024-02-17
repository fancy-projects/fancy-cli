from pathlib import Path

from rich import print
from rich.panel import Panel

from typer import Typer, Argument, Option
from typing_extensions import Annotated

from fancy import api

app = Typer()


@app.command()
def fancy(
        icon: Annotated[Path, Argument(exists=True, help="Icon file path.")],
        folder: Annotated[Path, Option('--folder', '-f', exists=True, help="Folder path.")] = api.get_folder_icon(),
        output_path: Annotated[Path, Option('--output-path', '-o', help="Output icon file path.")] = 'icon.icns',
):
    api.overlay_icon(folder, icon, output_path)

    print(Panel(
        f"[bold red]Folder created![/bold red] It should be stored at [cyan]{output_path}[/cyan]",
        title_align='left',
        title='Success',
        border_style='green'
    )
    )
