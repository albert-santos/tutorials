#include <iostream>

template <typename T>  T maximum(T a, T b){
    return (a > b) ?a:b;
}


int main() {

    int a{10};
    int b{23};
    double c{34.7};
    double d{23.4};

    std::string e{"hello"};
    std::string f{"world"};

    auto max = maximum<int>(a,b);
    std::cout << "max: " << max << std::endl;

    auto max2 = maximum<double>(a,b);
    std::cout << "max: " << max2 << std::endl;
    

    return 0;
}