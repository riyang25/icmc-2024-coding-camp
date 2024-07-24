from pyodide.console import BANNER, PyodideConsole, repr_shorten
from pyodide.code import CodeRunner
from pyodide.ffi import to_js
import __main__
import time

BANNER += "\nYou may need to refresh this page once to fully initialize the emulator."
__all__ = ["BANNER", "pycomplete", "exec_code"]

pyconsole = PyodideConsole(globals=__main__.__dict__, filename="<console>")


def pycomplete(source):
    return pyconsole.complete(source)


async def exec_code(
    code : str, syntax_check_passed, stdin_callback, stdout_callback, stderr_callback
):
    pyconsole.stdin_callback = stdin_callback
    pyconsole.stdout_callback = stdout_callback
    pyconsole.stderr_callback = stderr_callback

    # This can be used to execute a multiline block of code immediately.
#     code_runner = CodeRunner("""
# try:
#     import random
#     a = int(input("stuff: "))
#     for i in range(a):
#         print(i)
#     print(a, random.randint(1, 6))
# except:
#     print("An error occurred. Program ended.")
# """)
#     code_runner.compile()
#     await pyconsole.runcode("", code_runner)

    for line in code.splitlines():
        fut = pyconsole.push(line)
        if fut.syntax_check == "syntax-error":
            return to_js([-1, fut.formatted_error])
    syntax_check_passed()
    try:
        result = await fut
        repr_result = repr_shorten(result) if result is not None else None
        return to_js([0, repr_result])
    except Exception:
        return to_js([-1, fut.formatted_error])
