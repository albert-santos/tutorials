#include "person.h"
#include "engineer.h"
#include <iostream>

Engineer::Engineer()
{
    std::cout << "Default constructor for Engineer called..." << std::endl;
}

Engineer::Engineer(std::string_view fullName, int age, std::string_view address, int contract_count_param)
    : Person(fullName, age, address), contract_count(contract_count_param)
    {
        std::cout << "Custom constructor called for Enginner ... " << std::endl;
    }

std::ostream& operator<<(std::ostream& out , const Engineer& operand){
     out << "Engineer [Full name : " << operand.get_full_name() <<
                    ",age : " << operand.get_age() << 
                    ",address : " << operand.get_address() <<
                    ",contract_count : " << operand.get_contract_count() << "]";
    return out;
}


Engineer::~Engineer()
{
}
