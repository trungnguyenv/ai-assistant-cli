import platform
import os


def get_system_info():
    return f"""- architecture: {platform.architecture()[0]}
- operating_system: {platform.system()}
- os_version: {platform.version()}
- os_release: {platform.release()}
- shell: {os.getenv('SHELL')}
"""
