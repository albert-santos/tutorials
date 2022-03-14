#include <iostream>

int main()
{   
    int scores[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    //int count{std::size(scores)}; //std::size (C++17)

    int i {0};
    for(auto value : scores) {
        std::cout << "Value["<< i << "]: " << value << std::endl;
        ++i;
    }

}