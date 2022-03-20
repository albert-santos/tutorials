#include <iostream>

// Funções com apenas um parâmetro e que não retornam nada
// Declaração da função
void enter_bar(size_t age) { // Parâmetros da função
    if (age >= 18) {
        std::cout << "Voce tem " << age <<". Pode beber a vontade" << std::endl;
    }else{
        std::cout << "Muito novo para isso!" << std::endl;
    }
}


// Declaração de uma função que recebe mais de um parâmetro e retorna algo 
int max(int a, int b) {
    if (a>b) {
        return a;
    }else{
        return b;
    } 
}


// Função que não tem parâmetros e não retorna nada
void say_hello() {
    std::cout << "Hello there" << std::endl;
}


// Função que não tem parâmetros e retorna algo
int lucky_number() {
    return 99;
}


// Os argumentos passados para a função geram cópias cuja alterações são visíveis apenas dentro do escopo da função
// Ou seja, os argumentos que estavam fora da função permanecem inalterados
double increment_multiply (double a, double b) {
    std::cout << "Dentro da função, antes do incremento: " << std::endl;
    std::cout << "a: " << a << std::endl;
    std::cout << "b: " << b << std::endl;

    double result = ((++a))* ((++b));

    std::cout << "Dentro da função, após o incremento: " << std::endl;
    std::cout << "a: " << a << std::endl;
    std::cout << "b: " << b << std::endl;

    return result;
}


int main()
{   
   
   //enter_bar(15); //argumento da função

    /*
   for (size_t i{1} ; i<20 ; ++i){
       enter_bar(i); // Passando o valor de i como argumento da função
   }
    */

/*
   // Chamando a função max
   int result = max(10, 20); // passando os argumentos da função e armazenado o retorna da função na variável result
   std::cout << "max: " << result << std::endl;
*/

/*
    // Chamando função hello
    say_hello();
*/

/*
    int result{};
    result = lucky_number();
    std::cout << "Result: " << result << std::endl;
*/  

    double h {3.00};
    double i {4.00};

    std::cout << "Fora da função, antes do incremento" << std::endl;
    std::cout << "h: " << h << std::endl;
    std::cout << "i: " << i << std::endl;

    double result = increment_multiply(h, i);

    std::cout << "Fora da função, depois do incremento" << std::endl;
    std::cout << "h: " << h << std::endl;
    std::cout << "i: " << h << std::endl;

    return 0;
}