#include<iostream>
#include <SFML/Window/Joystick.hpp>
#include <SFML/Window.hpp>
#include <SFML/Graphics.hpp>

int main(int argc, char **argv){
    sf::RenderWindow window(sf::VideoMode(300, 200), "plswrk");
    while (window.isOpen()){
        sf::Event event;
        if (window.pollEvent(event)){
            if (event.type == sf::Event::EventType::Closed){
                window.close();
                break;
            }
            else if (event.type == sf::Event::EventType::JoystickMoved){
                std::cout << "joy: " << event.joystickMove.axis << ":" << event.joystickMove.position / 2 + 50 << std::endl;
            }
        }

        window.clear(sf::Color::Black);
        window.display();
    }
}