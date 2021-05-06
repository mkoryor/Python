

from __future__ import division


class QuickSort(object):

    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        return self._sort(data)

    def _sort(self, data):
        if len(data) < 2:
            return data
        equal = []
        left = []
        right = []
        pivot_index = len(data) // 2
        pivot_value = data[pivot_index]
        # Build the left and right partitions
        for item in data:
            if item == pivot_value:
                equal.append(item)
            elif item < pivot_value:
                left.append(item)
            else:
                right.append(item)
        # Recursively apply quick_sort
        left_ = self._sort(left)
        right_ = self._sort(right)
        return left_ + equal + right_
      
      
      
      
          
      
      
import unittest


class TestQuickSort(unittest.TestCase):

    def test_quick_sort(self):
        quick_sort = QuickSort()

        print('None input')
        self.assertRaises(TypeError, quick_sort.sort, None)

        print('Empty input')
        self.assertEqual(quick_sort.sort([]), [])

        print('One element')
        self.assertEqual(quick_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        self.assertEqual(quick_sort.sort(data), sorted(data))

        print('Success: test_quick_sort\n')


def main():
    test = TestQuickSort()
    test.test_quick_sort()


if __name__ == '__main__':
    main()
