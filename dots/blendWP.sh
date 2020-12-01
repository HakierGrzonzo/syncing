#!/usr/bin/bash
WALLPAPER="$HOME/Pictures/wallpaper.png"
WRKDIR="/tmp/blendWD"
STEP=10
mkdir $WRKDIR
convert $1 -resize 1920x1080 ${WRKDIR}/one.bmp
convert $WALLPAPER -resize 1920x1080 ${WRKDIR}/two.bmp
for ((i=$STEP; i < 100; i += $STEP)); do
    composite -blend $i -gravity center ${WRKDIR}/one.bmp ${WRKDIR}/two.bmp "${WRKDIR}/${i}.bmp"
done
echo "Done processing"
for ((i=$STEP; i < 100; i += $STEP)); do
    hsetroot -cover "${WRKDIR}/${i}.bmp"
done
hsetroot -cover $1
rm -r $WRKDIR

