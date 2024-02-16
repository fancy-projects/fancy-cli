"""
Folder Art with Neat Colors for You - FANCY
Use command 'fancy' in the terminal
"""

from pathlib import Path
from typer import Typer, Argument, Option
from fancy import api
from typing_extensions import Annotated
from rich import print

GREEN = "\e[32m"
CYAN = "\e[36m"
BOLD = "\e[1m"
END = "\e[0m"

app = Typer()

@app.command()
def fancy(
    icon: Annotated[Path, Argument(exists=True, help="Icon file path.")],
    folder: Annotated[Path, Option('--folder', '-f', exists=True, help="Folder path.")] = api.get_folder_icon(),
    output_path: Annotated[Path, Option('--output-path', '-o', help="Output icon file path.")] = 'icon.icns',
):
    api.overlay_icon(folder, icon, output_path)
    print(f"[bold red]Folder created![/bold red] It should be stored at [cyan]{output_path}[/cyan]")

if __name__ == "__main__":
    app()