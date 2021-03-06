# coding=utf-8
from django.test import SimpleTestCase as TestCase
from django_sae.utils.taskqueue import get_queue, get_queue_size


class TaskQueueTest(TestCase):
    def test_get_queue(self):
        queue_name = 'test'
        queue1 = get_queue(queue_name)
        queue2 = get_queue(queue_name)
        self.assertEqual(queue1, queue2)

    def test_get_queue_size(self):
        self.assertEqual(0, get_queue_size('queue1'))
        self.assertEqual(0, get_queue_size(['queue1', 'queue2']))