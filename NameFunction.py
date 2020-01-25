import CalculatorModule

print("\n")
print("------------------------------------------------------------------------")
print("__name__ function have two work to done")
print("1 : if we run particular file and its have __name__ in this file , it will return __main__ , because"
      "this file is the entry gate for the module")
print("2 : if __name__ written in any imported module , so it will return module name (means file name of imported file)")
print("\n")
print("-------------------------------------------------------------------------")
print("This file is entry point , so this will show output as a __main__")
print("but here we import CalculatorModule and this module also have __name__ , so this __name__ will return module name, because"
      "we calling this module from NameFunction file")
print("But if we call CalculatorModule Seperatedly , it will show you output as __main__, because on that time"
      "this file act as a entry point")

print("\n")
print("-------------------------------------------------------------------------")
print("__name__ in NameFunction: ",__name__)