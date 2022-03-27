// Verifica se constants.h não foi definido.
// Senão foi, ele então é definido.
// Essa verificação evita que o mesmo código seja declarado mais de uma vez no main.
// Ou seja, evita que aconteça include mais de uma vez.
#ifndef CONSTANTS_H
#define CONSTANTS_H

const double PI {3.14159265};

#endif