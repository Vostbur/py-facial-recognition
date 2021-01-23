import pickle
import base64

from django.db import models

import numpy as np
from PIL import Image
from face_recognition import face_encodings


def detect_face(image):
    image_np_array = np.array(Image.open(image))
    hash_np_array = face_encodings(image_np_array)[0]
    hash_np_bytes = pickle.dumps(hash_np_array)
    hash_base64 = base64.b64encode(hash_np_bytes)
    return hash_base64


class FaceImage(models.Model):
    image = models.ImageField(upload_to="images")
    name = models.CharField(max_length=100)
    face_hash = models.BinaryField(blank=True, null=True)

    def save(self, *args, **kwargs):
        face_hash = detect_face(self.image)
        self.face_hash = face_hash
        return super(FaceImage, self).save(*args, **kwargs)
