from ctypes import windll, byref, Structure, Array, wintypes

# Опишем структуру SYSTEM_INFO в виде класса, с помощью типов данных Windows, описанных в ctypes.wintypes

class SYSTEM_INFO(Structure):
    _fields_ = [("wProcessorArchitecture", wintypes.WORD),
                ("wReserved", wintypes.WORD),
                ("dwPageSize", wintypes.DWORD),
                ("lpMinimumApplicationAddress", wintypes.LPVOID),
                ("lpMaximumApplicationAddress", wintypes.LPVOID),
                ("dwActiveProcessorMask", wintypes.LPVOID),
                ("dwNumberOfProcessors", wintypes.DWORD),
                ("dwProcessorType", wintypes.DWORD),
                ("dwAllocationGranularity", wintypes.DWORD),
                ("wProcessorLevel", wintypes.WORD),
                ("wProcessorRevision", wintypes.WORD)]


# создаём переменную, являющуюся экзкмпляром класса SYSTEM_INFO
si = SYSTEM_INFO()

# загружаем динамическую библиотеку kernel32.dll
kernel32 = windll.kernel32

# вызываем функцию GetSystemInfo, передавая ей переменную si по ссылке
kernel32.GetSystemInfo(byref(si))

# после вызова функции выводим содержимое полей структуры SYSTEM_INFO
print("%s: %s (0x%x)" % ("Processor Architecture", si.wProcessorArchitecture, si.wProcessorArchitecture))
print("%s: %s (0x%x)" % ("Number of Processors", si.dwNumberOfProcessors, si.dwNumberOfProcessors))
print("%s: %s (0x%x)" % ("Page Size", si.dwPageSize, si.dwPageSize))
print("%s: %s (0x%x)" % ("Processor Level", si.wProcessorLevel, si.wProcessorLevel))
print("%s: %s (0x%x)" % ("Processor Revision", si.wProcessorRevision, si.wProcessorRevision))
print("%s: %s (0x%x)" % ("Minimum Application Address", si.lpMinimumApplicationAddress, si.lpMinimumApplicationAddress))
print("%s: %s (0x%x)" % ("Maximum Application Address", si.lpMaximumApplicationAddress, si.lpMaximumApplicationAddress))
print("%s: %s (0x%x)" % ("Active Processor Mask", si.dwActiveProcessorMask, si.dwActiveProcessorMask))