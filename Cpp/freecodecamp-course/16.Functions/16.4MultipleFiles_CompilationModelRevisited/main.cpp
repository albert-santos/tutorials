#include <iostream>
#include "compare.h" //Preprocessor
#include "operations.h" // Preprocessor

int main()
{   
    int maximum = max(134, 56);
    std::cout << "max: " << maximum << std::endl;

    int minimum = min(145, 23);
    std::cout << "min: "<< minimum <<std::endl;

    int result = incr_mult(2, 5);
    std::cout << "result: " << result << std::endl;

    return 0;
}