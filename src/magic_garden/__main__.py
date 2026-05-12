"""Command-line interface."""

import typer


app: typer.Typer = typer.Typer()


@app.command(name="magic-garden")
def main() -> None:
    """Magic Garden."""


if __name__ == "__main__":
    app()  # pragma: no cover
