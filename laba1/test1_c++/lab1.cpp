#include "pch.h"
#include <windows.h>
#include <stdio.h>
#pragma comment(lib, "user32.lib")

void main()
{
	SYSTEM_INFO siSysInfo;

	// Copy the hardware information to the SYSTEM_INFO structure. 

	GetSystemInfo(&siSysInfo);

	// Display the contents of the SYSTEM_INFO structure. 

	printf("Hardware information: \n");
	printf("  Processor Architecture: %u\n", siSysInfo.wProcessorArchitecture);
	printf("  Number of processors: %u\n", siSysInfo.dwNumberOfProcessors);
	printf("  Page size: %u\n", siSysInfo.dwPageSize);
	printf("  Processor Level: %u\n", siSysInfo.wProcessorLevel);
	printf("  Processor Revision: %u\n", siSysInfo.wProcessorRevision);
	printf("  Minimum application address: %lx\n", siSysInfo.lpMinimumApplicationAddress);
	printf("  Maximum application address: %lx\n", siSysInfo.lpMaximumApplicationAddress);
	printf("  Active processor mask: %u\n", siSysInfo.dwActiveProcessorMask);
}