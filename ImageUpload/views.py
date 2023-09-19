from django.shortcuts import render, redirect
from .forms import ImageUploadForm, ImageDeleteForm
from .models import Image


def form_upload(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/images/')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_img.html', {'form': form})

def list_of_files(request):
    images = Image.objects.all()
    delete_form = ImageDeleteForm(request.POST or None)

    if request.method == "POST":
        if delete_form.is_valid():
            images_to_delete = Image.objects.filter(id__in=request.POST.getlist('to_delete'))
            for image in images_to_delete:
                image.delete()
            return redirect('/images/')

    return render(request, 'list_of_images.html', {'images': images, 'delete_form': delete_form})
