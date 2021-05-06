

class RadixSort(object):

    def sort(self, array, base=10):
        if array is None:
            raise TypeError('array cannot be None')
        if not array:
            return []
        max_element = max(array)
        max_digits = len(str(abs(max_element)))
        curr_array = array
        
        for digit in range(max_digits):
            buckets = [[] for _ in range(base)]
            for item in curr_array:
                buckets[(item//(base**digit))%base].append(item)
            curr_array = []
            
            for bucket in buckets:
                curr_array.extend(bucket)
        return curr_array
      
      
      
import unittest


class TestRadixSort(unittest.TestCase):

    def test_sort(self):
        radix_sort = RadixSort()
        self.assertRaises(TypeError, radix_sort.sort, None)
        self.assertEqual(radix_sort.sort([]), [])
        array = [128, 256, 164, 8, 2, 148, 212, 242, 244]
        expected = [2, 8, 128, 148, 164, 212, 242, 244, 256]
        self.assertEqual(radix_sort.sort(array), expected)
        print('Success: test_sort')


def main():
    test = TestRadixSort()
    test.test_sort()


if __name__ == '__main__':
    main()
    
    
    
    
