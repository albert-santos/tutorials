#include <iostream>

const double PI{3.14159265};

class Cylinder {
    public:

        // Constructor
        Cylinder() {
            base_radius = 2.0;
            height = 2.0;
        }

        Cylinder(double rad_param, double height_param){
            base_radius = rad_param;
            height = height_param;
        }

        // Métodos (Funções)
        double volume() {
            return PI * base_radius * base_radius * height;
        }

    private:
        // Member variables
        double base_radius{1};
        double height{1};
};

int main()
{   

    Cylinder cylinder1(10, 4); // Objeto instanciado a partir da classe
    std::cout << "volume: " << cylinder1.volume() << std::endl;
    
    // std::cout << "base_radius: " << cylinder1.base_radius << std::endl;
    // std::cout << "height: " << cylinder1.height << std::endl;
    return 0;
}