def title(hour,minute,second,millsec,offset):
    total = (hour * 3600 + minute*60 + second ) * 1000 + millsec + offset
    h = total/3600000
    reminder = total%3600000
    m = reminder/60000
    reminder = reminder%60000
    s = reminder/1000
    off = reminder%1000
    return "[{:02}:{:02}:{:02},{:03}]".format(h,m,s,off)
