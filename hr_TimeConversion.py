def timeConversion(s):
    t = s.split(':')
    if s[-2:] == 'PM':
        if t[0] != '12':
            t[0] = str(int(t[0]) + 12)
        else:
            t[0] = '12'
    else:
        if t[0] == '12':
            t[0] = '00'
    newtime = ':'.join(t)
    return str(newtime[:-2])


if __name__ == '__main__':
    s = '12:24:54PM'
    print('12:24:54PM')
    print(timeConversion(s))