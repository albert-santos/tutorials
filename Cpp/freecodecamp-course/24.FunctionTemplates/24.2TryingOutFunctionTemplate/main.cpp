#include <iostream>

template <typename T>
T maximum(T a, T b) {
    return (a > b) ? a:b;
}

int main() {
    double x{5.5};
    double y{78.7};

    auto result = maximum(x, y);
    std::cout << "result: " << result << std::endl;

    return 0;
}