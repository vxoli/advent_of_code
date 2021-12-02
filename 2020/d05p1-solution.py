f = open('d05-input.txt', 'r')
data = f.readlines()

maxseatid=0

for line in data:
    row_code = line[:7]
    seat_code= line[7:]
    seatrow = []
    seatid = 0
    for s in range(0,128,1):
        seatrow.append(s)
    for s in row_code:
        if s == "F":
            seatrow = seatrow[:int(len(seatrow)/2)]
        else:
            seatrow = seatrow[int(len(seatrow)/2):]
    seatnum = []
    for s in range(0,8,1):
        seatnum.append(s)
    for s in seat_code:
        if s == "L":
            seatnum = seatnum[:int(len(seatnum)/2)]
        else:
            seatnum = seatnum[int(len(seatnum)/2):]
    seatid = seatrow[0] * 8 + seatnum[0]
    maxseatid = (seatid * (seatid > maxseatid)) + (maxseatid * (seatid <= maxseatid))
    print(seatrow,seatnum, seatid, maxseatid)
