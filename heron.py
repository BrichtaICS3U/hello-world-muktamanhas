#Heron's Method for Calculating Square Roots
#Stub by JP Brichta, March 2018
#
#Heron's method for calculating square roots is approximately 2000 years old and was devised by Hero of Alexandria. It is an
#iterative method (meaning that it uses a previous answer to calculate the next) that in principle, will continue forever.
#When using iterative method, it is important to decide if the answer is "good enough" or if the program should continue.
#You can read more about Heron's Method and other methods of computing square roots in the wikipedia entry here:
#https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method
#

def heron(x, accuracy=0.001):
  """Compute the square root of the number x using Heron's method. The accuracy is defaulted to three decimal places, but you
  can use a larger or smaller number if you wish. The smaller the number, the more time the calculation will take."""
  G = x/2
  while G**2 - x > 0.001:
    G = (G + x/G) / 2
  return (round(G,3))
