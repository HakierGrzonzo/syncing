#include <SFML/Graphics/Color.hpp>
#include <SFML/Window/WindowStyle.hpp>
#include <iostream>
#include <SFML/Window.hpp>
#include <SFML/Graphics.hpp>
#include <SFML/Graphics/Sprite.hpp>
#include <time.h>
#include <stdio.h>

struct res
{
    unsigned int x;
    unsigned int y;
};

// Get current date/time, format is HH:MM
const std::string currentDateTime() {
    time_t     now = time(0);
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    // Visit http://en.cppreference.com/w/cpp/chrono/c/strftime
    // for more information about date/time format
    strftime(buf, sizeof(buf), "%H:%M", &tstruct);

    return buf;
}

void lockScreen(res screen)
{
    sf::ContextSettings settings;
    settings.antialiasingLevel = 2;

    sf::RenderWindow window(sf::VideoMode(screen.x, screen.y), "grzeLock", sf::Style::Close | sf::Style::Fullscreen, settings);
    window.setVerticalSyncEnabled(true);
    
    // Handle background

    sf::Texture background;
    if (!background.loadFromFile("background.png"))
    {
        // on failure create something
        background.create(screen.x, screen.y);
    }
    background.setSmooth(true);

    sf::RectangleShape backgroundShape(sf::Vector2f(screen.x, screen.y));
    backgroundShape.setTexture(&background);


    // handle clock font

    sf::Font clockFont;
    if (!clockFont.loadFromFile("futura light bt.ttf"))
    {
        std::cout << "I can not proceed without clock font, Exiting!" << std::endl;
        return;
    }

    sf::Text clock;
    clock.setFont(clockFont);
    clock.setCharacterSize(100);
    clock.setOrigin(sf::Vector2f(1, 0));
    clock.setPosition(sf::Vector2f((float) 0.1 * screen.x, (float) 0.8 * screen.y ));
    clock.setFillColor(sf::Color::White);

    std::string time = "";

    while (window.isOpen())
    {
        sf::Event event;
        if (window.pollEvent(event))
        {
            if (event.type == sf::Event::EventType::Closed)
            {
                window.close();
                std::cout << "Closing window, goodbye!" << std::endl;
                break;
            }
            else if (event.type == sf::Event::EventType::Resized)
            {
                auto windowSize = window.getSize();
                //backgroundShape.setSize(sf::Vector2f((float) windowSize.x, (float) windowSize.y));
                std::cout << "Resized Now to " << windowSize.x << "x" << windowSize.y << std::endl;
            }
        }
        std::string newTime = currentDateTime();
        if (time != newTime)
        {
            time = newTime;
            clock.setString(time);
        }
        window.clear(); 
        // draw stuff
        // Draw Background sprite
        window.draw(backgroundShape);
        window.draw(clock);
        window.display();
    }
}