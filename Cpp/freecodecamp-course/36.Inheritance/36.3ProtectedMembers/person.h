#ifndef PERSON_H
#define PERSON_H

#include <string>
#include <iostream>
#include <string_view>

class Person{
    friend std::ostream& operator<<(std::ostream& out, const Person& person);

    public:
        Person();
        Person(std::string& first_name_param, std::string& last_name_param);
        ~Person(); // Destructor

        //Getters
        std::string get_first_name() const{
            return m_first_name;
        }

        std::string get_last_name() const {
            return m_last_name;
        }

        //Setters
        void set_first_name(std::string_view first_name_param) {
            m_first_name = first_name_param;
        }

        void set_last_name(std::string_view last_name_param){
            m_last_name = last_name_param;
        }

    protected:
        std::string m_first_name{"Mysterio"};
        std::string m_last_name{"Person"};
};



#endif // PERSON_H