#include <iostream>
#include <fstream>

int main()
{
    int16_t x= 0;
    int i = 0;
    std::ifstream source("/dev/random", std::ios_base::binary);
    while (source)
    {
        char buffer[sizeof(int16_t)];
        source.read(buffer, sizeof(int16_t));
        int16_t* ptr = reinterpret_cast<int16_t*>(buffer);
        x = *ptr;
        //std::cout << x << std::endl;
        if (x == 10)
        {
            std::cout << "Found 10 after " << i << " attempts";
            break;
        }
        i++;
    }
}