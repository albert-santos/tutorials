#include <iostream>

template <typename T> T maximum(T a, T b) {
    return (a>b)? a : b;
}

template <>
const char* maximum<const char*>(const char* a, const char* b){
    
}

int main() {
    
    int a{10};
    int b{23};
    double c{34.7};
    double d{23.4};
    std::string e{"Hello"};
    std::string f{"World"};

    auto max_int = maximum(a, b);
    auto max_double = maximum(c, d);
    std::string max_str = maximum(e, f);

    std::cout << "max_int: " << max_int << std::endl;
    std::cout << "max_double: " << max_double << std::endl;
    std::cout << "max_str: " << max_str << std::endl;
    

    const char* g{"Wild"};
    const char* h{"Animal"};

    auto result = maximum(g,h);
    std::cout << "max(const char*): " << result << std::endl;
    

    return 0;
}