#include <iostream>

using namespace std;

void loop_recursivo (string message,int number_times);

int main() {
	// your code goes here
    string message;
	int number_times;    
	std::cout <<"Ingrese un mensaje: "<< std::endl; 
	std::cin >> message;
    std::cout <<"¿Cuántas veces desea ver el mensaje?"<< std::endl; 
	std::cin >> number_times;
	
    std::cout << "*******";
    loop_recursivo(message ,number_times);
    std::cout << "*******";
    
	
	return 0;
}

void loop_recursivo (string message,int number_times){
    if (number_times>1){
        number_times--;
        loop_recursivo(message,number_times);
    }
    std::cout << message << std::endl; 
}