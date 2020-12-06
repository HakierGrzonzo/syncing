rgbwal: main.o color.o blender.o
	g++ blender.o main.o color.o -o rgbwal

main.o: main.cpp
	g++ -c main.cpp

color.o: color.cpp
	g++ -c color.cpp

blender.o: blender.cpp
	g++ -c blender.cpp

run: rgbwal
	./rgbwal

clean:
	rm *.o rgbwal

install: rgbwal
	cp rgbwal /usr/bin/