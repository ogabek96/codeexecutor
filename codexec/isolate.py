import os
import subprocess
import threading

class Isolate:
    def __init__(self):
        self.box_id = None
        self.lock = threading.RLock()

    # creates a new empty isolated box
    def init_box(self):
        with self.lock:
            while True:
                self.box_id = self._pick_free_box()
                cmd = ['isolate', '--init', '-b', str(self.box_id)]
                stdout, stderr = self._run_command(cmd)
                if not stderr:
                    return stdout.strip()

    # cleans up the box isolate created
    def cleanup(self):
        with self.lock:
            cmd = ['isolate', '--cleanup', '-b', str(self.box_id)]
            _, stderr = self._run_command(cmd)
            if stderr:
                raise Exception('Could not cleanup the isolate box: ' + stderr.strip())

    # runs the code in isolated environment
    def run_command(self, commands, stdin_str=None):
        with self.lock:
            args = [
                '--run', 
                '--box-id', str(self.box_id),
                '-E', 'HOME=/tmp',
                '--time', '2',
                '-p', '60',
                # '--mem', '128000',
                # '--stack', '64000',
                '--env', 'PATH=/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:toolchain-dir-absolute-path',
                '--silent',
                '-d', '/etc:noexec',
            ] + commands
            cmd = ['isolate'] + args
            stdout, stderr = self._run_command(cmd, stdin_str=stdin_str)
            return stdout.strip(), stderr.strip()

    # picks up the free box
    def _pick_free_box(self, max_id=999):
        boxes = self._get_boxes()
        for i in range(max_id):
            if str(i) not in boxes:
                print('box id:' + str(i))
                return i
        raise Exception('All boxes are full')

    # gets all created boxes
    def _get_boxes(self):
        return set(os.listdir('/var/local/lib/isolate'))

    # runs a command and returns its stdout and stderr
    def _run_command(self, cmd, stdin_str=None):
        process = subprocess.run(cmd,
                                input=stdin_str,
                                text=True,
                                capture_output=True)
        return process.stdout, process.stderr
