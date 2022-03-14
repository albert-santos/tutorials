#include <iostream>

int main()
{   
    //Declarando um array de inteiros
    //int scores[10];

    // Lendo o dado do array
    //std:: cout << "Scores [0]: " << scores[0] << std::endl;

/*
    // Lendo os dados por meio de um loop
    for (size_t i {0}; i < 10; ++i){
        std::cout << "Scores ["<< i << "]: " << scores[i] << std::endl;
    }

*/

/*

    // Atribuindo dados dentro do array
    scores[0] = 20;
    scores[1] = 21;
    scores[2] = 22;

    //Exibe a saída do array
    for (size_t i {0}; i < 10; ++i){
        std::cout << "Scores ["<< i << "]: " << scores[i] << std::endl;
    }
*/


/*

    for (size_t i{0}; i <10; ++i){
        scores[i] = i*10;
    }

    //Exibe a saída do array
    for (size_t i {0}; i < 10; ++i){
        std::cout << "Scores ["<< i << "]: " << scores[i] << std::endl;
    }
*/


/*
    double salaries[5] {12.7, 7.3, 13.2, 8.1, 9.3};

    for(size_t i{0}; i<5; ++i){
        std::cout << "Salary[" << i << "]: " << salaries[i] << std::endl;
    }
*/


/*

    int families[5] {12, 7, 5};

    for(size_t i{0}; i<5; ++i){
        std::cout << "Salary[" << i << "]: " << families[i] << std::endl;
    }

*/


/*
    // Omitindo o tamanho na declaração do array
    int class_sizes[] {10, 12, 15, 11, 18, 23};

    for (auto value : class_sizes){
        std::cout <<"Value: " << value << std::endl;
    }
*/


    int scores [] {2, 5, 8, 2, 5, 6, 9};
    int sum{0};

    for (int element : scores){
        sum += element;
    }
    std::cout << "Score sum: " << sum << std::endl;



    return 0;
}