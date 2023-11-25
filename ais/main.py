import subprocess

import typer
from openai import OpenAI
from rich.prompt import Prompt

import ais.auth_app
from ais.api_key_providers import KeyRingProvider
from ais.utils import get_system_info

app = typer.Typer()
app.add_typer(ais.auth_app.app)
key_provider = KeyRingProvider()


@app.command()
def cmd(prompt: str):
    messages = [
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
    ]

    response = get_ai_completion(messages)

    command = response.choices[0].message.content
    typer.echo(f"The suggested command is: {typer.style(command, fg=typer.colors.GREEN)}")

    prompt_execute = typer.style("E", fg=typer.colors.GREEN, bold=True) + "xecute"
    prompt_adjust = typer.style("A", fg=typer.colors.YELLOW, bold=True) + "djust"
    prompt_cancel = typer.style("C", fg=typer.colors.RED, bold=True) + "ancel"

    choice = Prompt.ask(f"Choose action to perform ({prompt_execute}/{prompt_adjust}/{prompt_cancel})",
                        choices=["E", "A", "C"], default="C")

    while choice == "A":
        if choice == "A":
            adjustment = Prompt.ask("What to adjust?")
            messages.append(response.choices[0].message)
            messages.append({
                "role": "user",
                "content": adjustment
            })
            response = get_ai_completion(messages)

            command = response.choices[0].message.content
            typer.echo(f"The suggested command is: {typer.style(command, fg=typer.colors.GREEN)}")

            choice = Prompt.ask(f"Choose action to perform ({prompt_execute}/{prompt_adjust}/{prompt_cancel})",
                                choices=["E", "A", "C"], default="C")

    if choice == "E":
        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       text=True)
            output, error = process.communicate()

            if process.returncode != 0:
                typer.echo(f"Error: {error}", err=True)
            else:
                typer.echo(output)

        except subprocess.SubprocessError as e:
            typer.echo(f"An error occurred: {e}", err=True)


def get_ai_completion(messages):
    client = OpenAI(api_key=key_provider.get_api_key())

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response


if __name__ == "__main__":
    app()
