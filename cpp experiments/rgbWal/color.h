# pragma once
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

RGB int2rgb(int x);
int rgb2int(RGB color);