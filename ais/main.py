import json
import subprocess

import typer
from openai import OpenAI

from ais.api_key_providers import KeyRingProvider
from ais.utils import get_system_info
import ais.auth_app

app = typer.Typer()
app.add_typer(ais.auth_app.app)
key_provider = KeyRingProvider()


@app.command()
def cmd(prompt: str):
    client = OpenAI(api_key=key_provider.get_api_key())

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"""You are AI Command Line Assistant, your task is to help to turn user input into a 
valid command line for execution Make sure the command use the correct syntax of the provided system 
info
Only output the command, do not explain
The command must be oneliner

System Info: 
{get_system_info()}`
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    command = response.choices[0].message.content
    typer.echo(f"The suggested command is: {typer.style(command, fg=typer.colors.GREEN)}")
    if typer.confirm("Do you want to execute it?"):
        typer.echo(subprocess.check_output(command, shell=True, text=True))


if __name__ == "__main__":
    app()
