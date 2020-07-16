#include <iostream>

using namespace std;


int main() {
	// your code goes here
	int hours, minutes;
    int hours_to_seconds, minutes_to_seconds;
    int hour_seconds=3600;
    int minute_seconds=60;
	std::cout <<"Ingrese las horas: "<< std::endl; 
	std::cin >> hours;
    std::cout <<"Ingrese los minutos: "<< std::endl; 
	std::cin >> minutes;
	
    hours_to_seconds=hours*hour_seconds;
    minutes_to_seconds=minutes*minute_seconds;

    std::cout << "Existen "<< hours_to_seconds+minutes_to_seconds << " segundos en "<< hours << " hora(s) y " << minutes << "minuto(s)." << std::endl; 
	
	return 0;
}
