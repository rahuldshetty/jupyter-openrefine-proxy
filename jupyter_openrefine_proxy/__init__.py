import os
import subprocess
import getpass
import shutil


def get_executable(prog):
    # Find prog in known locations
    other_paths = [
        os.path.join('/usr/lib/openrefine', prog)
    ]
    if shutil.which(prog):
        return prog

    for op in other_paths:
        if os.path.exists(op):
            return op

    raise FileNotFoundError(f'Could not find {prog} in PATH')


def setup_openrefineserver():
    def _get_env(port):
        return dict(USER=getpass.getuser())

    def _get_cmd(port):
        return [
            get_executable('refine'),
            '-p', str(port),
            '-i', '0.0.0.0',
            '-d', '/home/jovyan/openrefine'
        ]

    return {
        'command': _get_cmd,
        'port': 3333,
        'environment': _get_env,
        'launcher_entry': {
            'title': 'OpenRefine'
        }
    }
