#include <iostream>

int main() {
    
    //capture lists

    double a{10};
    double b {20};

    auto func= [a, b]() {
        std::cout << "a + b: " << a + b << std::endl;
    };

    func();

    return 0;
}