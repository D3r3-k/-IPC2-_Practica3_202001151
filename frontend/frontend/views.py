from django.shortcuts import render

xml = ""

def index(request):
    # Render the index.html template in myapp/templates directory
    return render(request, 'index.html')

def borrar(request):
    # Render the borrar.html template in myapp/templates directory
    return render(request, 'borrar.html')

def cargar(request):
    global xml
    xml = request.GET.get('xml')
    context = {
        'xml': xml
    }
    if xml is not "" and xml is not None:
        response = request.post('http://localhost:5000/api/v1/mascotas', data=xml)
    # Render the cargar.html template in myapp/templates directory
    return render(request, 'cargar.html', context)

def procesar(request):
    # Render the procesar.html template in myapp/templates directory
    return render(request, 'procesar.html')

def datos(request):
    # Render the datos.html template in myapp/templates directory
    return render(request, 'datos.html')

