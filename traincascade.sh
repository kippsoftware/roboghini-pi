#/bin/bash
rm -f stopsign/*.xml

opencv_traincascade \
    -data stopsign \
    -vec stopsign/stopsign.vec \
    -bg negative/negative.txt \
    -featureType HAAR \
    -precalcValBufSize 2048 \
    -precalcIdxBufSize 2048 \
    -minHitRate 0.995 \
    -numPos 20 \
    -numNeg 400 \
    -numStages 20 \
    -w 20 \
    -h 20
