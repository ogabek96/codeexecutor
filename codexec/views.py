import subprocess
import json

from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view

from .code_runner import CodeRunner

@api_view(['POST'])
def run(request):
    if not (request.data.get('src_code') and request.data.get('lang') and request.data.get('input')):
        return JsonResponse({'error': 'src_code, lang, input required'}, status=400)
    code_runner = CodeRunner()
    res = code_runner.run_code_single_input(request.data.get('src_code'), request.data.get('lang'), request.data.get('input'))
    return JsonResponse(res,
                        safe=False, status=status.HTTP_200_OK)