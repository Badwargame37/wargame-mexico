#include <iostream>
#include <string>
#include <cstdlib>

void executeCommand(const std::string& command) {
    system(command.c_str());
}

int main() {
    std::string input;
    while (true) {
        std::cout << "rbash$ ";
        std::getline(std::cin, input);

        if (input == "get-ip") {
            executeCommand("hostname -I");
        } 
        else if (input.substr(0, 14) == "chisel") {
            std::string chiselArgs = input.substr(15);
            executeCommand("/opt/chisel " + chiselArgs);
        } 
        else if (input == "help") {
            std::cout << "Available commands:" << std::endl;
            std::cout << "commande get-ip -> Get the IP" << std::endl;
            std::cout << "commande chisel -> Execute /opt/chisel with arguments" << std::endl;
            std::cout << "help -> Show help" << std::endl;
            std::cout << "exit -> Exit rbash" << std::endl;
        } 
        else if (input == "exit") {
            break;
        } 
        else {
            std::cout << "Unknown command. Type 'help' for a list of available commands." << std::endl;
        }
    }
    return 0;
}
