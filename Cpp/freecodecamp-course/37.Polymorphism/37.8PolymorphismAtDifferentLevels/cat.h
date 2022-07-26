#ifndef CAT_H
#define CAT_H

#include "feline.h"

class Cat: public Feline
{
    Cat() = default;
    Cat(std::string_view fur_style, std::string_view description);
    virtual ~Cat();

    virtual void miaw() const {
        std::cout << "Cat::miaw() called for: " << m_description << std::endl;
    }

    virtual void breathe() const {
        std::cout << "Cat::breathe called for: " << m_description <<std::endl;
    }

    virtual void run() const {
        std::cout << "Cat " << m_description << " is running" << std::endl;
    }
};



#endif // CAT_H

