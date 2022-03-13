#include <iostream>

int main()
{   
    auto var1 {12};
    auto var2 {13.0};
    auto var3 {14.0f};
    auto var4 {15.0l};
    auto var5 {'e'};

    // Utililzando com modificadores de inteiros
    auto var6 {123u}; // unsigned
    auto var7 {123ul}; // unsigned long
    auto var8 {123ll}; // long long

    std::cout << "var1 ocupa: " << sizeof(var1) << " bytes" << std::endl;
    std::cout << "var2 ocupa: " << sizeof(var2) << " bytes" << std::endl;
    std::cout << "var3 ocupa: " << sizeof(var3) << " bytes" << std::endl;
    std::cout << "var4 ocupa: " << sizeof(var4) << " bytes" << std::endl;
    std::cout << "var5 ocupa: " << sizeof(var5) << " bytes" << std::endl;
    std::cout << "var6 ocupa: " << sizeof(var6) << " bytes" << std::endl;
    std::cout << "var7 ocupa: " << sizeof(var7) << " bytes" << std::endl;
    std::cout << "var8 ocupa: " << sizeof(var8) << " bytes" << std::endl;

    return 0;
}