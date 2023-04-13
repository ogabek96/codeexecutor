import subprocess

# import os

# runArgs = [
#       'exec',
#       '-i',
#       '68787464aac4',
#       'isolate', '--run',
#       '--silent',
#       '--box-id', '0',
#       '--meta', '/var/local/lib/isolate/0/box/mount/meta.txt',
#       '--stdin', os.path.join(this.internalFolderPath, 'stdin.txt'),
#       '--stdout', os.path.join(this.internalFolderPath, 'stdout.txt'),
#       '--stderr', os.path.join(this.internalFolderPath, 'stderr.txt'),
#       '--time', '2',
#        '--mem', '1280000',
#        '--stack', '64000',
#       '-p60',
#       '-E', 'HOME=/tmp',
#       '--env', 'PATH=/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:toolchain-dir-absolute-path',
#       '-d', '/etc:noexec',
#       '--chdir', this.internalFolderPath,
#       # run command
#     ];
def exec_command(command, args):
    process = subprocess.Popen(['python', 'echo.py'],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        raise Exception(stderr)
    return stdout