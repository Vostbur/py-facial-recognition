import os
import unittest
import face_recognition


def check_image(my_image, images):
    image_to_be_matched = face_recognition.load_image_file(my_image)
    image_to_be_matched_encoded = \
        face_recognition.face_encodings(image_to_be_matched)[0]

    for image in images:
        current_image = face_recognition.load_image_file("images/" + image)
        current_image_encoded = \
            face_recognition.face_encodings(current_image)[0]
        result = face_recognition.compare_faces(
            [image_to_be_matched_encoded], current_image_encoded)
        if result[0]:
            print("Matched: " + image)
            return True

    print("Not matched!")
    return False


class Test(unittest.TestCase):
    images = os.listdir("images")

    data = [
        ("Barney_Stinson.jpg", False),
        ("Sheldon-Cooper.jpg", True),
    ]

    def test_check_image(self):
        for [image, result] in self.data:
            print("check: " + image)
            self.assertEqual(check_image(image, self.images), result)


if __name__ == "__main__":
    unittest.main()
