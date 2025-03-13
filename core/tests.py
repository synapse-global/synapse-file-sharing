from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from core.models import Files
import os


class FilesModelTest(TestCase):
    def setUp(self):
        self.file = Files.objects.create(
            file=SimpleUploadedFile("test.txt", b"Test file content"),
            key="test-key",
            name="Test File"
            )

    def test_file_creation(self):
        self.assertEqual(Files.objects.count(), 1)

    def test_str_representation(self):
        self.assertEqual(str(self.file), "test-key")

    def test_unique_key_constraint(self):
        with self.assertRaises(Exception):
            Files.objects.create(
                file=SimpleUploadedFile("test2.txt", b"Another content"),
                key="test-key",
                name="Duplicate Key File"
                )


class GetFileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.file = Files.objects.create(
            file=SimpleUploadedFile("test.txt", b"Test file content"),
            key="test-key",
            name="Test File"
            )

    def test_get_existing_file(self):
        response = self.client.get(reverse("get_file", args=["test-key"]))
        self.assertEqual(response.status_code, 200)

        expected_filename = os.path.basename(self.file.file.name)
        self.assertEqual(response["Content-Disposition"], f'inline; filename="files/{expected_filename}"')

    def test_get_non_existing_file(self):
        response = self.client.get(reverse("get_file", args=["wrong-key"]))
        self.assertEqual(response.status_code, 404)


class FilesAdminTest(TestCase):
    def setUp(self):
        self.file = Files.objects.create(
            file=SimpleUploadedFile("test.txt", b"Test file content"),
            key="test-key",
            name="Test File"
            )

    def test_file_url_generation(self):
        url = f"http://localhost/admin/files/{self.file.key}"
        self.assertIn(self.file.key, url)