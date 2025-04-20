#include <iostream>

//lambda¥Ú”°

int main() {
    [] {
        const auto print = [](auto&&... args) {
            (std::cout << ... << args);
            };
        print("Hello", " ", "World!\n");
        }();
}
