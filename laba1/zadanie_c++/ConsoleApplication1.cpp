#include "pch.h"
#include <iostream>
#include <windows.h>

//не описана в заголовочнике
extern "C" __declspec(dllimport)
BOOL __stdcall GetPhysicallyInstalledSystemMemory(PULONGLONG);

int main()
{
	ULONGLONG TotalMemoryInKilobytes;
	GetPhysicallyInstalledSystemMemory(&TotalMemoryInKilobytes);
	std::cout << TotalMemoryInKilobytes << " kB" << std::endl;
	return 0;
}
