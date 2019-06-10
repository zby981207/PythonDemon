import sys
sys.path.append("/pack")

from pack import customMath as math
from pack.customPrint import formatedPrint

formatedPrint(math.square(3))
formatedPrint(math.absolute(5))
formatedPrint(math.isPrime(7))