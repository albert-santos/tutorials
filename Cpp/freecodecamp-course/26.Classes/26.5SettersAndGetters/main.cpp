#include <iostream>

const double PI{3.14159265};

class Cylinder {
    public:
        //Constructors
        Cylinder() = default;
        Cylinder (double rad_param, double height_param){
            base_radius = rad_param;
            height = height_param;
        }

        //Funções ou métodos da classe
        double volume(){
            return base_radius * base_radius * PI * height;
        }

        //Métodos getter
        double get_base_radius(){
            return base_radius;
        }
        double get_height(){
            return height;
        }


        //Métodos setter
        void set_base_radius(double rad_param){
            base_radius = rad_param;
        }

        void set_height(double height_param){
            height = height_param;
        }

    private:
        double base_radius{1};
        double height{1};
};

int main()
{   

    Cylinder cylinder1(10,10); // Objeto instanciado a partir da classe
    std::cout << "volume: " << cylinder1.volume() << std::endl;
    
    std::cout << "base_radius: " << cylinder1.get_base_radius() << std::endl;
    std::cout << "height: " << cylinder1.get_height() << std::endl;

    //Modificando o objeto
    cylinder1.set_base_radius(100);
    cylinder1.set_height(10);

    std::cout << "volume: " << cylinder1.volume() << std::endl;
    std::cout << "base_radius: " << cylinder1.get_base_radius() << std::endl;
    std::cout << "height: " << cylinder1.get_height() << std::endl;

    return 0;
}