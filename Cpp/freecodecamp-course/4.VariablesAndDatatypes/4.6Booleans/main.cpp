#include <iostream>

int main()
{   
    bool red_light {true};
    bool green_light {false};

    if(red_light == true){
        std::cout << "Stop !" << std::endl;
    }else{
        std::cout << "Go through!" << std::endl;
    }


    // Exibindo o valor de uma variável booleana
    std::cout << "red_light: " << red_light << std::endl;
    std::cout << "green_light: " << green_light << std::endl;

    // Exibir true ou false ao invés de 1 ou 0 
    std::cout << std::boolalpha;
    std::cout << "red_light: " << red_light << std::endl;
    std::cout << "green_light: " << green_light << std::endl;



    return 0;
}