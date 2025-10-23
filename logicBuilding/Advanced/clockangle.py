def getMin(x, y):
    return x if x < y else y


def getClockAngle(t) -> str:
    h = int(t[:2])
    m = int(t[-2:])  
    
    h = h % 12
    
    hr_angle = h * 0.5 * 60
    min_angle = m * 6
    angle_diff = abs(hr_angle - min_angle)
    return getMin((360 - angle_diff), angle_diff)


print(getClockAngle("06:00"))