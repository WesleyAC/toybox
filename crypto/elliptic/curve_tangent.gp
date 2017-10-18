set view 0,0
set isosample 500,500
set contour base
set cntrparam levels discrete 0
unset surface
set grid
unset key
unset ztics
set xlabel ''
set ylabel ''

curve(x,y) = x**3 + -5*x + 9 - y**2
line(x,y) = (-0.188762*x)+3.42127 - y

set label at -1.1, 3.65, 0 " A" point pointtype 7 pointsize 1
set label at 2.23, 3.0, 0 " C" point pointtype 7 pointsize 1
set label at 2.23, -3.0, 0 " -C" point pointtype 7 pointsize 1

splot [-5:5][-5:5] curve(x,y), line(x,y)

pause -1
