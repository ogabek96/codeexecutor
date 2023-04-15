from codexec.code_runner import CodeRunner

code_runner = CodeRunner()
import time

source = """
process.stdin.on('data', data => {
  console.log(`You typed ${data.toString()}`);
  process.exit();
});
    """
inp = []
for i in range(10):
    inp.append('Ogabek' + str(i))
now = time.time_ns() / 1000000000
res = code_runner.run_code_multiple_input(source, 'node', inp)
then = time.time_ns() / 1000000000
print("runtime: " + str(then - now) + 's')
print(res)