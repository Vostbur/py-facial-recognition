import base64
import pickle
from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import face_recognition
import numpy as np
from PIL import Image

from .models import FaceImage
from .forms import UploadFileForm


def check_image(image):
    image_to_be_matched_encoded = face_recognition.face_encodings(image)[0]

    hashes = FaceImage.objects.all()
    for i in hashes:
        np_bytes = base64.b64decode(i.face_hash)
        np_array = pickle.loads(np_bytes)

        result = face_recognition.compare_faces(
            [image_to_be_matched_encoded], np_array
        )
        if result[0]:
            return True, {'name': i.name}

    return False, {}


@api_view(["POST", "GET"])
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image_bytes = request.FILES["imgfile"].read()
            image = np.array(Image.open(BytesIO(image_bytes)))

            result, person = check_image(image)
            if result:
                return Response(person, status=status.HTTP_200_OK)
            return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        form = UploadFileForm()
    return render(request, "index.html", {"form": form})


class AuthPerson(APIView):
    def get(self, request):
        msg = 'Hello'
        return HttpResponse(msg, content_type='text/plain')

    def post(self, request):
        image_bytes = request.data["imgfile"].read()
        image = np.array(Image.open(BytesIO(image_bytes)))
        result, person = check_image(image)
        if result:
            return Response(person, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
