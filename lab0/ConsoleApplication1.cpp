// ConsoleApplication1.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include "pch.h"
#include <iostream>
#include<fstream>

using namespace std;
	
int main()
{
	setlocale(LC_ALL, "Russian");
	ifstream in("input.txt");
	if (!in)
	{
		cout << "File not found" << endl;
		system("pause");
		return 1;
	}
	int n, count = 0, max=INT16_MIN, min=INT16_MAX;
	bool est=false;
	while (in >> n) ++count;

	in.clear();
	in.seekg(0, ios::beg);

	int * data = new int[count];
	count = 0;
	while (in >> n)
	{
		if (n >= max) max=n;
		if (n < min) min = n;
		data[count++] = n;
	}
	cout << "Не хватает: ";
	while (min < max)
	{
		min++;
		for (int i = 0; i < count; i++) 
			if (min == data[i])
			{
				est = true;
				break;
			}
		if (!est) cout << min<<" ";
		else est = false;
	}
	cout << "пакета.";

}
