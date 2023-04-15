from codexec.code_runner import CodeRunner

code_runner = CodeRunner()
import time

source = """

// C++ program to display "Hello World"
 
// Header file for input output functions
#include <iostream>
using namespace std;
 
// Main() function: where the execution of program begins
int main()
{
    // prints hello world
    cout << "Hello World";
 
    return 0;
}
    """
inp = []
for i in range(1):
    inp.append('Ogabek' + str(i))
now = time.time_ns() / 1000000000
res = code_runner.run_code_single_input('solution.cpp', source, 'cpp', '')
then = time.time_ns() / 1000000000
print("runtime: " + str(then - now) + 's')
print(res)