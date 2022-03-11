#include <iostream>

int main()
{   
    
    //Variable may contain random garbage value. WARNING
    int elephant_count;

    int lion_count {}; // inicializa com zero

    int dog_count {10}; // inicializa com 10

    int cat_count {15}; // inicializa com 15

    // Expressões podem ser utilizadas para inicializar uma variável
    int domesticated_animals {dog_count + cat_count};

    // int new_number{doesnt_exist};

    // // Gera erro. Informando que haverá conversão de 2.9 para 2
    // int narrowing_conversion{2.9}

    std::cout << "Elephant count: " << elephant_count << std::endl;
    std::cout << "Lion count: " << lion_count << std::endl;
    std::cout << "Dog count: " << dog_count << std::endl;
    std::cout << "Cat count: " << cat_count << std::endl;
    std::cout << "Domesticated count: " << domesticated_animals << std::endl;


    // Verificando o tamanho da variável com  o sizeof
    // Quanto de memória cada tipo de variável ocupa
    std::cout << "sizeof int: " << sizeof(int) << std::endl;
    std::cout << "sizeof Elephant_count: " << sizeof(elephant_count) << std::endl;

    return 0;
}