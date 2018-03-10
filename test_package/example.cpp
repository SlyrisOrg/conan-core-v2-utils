#include <iostream>
#include <core/utils/Utils.hpp>

ENUM(Lol,
     Salut)

int main() {
    std::cout << Lol::Salut << std::endl;
    return 0;
}
