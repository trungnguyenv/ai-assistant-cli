from typing import Optional

import typer
from rich.prompt import Prompt

from ais.api_key_providers import KeyRingProvider

app = typer.Typer(help="Manage OpenAI API Key")
key_provider = KeyRingProvider()


@app.command()
def set_key(api_key: Optional[str] = typer.Option(None, envvar="OPENAI_API_KEY")):
    """
    Set the OpenAI API key.
    """
    if not api_key:
        api_key = Prompt.ask("Please enter your OpenAI API Key", password=True)
    if not api_key:
        typer.echo("API key could not be found", err=True)
        raise typer.Exit(1)

    key_provider.set_api_key(api_key)
    typer.echo("API key saved successfully.")


@app.command()
def delete_key():
    """
    Delete the stored OpenAI API key.
    """
    key_provider.delete_api_key()
    typer.echo("API key deleted successfully.")
