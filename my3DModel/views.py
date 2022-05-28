from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage

from .forms import MyModelForm
from .models import threeDmodels
# Create your views here.
def home(request):
    return render(request,'3D_Model.html')

def upload(request):
    context={}
    if request.method == 'POST':
        uploaded_files=request.FILES['document']
        print(uploaded_files.name,"My file")
        fs = FileSystemStorage()
        name = fs.save(uploaded_files.name, uploaded_files)
        context['myurl'] = fs.url(name)
    return render(request, 'upload.html', context)

def showModel(request, modelid): #,modelfile
    MyModel = threeDmodels.objects.get(id = modelid)
    ModelName = MyModel.modelfile
    return render(request, 'Load3D.html', {'ModelName':ModelName}) #

def model_list(request):
    MyModels = threeDmodels.objects.all()
    #print(MyModels[0])
    return render(request, '3D_Model.html', {'MyModels':MyModels})

def upload_model(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('model_list')
    else:
        form = MyModelForm()
    return render(request, 'upload_model.html', {'form':form})

