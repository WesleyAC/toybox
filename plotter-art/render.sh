#!/bin/sh
while [ 1 ]
do
sleep 1 &&
python $1 > /tmp/out.hpgl &&
~/code/plotter-tools/viz/target/debug/viz /tmp/out.hpgl > /tmp/out_tmp.html &&
mv /tmp/out_tmp.html /tmp/out.html
done
