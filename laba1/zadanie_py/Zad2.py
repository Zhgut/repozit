from ctypes import windll, byref, Structure, Array, wintypes
class ULONGLONG(Structure):
  _fields_ = [("RAM", wintypes.ULONG),]
perem = ULONGLONG()
kernel32 = windll.kernel32
kernel32.GetPhysicallyInstalledSystemMemory(byref(perem))
print("RAM=", perem.RAM/1024/1024)
