from django.shortcuts import render

def code_editor(request):
    return render(request, 'code_editor.html')
