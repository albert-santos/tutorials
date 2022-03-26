#include <iostream>
#include <type_traits>
#include <concepts>


//Sintaxe 1
template <typename T>
concept MyIntegral = std::is_integral_v<T>;


template <typename T>
requires MyIntegral<T>
T add(T a, T b) {
    return a + b;
}

int main() {
    int a {5};
    int b{7};

    auto result = add(a, b);

    std::cout << "result: " << result << std::endl;
    
    return 0;
}