#include <iostream>
#include <string>
#include <vector>
#include <thread>
#include "color.h"
#include "blender.h"

int decodeHexColor(std::string s)
{
    int res;
    if (s.size() != 6 && s.size() != 7 && s[0] != '#')
    {
        throw std::invalid_argument("Bad hex value");
    }
    int start = 0;
    if (s.size() == 7 && s[0] == '#') start = 1;
    for (int i = start; i < s.size(); i++)
    {
        res *= 16;
        char c = s[i];
        if (c >= '0' && c <= '9')
        {
            res += c - '0';
        }
        else if (c >= 'a' && c <= 'f')
        {
            res += c - 'a' + 10;
        }
        else if (c >= 'A' && c <= 'F')
        {
            res += c - 'A' + 10;
        }
        else
        {
            throw std::invalid_argument("Bad hex value");
        }
    }
    return res;
}

int main(int argc, char** argv)
{
    if (argc < 2)
    {
        std::cerr << "Not enough colors to blend!" << std::endl;
        return 1;
    }
    std::vector<Color> colors;
    try 
    {
        for (int i = 1; i < argc; i++)
        {
            std::string arg = std::string(argv[i]);
            Color color = Color(RGB(int2rgb(decodeHexColor(arg))));
            colors.push_back(color);
        }
    }
    catch (std::invalid_argument e)
    {
        std::cerr << "Bad arguments!" << std::endl << "Arguments must be 24bit rgb values in hex with no prefixes!" << std::endl;
        return 1;
    }
    blend(colors);
    return 0;
}
