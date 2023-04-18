import subprocess
import base64
import json

from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view

from .code_runner import CodeRunner

@api_view(['POST'])
def run_single(request):
    if not (request.data.get('src_code_base64') and request.data.get('lang') and request.data.get('input')):
        return JsonResponse({'error': 'src_code_base64, lang, input required'}, status=400)
    code_runner = CodeRunner()
    res = code_runner.run_code_single_input(base64.b64decode(request.data.get('src_code_base64')).decode('utf-8'), request.data.get('lang'), request.data.get('input'))
    return JsonResponse(res,
                        safe=False, status=status.HTTP_200_OK)

@api_view(['POST'])
def run_multiple(request):
    if not (request.data.get('src_code_base64') and request.data.get('lang') and request.data.get('inputs')):
        return JsonResponse({'error': 'src_code, lang, inputs required'}, status=400)
    code_runner = CodeRunner()
    res = code_runner.run_code_multiple_input(base64.b64decode(request.data.get('src_code_base64')).decode('utf-8'), request.data.get('lang'), request.data.get('inputs'))
    return JsonResponse(res,
                        safe=False, status=status.HTTP_200_OK)