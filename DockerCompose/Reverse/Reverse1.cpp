#include <iostream>
#include <string>

int main() {
    std::string user_input;
    std::cout << "Entrez le mot de passe : ";
    std::cin >> user_input;

    if (user_input == "Arthur_mange_des_pouples") {
        std::cout << "Bravo, vous avez trouvé le mot de passe !" << std::endl;
    } else {
        std::cout << "Désolé, essayez à nouveau." << std::endl;
    }

    return 0;
}
