#include <exception>
#include <stdexcept>
#include<string>
#include<cmath>
#include<iostream>

struct YUV {
    double y, u, v;
};

struct RGB {
    double r, g, b;
};
class Color {
    public:
        RGB getRGB();
        YUV getYUV();
        Color (YUV color);
        Color (RGB color);
        Color lerp(Color target, double factor);
        Color operator+(Color b);
        Color operator-(Color b);
    private:
        YUV _color;
};

RGB Color::getRGB()
{
    RGB res;
    res.r = _color.y + 1.140 * _color.v;
    res.g = _color.y - 0.395 * _color.u - 0.581 * _color.v;
    res.b = _color.y + 2.032 * _color.u;
    return res;
}

YUV Color::getYUV()
{
    return _color;
}

Color::Color (YUV color)
{
    _color = color;
}

Color::Color (RGB color)
{
    _color.y = 0.299 * color.r + 0.587 * color.g + 0.114 * color.b;
    _color.u = 0.492 * (color.b - _color.y);
    _color.v = 0.877 * (color.r - _color.y);
}

Color Color::operator+(Color b)
{
    YUV yuv = b.getYUV();
    yuv.y += _color.y;
    yuv.u += _color.u;
    yuv.v += _color.v;
    return Color(yuv);
}

Color Color::operator-(Color b)
{
    YUV yuv = b.getYUV();
    yuv.y -= _color.y;
    yuv.u -= _color.u;
    yuv.v -= _color.v;
    YUV fin {- yuv.y, -yuv.u, -yuv.v};
    return Color(fin);
}

Color Color::lerp(Color target, double factor)
{
    if (factor < 0 || factor > 1)
    {
        throw std::invalid_argument("factor must be beetween 0 and 1");
    }
    YUV b = _color;
    YUV a = (target - *this).getYUV();
    YUV res;
    res.y = b.y + factor * a.y;
    res.u = b.u + factor * a.u;
    res.v = b.v + factor * a.v;
    return Color(res);
}

RGB int2rgb(int x)
{
    RGB res;
    res.b = x % 256;
    x = x >> 8;
    res.g = x % 256;
    x = x >> 8;
    res.r = x;
    return res;
}

int rgb2int(RGB color)
{
    double r = abs(round(color.r));
    double g = abs(round(color.g));
    double b = abs(round(color.b));

    if (g > 255 || r > 255 || b > 255 || r < 0 || g < 0 || b < 0)
    {
        throw std::invalid_argument("Color is not 24bit!");
    }
    return (int) 256 * 256 * r + 256 * g + b;
}