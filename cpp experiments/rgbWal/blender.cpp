#include <string>
#include <vector>
#include "color.h"
#include <iomanip>
#include <thread>
#include <fstream>
#include <iostream>
#include <cmath>
void blend (std::vector<Color> colors)
{
    const int steps = 32;
    std::ofstream ckbfile;
    while(true)
    {
        for (int i = 0; i < colors.size(); i++)
        {   
            int previous_index = i == 0 ? colors.size() - 1 : i -1;
            Color previous = colors[i == 0 ? colors.size() - 1 : i -1];
            Color next = colors[i];
            for (int y = 0; y < steps; y++)
            {
                double factor = ((double) y) / steps;
                RGB color = previous.lerp(next, factor).getRGB();
                ckbfile.open("/tmp/ckbpipe000");
                ckbfile << "rgb ";
                ckbfile << std::setfill('0') << std::setw(6) << std::hex << rgb2int(color);
                ckbfile << "ff"; // provide alpha
                ckbfile.close();
                std::cerr << round(color.r) << ' ' << round(color.g) << ' ' << round(color.b);
                std::cerr << ' ' << previous_index << ' ' << i << ' ' << factor << std::endl;
                std::this_thread::sleep_for(std::chrono::milliseconds(50));
            }
        }
    }
}