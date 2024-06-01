import unittest
from queue import Queue

class QueueTests(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size, 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size, 2)

    def test_dequeue(self):
        self.assertIsNone(self.queue.dequeue())
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.size, 1)

    def test_size(self):
        self.assertEqual(self.queue.size, 0)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size, 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size, 2)

if __name__ == '__main__':
    unittest.main()