Xo = float(input('Please enter Initial Position: '))
Vo = float(input('Please enter Initial Acceleration: '))
a = float(input('Please enter Velocity: '))
t = float(input('Please enter Time: '))
print('xf = ', (Xo), ' + ', (Vo), ' * ', (t), ' + ', (.5), ' * ', (a), ' * ', (t), ' * ', (t))
total = Xo + Vo * t + .5 * a * t * t
print('xf = ', total)
