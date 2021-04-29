def add_time(start, duration, d=""):
    def T_time(start1):
        t = start1.split(" ")[0]
        a = start1.split(" ")[1]
        t = t.split(":")[0] + t.split(":")[1]
        return [t, a]

    def convertn(t, a):
        if (a == "AM"):
            if (t == "1200"):
                t = "000"
            if (int(t) < 1000):
                t = "0" + t
        else:
            if (t == "1200"):
                t = "000"
            t = str(int(t) + 1200)
        return t


    def dur(t, duration):
        d = duration.split(":")[0]
        k = duration.split(":")[1]
        h = int(t[:2]) + int(d)
        m = int(t[2:]) + int(k)
        ct = 0

        hr = 0


        if (m >= 60):
            if (m == 60):
                hr = 1
            hr = int(m / 60)
            m = m % 60
        if (hr > 0):
            h = (h + hr)
        if (h >= 24):
            if (h == 24):
                ct = 1
            ct = int(h / 24)
            h = h % 24

        return [h, m, ct]


    def convertq(t):
        if (int(t) >= 1200):

            k = int(t[:2]) % 12
            if (k == 0):
                return t[:2] + ":" + t[2:] + " PM"
            else:
                return str(k) + ":" + t[2:] + " PM"
        else:
            if (t[:2] == "00"):
                t = "12"+t[2:]
                return t[:2] + ":" + t[2:] + " AM"
            else:
                k = int(t[:2]) % 12
                return str(k) + ":" + t[2:] + " AM"


    dys = {
        "Sunday": 0,
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6
    }
    sy = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    if (d == ""):
        t1 = T_time(start)
        t2 = convertn(t1[0], t1[1])
        dd = dur(t2, duration)
        if int(dd[0]) < 10 and int(dd[1]) < 10:

            t3 = "0" + str(dd[0]) + "0" + str(dd[1])
        elif (int(dd[0]) < 10):
            t3 = "0" + str(dd[0]) + str(dd[1])
        elif (int(dd[1]) < 10):
            t3 = str(dd[0]) + "0" + str(dd[1])
        else:
            t3 = str(dd[0]) + str(dd[1])
        if dd[2] == 0:
            return convertq(t3)
        if dd[2] == 1:
            return convertq(t3) + " (next day)"
        return convertq(t3) + " (" + str(dd[2]) + " days later)"
    else:
        t1 = T_time(start)
        t2 = convertn(t1[0], t1[1])
        dd = dur(t2, duration)
        if int(dd[0]) < 10 and int(dd[1])<10:

            t3 = "0" + str(dd[0]) +"0"+ str(dd[1])
        elif(int(dd[0]) < 10):
            t3 = "0" + str(dd[0])  + str(dd[1])
        elif(int(dd[1]) < 10):
            t3 =  str(dd[0])+"0"+ str(dd[1])
        else:
            t3 = str(dd[0]) + str(dd[1])
        if dd[2] == 0:
            return convertq(t3) + ", " + d.capitalize()
        if dd[2] == 1:
            return convertq(t3) + ", " + sy[(dys[d.capitalize()] + dd[2]) % 7] + " (next day)"
        return convertq(t3) + ", " + sy[(dys[d.capitalize()] + dd[2]) % 7] + " (" + str(dd[2]) + " days later)"
