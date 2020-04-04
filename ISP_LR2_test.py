import unittest
import sys
#sys.path.append("C:\\Users\\User\\source\\repos\\ISP_LR2_test\\ISP_LR2_test\\ISP_LR2_2\\ISP_LR2_2")
#sys.path.append("C:\\Users\\User\\source\\repos\\ISP_LR2_test\\ISP_LR2_test\\ISP_LR2_2\\ISP_LR2_2")
#sys.path.append("C:\\Users\\User\\source\\repos\\ISP_LR2_test\\ISP_LR2_test\\ISP_LR2_3\\ISP_LR2_3")
##sys.path.append("C:\\Users\\User\\source\\repos\\ISP_LR2_test\\ISP_LR2_test\\ISP_LR2_4\\ISP_LR2_4")
#import ISP_LR2_1
#import ISP_LR2_2
#import ISP_LR2_3
#import ISP_LR2_4
import my1
import my2
#print ('\n---------------------\n')
import my3
#print ('\n---------------------\n')
import my4
#print ('\n---------------------\n')

#path = "C:\\Users\\User\\source\\repos\\ISP_LR2_test\\ISP_LR2_test\\ISP_LR2_1\\ISP_LR2_1\\temp1.txt"
#path = "C:\\Users\\User\\source\\repos\\ISP_LR2_test\\ISP_LR2_test\\temp1.txt"
sort_nums = "23 34 12 11 32 12 56 90 74 65 23 34 12 11 32 12 56 90 74 65 23 34 12 11 32 12 56 90 74 65"
sample_sotred_nums = "11 11 11 12 12 12 12 12 12 23 23 23 32 32 32 34 34 34 56 56 56 65 65 65 74 74 74 90 90 90"


class TestLab(unittest.TestCase):

  def test_external_sort(self):
      with open('temp1.txt', 'w') as file:
          file.write(sort_nums)
      my1.ExternSort()
      with open('temp1.txt', 'r') as file:
          sorted_nums = file.read()
      a = sorted_nums == sample_sotred_nums
      self.assertTrue(a)

  def test_to_json(self):
      with open('my_cash_2.txt', 'w') as file:
          file.write(my2.ToJsonTest())
      procesed_string = ''
      with open('my_cash_2.txt', 'r') as file:
          processed_string = file.read()
      with open('2_module_right.txt', 'r') as file:
          sample_string = file.read()
      a = processed_string == sample_string
      self.assertTrue(a)

  def test_vector(self):
      with open('my_cash_3.txt', 'w') as file:
          file.write(my3.ShowWork(my3.TestVector(3, [5, 6, 7]), my3.TestVector(3, [12, 0, 4]), my3.TestVector(2, [4, 5])))
      procesed_string = ''
      with open('my_cash_3.txt', 'r') as file:
          processed_string = file.read()
      with open('3_module_right.txt', 'r') as file:
          sample_string = file.read()
      a = processed_string == sample_string
      self.assertTrue(a)

  def test_decorator(self):
      with open('my_cash_4.txt', 'w') as file:
          file.write(my4.ShowWork())
      procesed_string = ''
      with open('my_cash_4.txt', 'r') as file:
          processed_string = file.read()
      with open('4_module_right.txt', 'r') as file:
          sample_string = file.read()
      a = processed_string == sample_string
      self.assertTrue(a)

if __name__ == '__main__':
    unittest.main()