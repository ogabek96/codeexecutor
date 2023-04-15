from codexec.code_runner import CodeRunner

code_runner = CodeRunner()
import time

source = """
public class Solution
{
    public static void main(String []args)
    {
        System.out.println("My First Java Program.");
    }
};
    """
inp = []
for i in range(1):
    inp.append('Ogabek' + str(i))
now = time.time_ns() / 1000000000
res = code_runner.run_code_single_input('Solution.java', source, 'java', '')
then = time.time_ns() / 1000000000
print("runtime: " + str(then - now) + 's')
print(res)