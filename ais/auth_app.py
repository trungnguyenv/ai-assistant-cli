import typer

from ais.api_key_providers import KeyRingProvider

app = typer.Typer(help="Manage OpenAI API Key")
key_provider = KeyRingProvider()


@app.command()
def set_key(api_key: str):
    """
    Set the OpenAI API key.
    """
    key_provider.set_api_key(api_key)
    typer.echo("API key saved successfully.")


@app.command()
def delete_key():
    """
    Delete the stored OpenAI API key.
    """
    key_provider.delete_api_key()
    typer.echo("API key deleted successfully.")
