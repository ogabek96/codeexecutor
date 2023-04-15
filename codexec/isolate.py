import subprocess
import os
class Isolate:
    def __init__(self):
        self.box_id = self._pick_free_box()

    def init_box(self):
        process = subprocess.Popen(['isolate', '--init', '-b', str(self.box_id)],
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            raise Exception('Could not initialize a new isolate box: ' + stderr.decode('utf-8').strip())
        return stdout.decode('utf-8').strip()

    def cleanup(self):
        process = subprocess.Popen(['isolate', '--cleanup', '-b', str(self.box_id)],
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE)
        _, stderr = process.communicate()
        if stderr:
            raise Exception('Could not cleanup the isolate box: ' + stderr.decode("utf-8").strip())

    def run_command(self, commands, stdin_str = None):
        args = [
            '--run', 
            '--box-id', str(self.box_id),
             '-E','HOME=/tmp',
            '--time', '2',
            '-p60',
            # '--mem', '128000',
            # '--stack', '64000',
            '--env', 'PATH=/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:toolchain-dir-absolute-path',
            '--silent',
            '-d', '/etc:noexec',
            ] + commands
        process = subprocess.run(['isolate'] + args,
                            input=stdin_str,
                            text = True,
                            capture_output=True)
        return process.stdout, process.stderr

    def _pick_free_box(self):
        boxes = self._get_boxes()
        for i in range(1000):
            if str(i) not in boxes:
                return i
        raise Exception('All boxes are full')

    def _get_boxes(self):
        return set(os.listdir('/var/local/lib/isolate'))