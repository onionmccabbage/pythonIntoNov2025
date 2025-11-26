# Python has acces to teh operating system via 'sys' (and also via 'os')
import sys

# we may choose to define an additional path where Python should look if we import stuff
sys.path.append("D:\\pythonIntoNov2025\\my_assets")

# we can examine the current system path that python is aware of
print(sys.path)