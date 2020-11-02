#include <iostream>
#include <SFML/Window.hpp>
#include <SFML/Graphics.hpp>
#include <SFML/Graphics/Sprite.hpp>

struct res
{
    unsigned int x;
    unsigned int y;
};

void lockScreen(res screen)
{
    sf::RenderWindow window(sf::VideoMode(screen.x, screen.y), "grzeLock");

    sf::Texture background;
    if (!background.loadFromFile("background.png"))
    {
        // on failure create black image
        background.create(screen.x, screen.y);
    }

    sf::Sprite backgroundSprite;
    backgroundSprite.setTexture(background);

    sf::Vector2u WindowSize = window.getSize();             //Get size of window.

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
        }

        // draw stuff
        // calculate scale
        sf::Vector2u TextureSize = background.getSize(); //Get size of texture.

        float ScaleX = (float) WindowSize.x / TextureSize.x;
        float ScaleY = (float) WindowSize.y / TextureSize.y;     //Calculate scale.
        backgroundSprite.setScale(sf::Vector2f(ScaleX, ScaleY));
        window.draw(backgroundSprite);
        window.display();
    }
}