#include <iostream>
#include "shape.h"
#include <memory>
#include "oval.h"
#include "circle.h"

void draw_shape(Shape* s){
    s->draw();
}

void draw_shape_v1(const Shape& s_r){
    s_r.draw();
}

int main() {
    Shape shape1("Shape1");
    //shape1.draw();

    Oval oval1(2.0,3.5,"Oval1");
    //oval1.draw();

    Circle circle1(3.3,"Circle1");
    //circle1.draw();



    // Shapes stored in collections
    Shape* shape_collection[]{&shape1, &oval1, &circle1};

    for (Shape* s_ptr: shape_collection){
        s_ptr->draw();
    }

   
    return 0;
}