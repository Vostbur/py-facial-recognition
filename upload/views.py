import os

from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm

import face_recognition


def handle_uploaded_file(f):
    with open("image.jpg", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def check_image():
    images = os.listdir("media/images")
    image_to_be_matched = face_recognition.load_image_file("image.jpg")
    image_to_be_matched_encoded = face_recognition.face_encodings(
        image_to_be_matched)[0]

    for image in images:
        current_image = face_recognition.load_image_file(
            "media/images/" + image)
        current_image_encoded = face_recognition.face_encodings(
            current_image)[0]
        result = face_recognition.compare_faces(
            [image_to_be_matched_encoded], current_image_encoded
        )
        if result[0]:
            return True

    return False


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["imgfile"])
            if check_image():
                return HttpResponse("Ok")
            return HttpResponse("Not Ok")
    else:
        form = UploadFileForm()
    return render(request, "index.html", {"form": form})
