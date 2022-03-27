#include <iostream>

class Dog{
    public:
        std::string m_name; // Member variable
};

struct Cat{
    std::string  m_name;
};


int main()
{   
    Dog dog1;
    Cat cat1;

    dog1.m_name = "Sansao"; // Erro de compilação porque a variável é privada
    cat1.m_name = "Floco";

    std::cout << "cat name: " << cat1.m_name << std::endl;
    std::cout << "dog name: " << dog1.m_name << std::endl;

    return 0;
}