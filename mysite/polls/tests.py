from django.test import TestCase

# Create your tests here.

from .models import *
from django.utils import timezone


class ModelTestCase(TestCase):
    def setUp(self):
        q = Question.objects.create(
            question_text="To be or not to be, THAT is the question.",
            pub_date=timezone.now(),
        )
        Choice.objects.create(question=q, choice_text="To be")

    def test_question(self):
        q = Question.objects.get(
            question_text="To be or not to be, THAT is the question."
        )
        self.assertEqual(q.was_published_recently(), True)
