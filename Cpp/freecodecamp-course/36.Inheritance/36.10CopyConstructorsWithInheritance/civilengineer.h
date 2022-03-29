#ifndef CIVIL_ENGINEER_H
#define CIVIL_ENGINEER_H

#include "engineer.h"

class CivilEngineer: public Engineer{
    friend std::ostream& operator<<(std::ostream&, const CivilEngineer& operand);

    public:
        CivilEngineer();//Construtor padrão
        CivilEngineer(std::string_view fullName, int age, 
        std::string_view address, int contract_count, std::string_view speciality); //Construtor 
        CivilEngineer(const CivilEngineer& source);
        ~CivilEngineer(); //Deconstructor

        void build_road(){
            
            add(10,2);
            add(10,2,4);
        }


    private:
        std::string m_speciality{"None"};
};


#endif // CIVIL_ENGINEER_H