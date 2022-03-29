#ifndef ENGINEER_H
#define ENGINEER_H

#include "person.h"

class Engineer: public Person{
    friend std::ostream& operator<<(std::ostream& , const Engineer& operand);

    public:
        Engineer();
        Engineer(std::string_view fullName, int age, 
        std::string_view address, int contract_count); //Construtor 
        ~Engineer();

        void build_something(){
            m_full_name = "Albert Santos";
            m_age = 23;
        }

        int get_contract_count() const{
            return contract_count;
        }

    private:
        int contract_count{0};
};


#endif // ENGINEER_H