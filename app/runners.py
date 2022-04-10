import os
import subprocess


def py_runner(source):

    command = f'python3 {source}'
    results = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')

    return results


def c_runner(source):
    # compile code in a subprocess, get result
    
    source_fn, source_ext = os.path.splitext(source)
    compilation_command = f'gcc -o {source_fn} {source}'
    compilation_results = subprocess.run(
        compilation_command, shell=True, capture_output=True, text=True, encoding='utf-8')
    # check return_code, stdout, stderr : if return_code non zero, return results
    if compilation_results.returncode != 0:
        return compilation_results
    # execute resulting executable, get result
    execution_command = f'./{source_fn}'
    execution_results = subprocess.run(
        execution_command, shell=True, capture_output=True, text=True, encoding='utf-8')
    # return results
    return execution_results


def cpp_runner(source):
    # compile code in a subprocess, get result
    source_fn, source_ext = os.path.splitext(source)
    compilation_command = f'g++ -o {source_fn} {source}'
    compilation_results = subprocess.run(
        compilation_command, shell=True, capture_output=True, text=True, encoding='utf-8')
    # check return_code, stdout, stderr : if return_code non zero, return results
    if compilation_results.returncode != 0:
        return compilation_results
    # execute resulting executable, get result
    execution_command = f'./{source_fn}'
    execution_results = subprocess.run(
        execution_command, shell=True, capture_output=True, text=True, encoding='utf-8')
    # return results
    return execution_results


def js_runner(source):

    command = f'node {source}'
    results = subprocess.run(
        command, shell=True, capture_output=True, text=True, encoding='utf-8')

    return results


if __name__ == '__main__':

    assert py_runner('hello.py').stdout == 'Hello World!\n'
    assert c_runner('hello.c').stdout == 'Hello World!'
    assert cpp_runner('hello.cpp').stdout == 'Hello World!'
    assert js_runner('hello.js').stdout == 'Hello World!\n'
