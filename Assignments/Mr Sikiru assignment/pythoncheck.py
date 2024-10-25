import os
import sys
import platform

operating_system = platform.system()
print("Python Operating System: ", operating_system)

version = platform.python_version()
print("Python version: ", version)

home = os.path.dirname(sys.executable)
print("Python Home: ", home)

vendorUrl = platform.vendor_info()
print("Python Class Path: ", vendorUrl)

classPath = platform.vendor_info()
print("Python Class Path: ", classPath)