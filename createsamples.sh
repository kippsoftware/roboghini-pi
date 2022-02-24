#/bin/bash
opencv_createsamples \
    -vec stopsign/stopsign.vec \
    -num 20 \
    -info stopsign/stopsign.txt \
    -bg negative/negative.txt \
    -w 20 \
    -h 20
