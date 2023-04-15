from codexec.isolate import Isolate


class CodeRunner:

    def __init__(self) -> None:
        self.lng = {
            'python3': {
                'file_name': 'solution.py',
                'compile_cmd': None,
                'run_cmd': ['/bin/python3', 'solution.py'] 
            },
            'java': {
                'file_name': 'Solution.java',
                'compile_cmd': ['/usr/bin/javac', 'Solution.java'],
                'run_cmd': ['/usr/bin/java', 'Solution']
            },
            'cpp': {
                'file_name': 'solution.cpp',
                'compile_cmd': ['/usr/bin/c++', 'solution.cpp'],
                'run_cmd': ['./a.out']
            },
            'go': {
                'file_name': 'solution.go',
                'compile_cmd': None,
                'run_cmd': ['/usr/local/go/bin/go', 'run', 'solution.go']
            },
            'node': {
                'file_name': 'solution.js',
                'compile_cmd': None,
                'run_cmd': ['/usr/bin/node', 'solution.js']
            }
        }

    def run_code_single_input(self, source_code,
                              src_language, stdin):
        isolate_box = Isolate()

        box_path = isolate_box.init_box()
        file_name = self.lng[src_language]['file_name']
        try:
            self._copy_source_code(box_path, file_name, source_code)
            self._compile_source_code(isolate_box, src_language)
            stdout, stderr = isolate_box.run_command(
                self.lng[src_language]['run_cmd'], stdin)
            return stdout, stderr
        except:
            print("Error running single input code")
        finally:
            isolate_box.cleanup()

    def run_code_multiple_input(self, source_code,
                                src_language, stdin_list):
        stdout_list = []

        isolate_box = Isolate()

        box_path = isolate_box.init_box()
        file_name = self.lng[src_language]['file_name']
        try:
            self._copy_source_code(box_path, file_name, source_code)
            self._compile_source_code(isolate_box, src_language)
            for stdin in stdin_list:
                stdout, stderr = isolate_box.run_command(
                    self.lng[src_language]['run_cmd'], stdin)
                stdout_list.append({'stdout': stdout, 'stderr': stderr})
        finally:
            isolate_box.cleanup()
        return stdout_list

    def _compile_source_code(self, isolate_box, code_lang):
        if self.lng[code_lang]['compile_cmd']:
            stdout, stderr = isolate_box.run_command(
                self.lng[code_lang]['compile_cmd'])
            return stdout, stderr
        return None, None

    def _copy_source_code(self, box_path, file_name, source_code):
        with open(box_path + '/box/' + file_name, 'w') as f:
            f.write(source_code)
