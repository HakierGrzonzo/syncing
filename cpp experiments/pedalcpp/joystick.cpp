#include <vector>
#include <SFML/Window/Joystick.hpp>

struct joystick_state {
    std::vector<signed short> button;
    std::vector<signed short> axis;
};