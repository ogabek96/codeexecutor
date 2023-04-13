import subprocess
from django.http import HttpResponse
from .codeexecute import exec_command

def index(request):
    return HttpResponse(exec_command('python', 'echo.py'))