import serial
import data
import os
import json,re
#I see you got curious, eh?
#Dont be too overwhelmed
#Call 4408797036 if you have any
#questions

#Sport       Added  Works       Board #
#Baseball    X      X           34
#Basketball  X      X           06
#Football    X      X           00 or 23?
#Hockey      X      X           00
#Lacrosse    X      NO          21?
#Soccer      X                  21
#Volleyball  X      X           06 or 00
#Wrestling   X      X           06 or 00

ui = "ONE MOMENT... CONNECTING"
discordtxt2 = " "
ui2 = "eeee"
bbstath = 0
hpstats2 = " "
vpstats2 = " "
bbvstat = 0
uivar = " "
sport = " "
time2 = " "
names2 = " "
scores2 = " "
per2 =" "
ts2 = "0"
txttime2 = " "
line12 =" "
line22 =" "
line32 =" "
line42 =" "
timer2 = " "
hscore = " "
vscore = " "
hname = " "
vname = " "
min = "  "
sec = "  "
ts = " "
per = " "
line1 = "  "
line2 = line1
line3 = line1
line4 = line1
timer = "  "
hinn = 0
vinn = 0
wrtime = 0
hvdata = 0
vvdata = 0
bbhome = 0
bbvis = 0
idle = 15
cPack = 0
lastPack = "0"
twoLastPack = "0"
threeLastPack = "0"
blank=" "
emptyline = "                        "
credits = "Made by JumpShot Interactive, SPCcleveland9035,\nand Aaron S\n\nFairPlay AllSport MP70\n"

os.system('clear')
print(credits)
config = json.load(open("config.json"))
txt = config.get("UniText", "Y")
hBonusVal = config.get("hBonus", "<")
hDBonusVal = config.get("hDBonus", "<<")
vBonusVal = config.get("vBonus", ">")
vDBonusVal = config.get("vDBonus", ">>")
hPossVal = config.get("hPoss", "<")
vPossVal = config.get("vPoss", ">")
sportspecific = config.get("SportText", "N")
uistatyn = config.get("UIStats", "N")
uitimeryn = config.get("UITimer", "N")
control = config.get("MP70or80", 70)
hrost = config.get("HRoster", "")
percust = config.get("customPeriod", "N")
if percust == "Y":
    blankPCust = config.get(" P", " ")
    ZeroPCust = config.get("0P", "0th")
    OnePCust = config.get("1P", "1st")
    TwoPCust = config.get("2P", "2nd")
    ThreePCust = config.get("3P", "3rd")
    FourPCust = config.get("4P", "4th")
    FivePCust = config.get("5P", "5th")
    SixPCust = config.get("6P", "6th")
    SevenPCust = config.get("7P", "7th")
    EightPCust = config.get("8P", "8th")
    NinePCust = config.get("9P", "9th")
vrost =  config.get("VRoster", "")
nohname = config.get("HName", "")
txt10ths = config.get("txt10ths", "N")
zeros = config.get("00or0", "0")
novname = config.get("VName", "")
stream = config.get("Stream", "N")
port = config.get("Port", "COM6")
baud = config.get("Baud", 9600)
spaces = config.get("txtRmvSpaces", "N")
hksaves = config.get("HKSaves", "Y")
intClock = config.get("intClock", "N")
basicDir = config.get("basicDir", "./")
uniDir = config.get("universalDir", "./uni")
fbDir = config.get("footballDir", "./sport/FB")
baDir = config.get("baseballDir", "./sport/BA")
bbDir = config.get("basketballDir", "./sport/BB")
scDir = config.get("soccerDir", "./sport/SC")
laDir = config.get("lacrosseDir", "./sport/LA")
hkDir = config.get("hockeyDir", "./sport/HK")
wrDir = config.get("wrestlingDir", "./sport/WR")
vbDir = config.get("volleyballDir", "./sport/VB")
if spaces == "Y" or spaces == "y" or spaces == "yES" or spaces == "yes" or spaces == "YES" or spaces == "Yes":
    spaces = 1
else:
    spaces = 0
if percust == "Y" or percust == "y" or percust == "yES" or percust == "yes" or percust == "YES" or percust == "Yes":
    percust = 1
else:
    percust = 0
if hksaves == "Y" or hksaves == "y" or hksaves == "yES" or hksaves == "yes" or hksaves == "YES" or hksaves == "Yes":
    hksaves = 1
else:
    hksaves = 0
if txt10ths == "Y" or txt10ths == "y" or txt10ths == "yES" or txt10ths == "yes" or txt10ths == "YES" or txt10ths == "Yes":
    txt10ths = 1
else:
    txt10ths = 0
if txt == "Y" or txt == "y" or txt == "yES" or txt == "yes" or txt == "YES" or txt == "Yes":
    txt = 1
else:
    txt = 0
if sportspecific == "Y" or sportspecific == "y" or sportspecific == "yES" or sportspecific == "yes" or sportspecific == "YES" or sportspecific == "Yes":
    sportspecific = 1
    if hrost == "" or hrost == " ":
        hrost = "home"
    if vrost == "" or vrost == " ":
        vrost = "away"
else:
    sportspecific = 0
if uistatyn == "Y" or uistatyn == "y" or uistatyn == "yES" or uistatyn == "yes" or uistatyn == "YES" or uistatyn == "Yes":
    uistatyn = 1
else:
    uistatyn = 0
if uitimeryn == "Y" or uitimeryn == "y" or uitimeryn == "yES" or uitimeryn == "yes" or uitimeryn == "YES" or uitimeryn == "Yes":
    uitimeryn = 1
else:
    uitimeryn = 0
os.makedirs(basicDir, exist_ok=True)
os.makedirs(uniDir, exist_ok=True)
os.makedirs(baDir, exist_ok=True)
os.makedirs(bbDir, exist_ok=True)
os.makedirs(vbDir, exist_ok=True)
os.makedirs(wrDir, exist_ok=True)
os.makedirs(fbDir, exist_ok=True)
os.makedirs(laDir, exist_ok=True)
os.makedirs(hkDir, exist_ok=True)
os.makedirs(scDir, exist_ok=True)
print(sportspecific)
print(bbDir)
if len(nohname) == 0:
    nohname = "   HOME   "
elif len(nohname) == 1:
    nohname = "     " + nohname + "    "
elif len(nohname) == 2:
    nohname = "    " + nohname + "    "
elif len(nohname) == 3:
    nohname = "    " + nohname + "   "
elif len(nohname) == 4:
    nohname = "   " + nohname + "   "
elif len(nohname) == 5:
    nohname = "   " + nohname + "  "
elif len(nohname) == 6:
    nohname = "  " + nohname + "  "
elif len(nohname) == 7:
    nohname = "  " + nohname + " "
elif len(nohname) == 8:
    nohname = " " + nohname + " "
elif len(nohname) == 9:
    nohname = " " + nohname
elif len(nohname) == 10:
    nohname = nohname
else:
    nohname = "   HOME   "


if len(novname) == 0:
    novname = "  VISITOR "
elif len(novname) == 1:
    novname = "     " + novname + "    "
elif len(novname) == 2:
    novname = "    " + novname + "    "
elif len(novname) == 3:
    novname = "    " + novname + "   "
elif len(novname) == 4:
    novname = "   " + novname + "   "
elif len(novname) == 5:
    novname = "   " + novname + "  "
elif len(novname) == 6:
    novname = "  " + novname + "  "
elif len(novname) == 7:
    novname = "  " + novname + " "
elif len(novname) == 8:
    novname = " " + novname + " "
elif len(novname) == 9:
    novname = " " + novname
elif len(novname) == 10:
    novname = novname
else:
    novname = "  VISITOR "
os.system('clear')
serstart = 0
while serstart != 1:
    try:
        ser = serial.Serial(port, baud)
        serstart = 1
    except:
        os.system('clear')
        print(f"No Connections, verify settings and try again\n{port}, {baud}")

error = 1
while True:
    try:
        sta = ser.read(1)
        idle = 0
        if post == 1:
            os.system('clear')
            print(uivar)
        if post == 2:
            post = post - 1
        if sta == b'\x02':
            # read the next byte to check for 'H' or 'C'
            data = ser.read(1)
            # If format type H
            if data == b'H':
                hname = ser.read(10).decode('utf-8')
                hscore = ser.read(2).decode('utf-8')
                hsog = ser.read(2).decode('utf-8')
                hp1no = ser.read(2).decode('utf-8')
                hp1min = ser.read(2).decode('utf-8')
                hp1sec = ser.read(2).decode('utf-8')
                hp2no = ser.read(2).decode('utf-8')
                hp2min = ser.read(2).decode('utf-8')
                hp2sec = ser.read(2).decode('utf-8')
                if control == 80:
                    temp = ser.read(1)
                vname = ser.read(10).decode('utf-8')
                vscore = ser.read(2).decode('utf-8')
                vsog = ser.read(2).decode('utf-8')
                vp1no = ser.read(2).decode('utf-8')
                vp1min = ser.read(2).decode('utf-8')
                vp1sec = ser.read(2).decode('utf-8')
                vp2no = ser.read(2).decode('utf-8')
                vp2min = ser.read(2).decode('utf-8')
                vp2sec = ser.read(2).decode('utf-8')
                if control == 80:
                    if vp1min == "  " and vp1sec != "  ":
                        vp1min = " 0"
                        if len(vp1sec) == 2:
                            if vp1sec[0] == ' ':
                                vp1sec = vp1sec[1:]
                                vp1sec = "0" + vp1sec
                    if hp2min == "  " and hp2sec != "  ":
                        hp2min = " 0"
                        if len(hp2sec) == 2:
                            if hp2sec[0] == ' ':
                                hp2sec = hp2sec[1:]
                                hp2sec = "0" + hp2sec
                    if vp2min == "  " and vp2sec != "  ":
                        vp2min = " 0"
                        if len(vp2sec) == 2:
                            if vp2sec[0] == ' ':
                                vp2sec = vp2sec[1:]
                                vp2sec = "0" + vp2sec
                    if hp1min == "  " and hp1sec != "  ":
                        hp1min = " 0"
                        if len(hp1sec) == 2:
                            if hp1sec[0] == ' ':
                                hp1sec = hp1sec[1:]
                                hp1sec = "0" + hp1sec

                line1 = "SOG    PENALTIES     SOG"
                #SOG    PENALTIES     SOG
                #00 88:88 88  88 88:88 00
                #   88:88 88  88 88:88 
                line2 = hsog + " " + hp1min + ":" + hp1sec + " " + hp1no + "  " + vp1no + " " + vp1min + ":" + vp1sec + " " + vsog
                line3 = "   " + hp2min + ":" + hp2sec + " " + hp2no + "  " + vp2no + " " + vp2min + ":" + vp2sec + "   "
                line4 = emptyline
                sport = "HK"
            # If format type C
            if data == b'C':
                min = ser.read(2).decode('utf-8')
                sec = ser.read(2).decode('utf-8')
                ts = ser.read(1).decode('utf-8')
                per = ser.read(1).decode('utf-8')
                timer = ser.read(2).decode('utf-8')
                otherts = ts
                if intClock == "Y":
                    if ts != " ":
                        if lastPack == ts:
                            if twoLastPack != lastPack:
                                temp = int(ts)
                                temp = temp - 1
                                if temp == -1:
                                    if sec == " 0" or sec == "00":
                                        temp = 0
                                    else:
                                        temp = 9
                                ts = str(temp)
                        threeLastPack = twoLastPack
                        twoLastPack = lastPack
                        lastPack = otherts

            if data == b'A':
                temp = ser.read(1).decode('utf-8')
                per = ser.read(1).decode('utf-8')
                b = ser.read(1).decode('utf-8')
                s = ser.read(1).decode('utf-8')
                o = ser.read(1).decode('utf-8')
                tb = ser.read(1).decode('utf-8')
                atbat = ser.read(2).decode('utf-8')
                hiterr = ser.read(2).decode('utf-8')
                sport = "BA"
            if data == b'F':
                hname = ser.read(10).decode('utf-8')
                hscore = ser.read(2).decode('utf-8')
                htol = ser.read(1).decode('utf-8')
                vname = ser.read(10).decode('utf-8')
                vscore = ser.read(2).decode('utf-8')
                vtol = ser.read(1).decode('utf-8')
                down = ser.read(1).decode('utf-8')
                togo = ser.read(2).decode('utf-8')
                ballon = ser.read(2).decode('utf-8')
                poss = ser.read(1).decode('utf-8')

                line1 = "TOL DOWN   TOGO   ON TOL"
                line2 = " " + htol + "    " + down + "     " + togo + "    " + ballon + "  " + vtol + " "
                if poss == "H":
                    line3 = "   <   POSSESSION       "
                elif poss == "V":
                    line3 = "       POSSESSION    >  "
                else: 
                    line3 = "       POSSESSION       "
                #T   DOWN   TOGO   ON   T
                #3     1     10    50   3
                #   <   POSSESSION    >   
                #
                sport = "FB"
            if data == b'S':
                secdata = ser.read(1)
                if secdata == b'H':
                    hp1no = ser.read(2).decode('utf-8')
                    hp1fls = ser.read(1).decode('utf-8')
                    hp1pts = ser.read(2).decode('utf-8')
                    hp2no = ser.read(2).decode('utf-8')
                    hp2fls = ser.read(1).decode('utf-8')
                    hp2pts = ser.read(2).decode('utf-8')
                    hp3no = ser.read(2).decode('utf-8')
                    hp3fls = ser.read(1).decode('utf-8')
                    hp3pts = ser.read(2).decode('utf-8')
                    hp4no = ser.read(2).decode('utf-8')
                    hp4fls = ser.read(1).decode('utf-8')
                    hp4pts = ser.read(2).decode('utf-8')
                    hp5no = ser.read(2).decode('utf-8')
                    hp5fls = ser.read(1).decode('utf-8')
                    hp5pts = ser.read(2).decode('utf-8')

                    hpstats = hp1no+hp2no+hp3no+hp4no+hp5no+hp1fls+hp2fls+hp3fls+hp4fls+hp5fls+hp1pts+hp2pts+hp3pts+hp4pts+hp5pts
                    if hpstats != hpstats2 and sportspecific == 1:
                        sstxt = 1
                        hpstats2=hpstats
                    bbstath = 1
                if secdata == b'V':
                    vp1no = ser.read(2).decode('utf-8')
                    vp1fls = ser.read(1).decode('utf-8')
                    vp1pts = ser.read(2).decode('utf-8')
                    vp2no = ser.read(2).decode('utf-8')
                    vp2fls = ser.read(1).decode('utf-8')
                    vp2pts = ser.read(2).decode('utf-8')
                    vp3no = ser.read(2).decode('utf-8')
                    vp3fls = ser.read(1).decode('utf-8')
                    vp3pts = ser.read(2).decode('utf-8')
                    vp4no = ser.read(2).decode('utf-8')
                    vp4fls = ser.read(1).decode('utf-8')
                    vp4pts = ser.read(2).decode('utf-8')
                    vp5no = ser.read(2).decode('utf-8')
                    vp5fls = ser.read(1).decode('utf-8')
                    vp5pts = ser.read(2).decode('utf-8')

                    vpstats = vp1no+vp2no+vp3no+vp4no+vp5no+vp1fls+vp2fls+vp3fls+vp4fls+vp5fls+vp1pts+vp2pts+vp3pts+vp4pts+vp5pts
                    if vpstats != vpstats2 and sportspecific == 1:
                        sstxt = 1
                        vpstats2=vpstats
                    bbvstat = 1
                if bbstath == 1 and bbvstat == 1:
                    try:
                        roster = json.load(open("rosters.json"))
                    except:
                        roster = ""
                    if hp1no == "  ":
                        hp1name = " "
                    else:
                        try:
                            hp1name = roster[hrost][hp1no]
                        except:
                            hp1name = " "
                    if hp2no == "  ":
                        hp2name = " "
                    else:
                        try:
                            hp2name = roster[hrost][hp2no]
                        except:
                            hp2name = " "
                    if hp3no == "  ":
                        hp3name = " "
                    else:
                        try:
                            hp3name = roster[hrost][hp3no]
                        except:
                            hp3name = " "
                    if hp4no == "  ":
                        hp4name = " "
                    else:
                        try:
                            hp4name = roster[hrost][hp4no]
                        except:
                            hp4name = " "
                    if hp5no == "  ":
                        hp5name = " "
                    else:
                        try:
                            hp5name = roster[hrost][hp5no]
                        except:
                            hp5name = " "
                    
                    if vp1no == "  ":
                        vp1name = " "
                    else:
                        try:
                            vp1name = roster[vrost][vp1no]
                        except:
                            vp1name = " "
                    if vp2no == "  ":
                        vp2name = " "
                    else:
                        try:
                            vp2name = roster[vrost][vp2no]
                        except:
                            vp2name = " "
                    if vp3no == "  ":
                        vp3name = " "
                    else:
                        try:
                            vp3name = roster[vrost][vp3no]
                        except:
                            vp3name = " "
                    if vp4no == "  ":
                        vp4name = " "
                    else:
                        try:
                            vp4name = roster[vrost][vp4no]
                        except:
                            vp4name = " "
                    if vp5no == "  ":
                        vp5name = " "
                    else:
                        try:
                            vp5name = roster[vrost][vp5no]
                        except:
                            vp5name = " "
                    sport = "BB"
            if data == b'B':
                secdata = ser.read(1)
                if secdata == b'H':
                    hname = ser.read(10).decode('utf-8')
                    hscore = ser.read(3).decode('utf-8')
                    hfls = ser.read(2).decode('utf-8')
                    htol = ser.read(1).decode('utf-8')
                    hposs = ser.read(1).decode('utf-8')
                    hbns1 = ser.read(1).decode('utf-8')
                    hbns2 = ser.read(1).decode('utf-8')
                    temp = ser.read(1).decode('utf-8')
                    plyr = ser.read(2).decode('utf-8')
                    fls = ser.read(1).decode('utf-8')
                    pts = ser.read(2).decode('utf-8')
                    bbhome = 1
                if secdata == b'V':
                    vname = ser.read(10).decode('utf-8')
                    vscore = ser.read(3).decode('utf-8')
                    vfls = ser.read(2).decode('utf-8')
                    vtol = ser.read(1).decode('utf-8')
                    vposs = ser.read(1).decode('utf-8')
                    vbns1 = ser.read(1).decode('utf-8')
                    vbns2 = ser.read(1).decode('utf-8')
                    temp = ser.read(1).decode('utf-8')
                    plyr = ser.read(2).decode('utf-8')
                    fls = ser.read(1).decode('utf-8')
                    pts = ser.read(2).decode('utf-8')
                    bbvis = 1
                
                line1 = "FLS  T   PLYR F   T  FLS"
                if bbhome == 1 and bbvis == 1:
                    line2 = hfls + "   " + htol + "    " + plyr + "  " + fls + "   " + vtol + "   " + vfls
                    if hbns1 == "1":
                        hbns1e = "<"
                    else:
                        hbns1e = " "

                    if vbns1 == "1":
                        vbns1e = ">"
                    else:
                        vbns1e = " "
                    
                    if hbns2 == "1":
                        hbns2e = "<"
                    else:
                        hbns2e = " "
                    
                    if vbns2 == "1":
                        vbns2e = ">"
                    else:
                        vbns2e = " "
                    
                    if hposs == "1":
                        hposse = "<"
                    else:
                        hposse = " "
                    if vposs == "1":
                        vposse = ">"
                    else:
                        vposse = " "
                    line3 = "      " + hposse + "   POSS   " + vposse + "      "
                    line4 = "     " + hbns1e + hbns2e + "  BONUS   " + vbns2e + vbns1e
                #FLS  T   PLYR F   T  FLS
                #00   0    00  0   0   00
                #      <   POSS   >      
                #     <<  BONUS   >>    
                #123456789012345678901234
                sport = "BB"
            if data == b'R':
                hname = ser.read(10).decode('utf-8')
                hscore = ser.read(2).decode('utf-8')
                hsog = ser.read(2).decode('utf-8')
                hsaves = ser.read(2).decode('utf-8')
                hck = ser.read(2).decode('utf-8')
                vname = ser.read(10).decode('utf-8')
                vscore = ser.read(2).decode('utf-8')
                vsog = ser.read(2).decode('utf-8')
                vsaves = ser.read(2).decode('utf-8')
                vck = ser.read(2).decode('utf-8')
                htol = ser.read(1).decode('utf-8')
                vtol = ser.read(1).decode('utf-8')

                line1 = "SOG SVS C/K  C/K SVS SOG"
                line2 = hsog + "   " + hsaves + "  " + hck + "    " + vck + "  " + vsaves + "   " + vsog
                line3 = emptyline
                line4 = "TOL: " + htol + "            " + vtol + " :TOL"
                #123456789012345678901234
                #SOG SVS C/K  C/K SVS SOG
                #00   00  0    0  00   00
                #
                #TOL: 0            0 :TOL
                sport = "SC"
            if data == b'L':
                hname = ser.read(10).decode('utf-8')
                hscore = ser.read(2).decode('utf-8')
                htol = ser.read(1).decode('utf-8')
                hsog = ser.read(2).decode('utf-8')
                hsaves = ser.read(2).decode('utf-8')
                hp1no = ser.read(2).decode('utf-8')
                hp1min = ser.read(2).decode('utf-8')
                hp1sec = ser.read(2).decode('utf-8')
                hp2no = ser.read(2).decode('utf-8')
                hp2min = ser.read(2).decode('utf-8')
                hp2sec = ser.read(2).decode('utf-8')
                hp3no = ser.read(2).decode('utf-8')
                hp3min = ser.read(2).decode('utf-8')
                hp3sec = ser.read(2).decode('utf-8')
                vname = ser.read(10).decode('utf-8')
                vscore = ser.read(2).decode('utf-8')
                vtol = ser.read(1).decode('utf-8')
                vsog = ser.read(2).decode('utf-8')
                vsaves = ser.read(2).decode('utf-8')
                vp1no = ser.read(2).decode('utf-8')
                vp1min = ser.read(2).decode('utf-8')
                vp1sec = ser.read(2).decode('utf-8')
                vp2no = ser.read(2).decode('utf-8')
                vp2min = ser.read(2).decode('utf-8')
                vp2sec = ser.read(2).decode('utf-8')
                vp3no = ser.read(2).decode('utf-8')
                vp3min = ser.read(2).decode('utf-8')
                vp3sec = ser.read(2).decode('utf-8')
                poss = ser.read(1).decode('utf-8')

                line1 = "NO PNLTY  SHOG  PNLTY NO"
                line2 = hp1no + " " + hp1min + ":" + hp1sec + " " + hsog + "  " + vsog + " " + vp1min + ":" + vp1sec + " " + vp1no
                line3 = hp2no + " " + hp2min + ":" + hp2sec + "  SAVS  " + vp2min + ":" + vp2sec + " " + vp2no
                line4 = hp3no + " " + hp3min + ":" + hp3sec + " " + hsaves + "  " + vsaves + " " + vp3min + ":" + vp3sec + " " + vp3no
                #NO PNLTY  SHOG  PNLTY NO
                #01  2:00 00  00  2:00 02
                #03  2:00  SAVS  10:00 04
                #05  5:00 00  00 15:00 06
                sport = "LA"
            if data == b'V':
                secdata = ser.read(1)
                if secdata == b'H':
                    hname = ser.read(10).decode('utf-8')
                    hscore = ser.read(2).decode('utf-8')
                    hwon = ser.read(1).decode('utf-8')
                    htol = ser.read(1).decode('utf-8')
                    game = ser.read(1).decode('utf-8')
                    hser = ser.read(1).decode('utf-8')
                    hvdata = 1
                    
                if secdata == b'V':
                    vname = ser.read(10).decode('utf-8')
                    vscore = ser.read(2).decode('utf-8')
                    vwon = ser.read(1).decode('utf-8')
                    vtol = ser.read(1).decode('utf-8')
                    game = ser.read(1).decode('utf-8')
                    vser = ser.read(1).decode('utf-8')
                    vvdata = 1

                line1 = "WON  T    GAME    T  WON"
                if hvdata == 1 and vvdata == 1:
                    line2 = " " + hwon + "   " + htol + "      " + game + "     " + vtol + "   " + vwon
                line3 = " "
                line4 = " "
                #WON  T    GAME    T  WON
                # 0   0      0     0   0
                #
                #
                sport = "VB"
            if data == b'W':
                hname = ser.read(10).decode('utf-8')
                if control == 80:
                    hscore = ser.read(2).decode('utf-8')
                    hteamscore = ser.read(2).decode('utf-8')
                else:
                    hteamscore = ser.read(2).decode('utf-8')
                    hscore = ser.read(2).decode('utf-8')
                vname = ser.read(10).decode('utf-8')
                if control == 80:
                    vscore = ser.read(2).decode('utf-8')
                    vteamscore = ser.read(2).decode('utf-8')
                else:
                    vteamscore = ser.read(2).decode('utf-8')
                    vscore = ser.read(2).decode('utf-8')
                match = ser.read(3).decode('utf-8')
                advteam = ser.read(1).decode('utf-8')
                line1 = "TEAM MATCH    ADV   TEAM"
                if wrtime != 1:
                    line2 = hteamscore + "    " + match + "             " + vteamscore
                else:
                    if advteam == "H":
                        line2 = hteamscore + "    " + match + "  <  " +advmin + ":" + advsec + "    " + vteamscore
                    elif advteam == "V":
                        line2 = hteamscore + "    " + match + "     " +advmin + ":" + advsec + " >  " + vteamscore
                    else:
                        line2 = hteamscore + "    " + match + "             " + vteamscore
                line3 = emptyline
                line4 = emptyline
                sport = "WR"
            if data == b'G':
                min = ser.read(2).decode('utf-8')
                sec = ser.read(2).decode('utf-8')
                ts = ser.read(1).decode('utf-8')
                per = ser.read(1).decode('utf-8')
                advmin = ser.read(1).decode('utf-8')
                advsec = ser.read(2).decode('utf-8')
                otherts = ts
                if intClock == "Y":
                    if ts != " ":
                        if lastPack == ts:
                            if twoLastPack != lastPack:
                                temp = int(ts)
                                temp = temp - 1
                                if temp == -1:
                                    if sec == " 0" or sec == "00":
                                        temp = 0
                                    else:
                                        temp = 9
                                ts = str(temp)
                        threeLastPack = twoLastPack
                        twoLastPack = lastPack
                        lastPack = otherts
                wrtime = 1
                #TEAM MATCH    ADV   TEAM
                #00    000  <  0:00 >  00
                #
                #
            if data == b'T':
                data = ser.read(1)
                if data == b'H':
                    hname = ser.read(10).decode('utf-8')
                    hscore = ser.read(2).decode('utf-8')
                    hhits = ser.read(2).decode('utf-8')
                    herr = ser.read(1).decode('utf-8')
                    h1 = ser.read(2).decode('utf-8')
                    h2 = ser.read(2).decode('utf-8')
                    h3 = ser.read(2).decode('utf-8')
                    h4 = ser.read(2).decode('utf-8')
                    h5 = ser.read(2).decode('utf-8')
                    h6 = ser.read(2).decode('utf-8')
                    h7 = ser.read(2).decode('utf-8')
                    h8 = ser.read(2).decode('utf-8')
                    h9 = ser.read(2).decode('utf-8')
                    h10 = ser.read(2).decode('utf-8')
                    inning10 = ser.read(1).decode('utf-8')
                    hinn = 1
                if data == b'V':
                    vname = ser.read(10).decode('utf-8')
                    vscore = ser.read(2).decode('utf-8')
                    vhits = ser.read(2).decode('utf-8')
                    verr = ser.read(1).decode('utf-8')
                    v1 = ser.read(2).decode('utf-8')
                    v2 = ser.read(2).decode('utf-8')
                    v3 = ser.read(2).decode('utf-8')
                    v4 = ser.read(2).decode('utf-8')
                    v5 = ser.read(2).decode('utf-8')
                    v6 = ser.read(2).decode('utf-8')
                    v7 = ser.read(2).decode('utf-8')
                    v8 = ser.read(2).decode('utf-8')
                    v9 = ser.read(2).decode('utf-8')
                    v10 = ser.read(2).decode('utf-8')
                    inning10 = ser.read(1).decode('utf-8')
                    vinn = 1
                #    1 2 3 4 5 6 7 8 9 10
                #V   0 0 0 0 0 0 0 0 0  0  
                #H   0 0 0 0 0 0 0 0 0  0
                #B:0 S:0 O:0 -- H:00  E:7
                #123456789012345678901234
                if inning10 == "0":
                    line1 = "    1 2 3 4 5 6 7 8 9 10"
                if inning10 == "1":
                    line1 = "   111213141516171819 20"
                if vinn == 1:
                    if tb == "V":
                        line2 = "V> " + v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + " " +v10
                    else:
                        line2 = "V  " + v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + " " +v10
                if hinn == 1:
                    if tb == "H":
                        line3 = "H> " + h1 + h2 + h3 + h4 + h5 + h6 + h7 + h8 + h9 + " " +h10
                    else:
                        line3 = "H  " + h1 + h2 + h3 + h4 + h5 + h6 + h7 + h8 + h9 + " " +h10
                if b == " " and s == " ":
                    if o != " ":
                        bso = "  OUTS: " + o + "  "
                            #B:0 S:0 O:0
                    else:
                        bso = "   " + "    "  + "    "
                else:
                    bso = "B:" + b + " S:" + s + " O:" + o
                if atbat == "  " and vinn == 1 and hinn == 1:
                    if tb == "H":
                        line4 = bso + " " + hiterr + " H:" + hhits + "  E:" + verr
                    elif tb == "V":
                        line4 = bso + " " + hiterr + " H:" + vhits + "  E:" + herr
                    else:
                        if per == " " and bso == "           ":
                            line4 = "H:" + hhits + " E:" + herr + "        E:" + verr + " H:" + vhits
                            #        H:00 E:0        E:0 H:00
                            #        123456789012345678901234
                        else:
                            line4 = bso + " " + hiterr + "          "
                else:
                    line4 = bso + " " + hiterr + " AT BAT:" + atbat
                min = "  "
                sec = min
                ts = " "
            scores = hscore + vscore
            if hname == "          ":
                hname = nohname
            if vname == "          ":
                vname = novname
            names = hname + vname
            time = min+sec+ts
            if txt == 1:
                if scores != scores2:
                    ui = 1
                    htemp = hscore
                    vtemp = vscore
                    if spaces == 1:
                        if len(htemp) == 3:
                            if htemp[0] == ' ':
                                htemp = htemp[1:]
                        if len(htemp) == 2:
                            if htemp[0] == ' ':
                                htemp = htemp[1:]
                        if len(vtemp) == 3:
                            if vtemp[0] == ' ':
                                vtemp = vtemp[1:]
                        if len(vtemp) == 2:
                            if vtemp[0] == ' ':
                                vtemp = vtemp[1:]
                    outputfile = open(os.path.join(basicDir,"hscore.txt"), "w")
                    outputfile.write(htemp)
                    outputfile.close()
                    outputfile = open(os.path.join(basicDir,"vscore.txt"), "w")
                    outputfile.write(vtemp)
                    outputfile.close()
                    scores2 = scores
                if names != names2:
                    ui = 1
                    outputfile = open(os.path.join(basicDir,"hname.txt"), "w")
                    outputfile.write(hname)
                    outputfile.close()
                    outputfile = open(os.path.join(basicDir,"vname.txt"), "w")
                    outputfile.write(vname)
                    outputfile.close()
                    names2 = names
                if per != per2:
                    ui = 1
                    if percust == 1:
                        if per == "1":
                            temp = OnePCust
                        elif per == "2":
                            temp = TwoPCust
                        elif per == "3":
                            temp = ThreePCust
                        elif per == "4":
                            temp = FourPCust
                        elif per == "5":
                            temp = FivePCust
                        elif per == "6":
                            temp = SixPCust
                        elif per == "7":
                            temp = SevenPCust
                        elif per == "8":
                            temp = EightPCust
                        elif per == "9":
                            temp = NinePCust
                        elif per == "0":
                            temp = ZeroPCust
                        elif per == " ":
                            temp = blankPCust
                    else:
                        temp = per
                    outputfile = open(os.path.join(basicDir,"period.txt"), "w")
                    outputfile.write(temp)
                    outputfile.close()
                    per2 = per
                if line1 != line12:
                    ui = 1
                    outputfile = open(os.path.join(uniDir,"line1.txt"), "w")
                    outputfile.write(line1)
                    outputfile.close()
                    line12 = line1
                    if sportspecific == 1:
                        sstxt = 1
                if line2 != line22:
                    ui = 1
                    outputfile = open(os.path.join(uniDir,"line2.txt"), "w")
                    outputfile.write(line2)
                    outputfile.close()
                    line22 = line2
                    if sportspecific == 1:
                        sstxt = 1
                if line3 != line32:
                    ui = 1
                    outputfile = open(os.path.join(uniDir,"line3.txt"), "w")
                    outputfile.write(line3)
                    outputfile.close()
                    line32 = line3
                    if sportspecific == 1:
                        sstxt = 1
                if line4 != line42:
                    ui = 1
                    outputfile = open(os.path.join(uniDir,"line4.txt"), "w")
                    outputfile.write(line4)
                    outputfile.close()
                    line42 = line4
                    if sportspecific == 1:
                        sstxt = 1
                if sportspecific == 1 and sstxt == 1:
                    #"C:\Users\thego\Desktop\Universal\sportspecific"
                    #"C:/Users/thego/Desktop/Universal/sportspecific/"
                    if sport == "FB":
                        fileDirTemp = fbDir
                        outputfile = open(os.path.join(fileDirTemp, "htol.txt"), "w")
                        outputfile.write(htol)
                        outputfile.close()
                        outputfile = open(os.path.join(fileDirTemp, "vtol.txt"), "w")
                        outputfile.write(vtol)
                        outputfile.close()
                        temp = ballon
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "ballon.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = togo
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "togo.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        outputfile = open(os.path.join(fileDirTemp, "down.txt"), "w")
                        outputfile.write(down)
                        outputfile.close()
                        if poss == "H":
                            temp = hPossVal
                        else:
                            temp = " "
                        outputfile = open(os.path.join(fileDirTemp, "hposs.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        if poss == "V":
                            temp = vPossVal
                        else:
                            temp = " "
                        outputfile = open(os.path.join(fileDirTemp, "vposs.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                    if sport == "BA" and hinn == 1 and vinn == 1:
                        fileDirTemp = baDir
                        temp = h1
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "h1.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = h2
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "h2.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = h3
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "h3.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = h4
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "h4.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = h5
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "h5.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = h6
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "h6.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = h7
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "h7.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = h8
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "h8.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = h9
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "h9.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = h10
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "h10.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = v1
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "v1.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = v2
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "v2.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = v3
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "v3.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = v4
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "v4.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = v5
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "v5.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = v6
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "v6.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = v7
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "v7.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = v8
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "v8.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = v9
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "v9.txt"), "w")
                        outputfile.write(temp)
                        temp = v10
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile.close()
                        outputfile = open(os.path.join(fileDirTemp, "v10.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        outputfile = open(os.path.join(fileDirTemp, "outs.txt"), "w")
                        outputfile.write(o)
                        outputfile.close()
                        outputfile = open(os.path.join(fileDirTemp, "strikes.txt"), "w")
                        outputfile.write(s)
                        outputfile.close()
                        outputfile = open(os.path.join(fileDirTemp, "balls.txt"), "w")
                        outputfile.write(b)
                        outputfile.close()
                        temp = atbat
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "atbat.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        outputfile = open(os.path.join(fileDirTemp, "play.txt"), "w")
                        outputfile.write(hiterr)
                        outputfile.close()


                        if tb == "H":
                            temp = hPossVal
                        else:
                            temp = " "
                        outputfile = open(os.path.join(fileDirTemp, "hposs.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        if tb == "V":
                            temp = vPossVal
                        else:
                            temp = " "
                        outputfile = open(os.path.join(fileDirTemp, "vposs.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()


                        temp = hhits
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "hhits.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = herr
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "herr.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = vhits
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "vhits.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = verr
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "verr.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        if inning10 == "0":
                            inning = per
                        elif inning10 == "1":
                            if per == 0:
                                inning = "20"
                            else:
                                inning = "1" + per
                        if spaces == 1:
                            if len(inning) == 2:
                                if inning[0] == ' ':
                                    inning = inning[1:]
                        outputfile = open(os.path.join(fileDirTemp, "inning.txt"), "w")
                        outputfile.write(inning)
                        outputfile.close()
                    if sport == "BB" and bbhome == 1 and bbvis == 1:
                        fileDirTemp = bbDir
                        temp = hfls
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "hfls.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = vfls
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "vfls.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        outputfile = open(os.path.join(fileDirTemp, "htol.txt"), "w")
                        outputfile.write(htol)
                        outputfile.close()
                        temp = plyr
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "plyr.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                       
                        outputfile = open(os.path.join(fileDirTemp, "fls.txt"), "w")
                        outputfile.write(fls)
                        outputfile.close()
                        temp = pts
                        if spaces == 1:
                            if len(temp) == 2:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "pts.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()


                        outputfile = open(os.path.join(fileDirTemp, "vtol.txt"), "w")
                        outputfile.write(vtol)
                        outputfile.close()
                        if hbns1 == "1" and hbns2 == "0":
                            temp = hBonusVal
                        elif hbns1 == "1" and hbns2 == "1":
                            temp = hDBonusVal
                        else:
                            temp = " "
                        outputfile = open(os.path.join(fileDirTemp, "hbns.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        if vbns1 == "1" and vbns2 == "0":
                            temp = vBonusVal
                        elif vbns1 == "1" and vbns2 == "1":
                            temp = vDBonusVal
                        else:
                            temp = " "
                        outputfile = open(os.path.join(fileDirTemp, "vbns.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        if hposs == "1":
                            temp = hPossVal
                        else:
                            temp = " "
                        outputfile = open(os.path.join(fileDirTemp, "hposs.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        if vposs == "1":
                            temp = vPossVal
                        else:
                            temp = " "
                        outputfile = open(os.path.join(fileDirTemp, "vposs.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                    if sport == "BB" and bbstath == 1 and bbvstat == 1:
                        fileDirTemp = bbDir
                        if spaces == 1:
                            if len(hp1no) == 2:
                                if hp1no[0] == ' ':
                                    hp1no = hp1no[1:]
                            if len(hp2no) == 2:
                                if hp2no[0] == ' ':
                                    hp2no = hp2no[1:]
                            if len(hp3no) == 2:
                                if hp3no[0] == ' ':
                                    hp3no = hp3no[1:]
                            if len(hp4no) == 2:
                                if hp4no[0] == ' ':
                                    hp4no = hp4no[1:]
                            if len(hp5no) == 2:
                                if hp5no[0] == ' ':
                                    hp5no = hp5no[1:]
                        temp = hp1no + "\n" + hp2no + "\n" + hp3no + "\n" + hp4no + "\n" + hp5no
                        outputfile = open(os.path.join(fileDirTemp, "hstatno.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        if spaces == 1:
                            if len(hp1pts) == 2:
                                if hp1pts[0] == ' ':
                                    hp1pts = hp1pts[1:]
                            if len(hp2pts) == 2:
                                if hp2pts[0] == ' ':
                                    hp2pts = hp2pts[1:]
                            if len(hp3pts) == 2:
                                if hp3pts[0] == ' ':
                                    hp3pts = hp3pts[1:]
                            if len(hp4pts) == 2:
                                if hp4pts[0] == ' ':
                                    hp4pts = hp4pts[1:]
                            if len(hp5pts) == 2:
                                if hp5pts[0] == ' ':
                                    hp5pts = hp5pts[1:]
                        temp = hp1fls + "\n" + hp2fls + "\n" + hp3fls + "\n" + hp4fls + "\n" + hp5fls
                        outputfile = open(os.path.join(fileDirTemp, "hstatfls.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = hp1pts + "\n" + hp2pts + "\n" + hp3pts + "\n" + hp4pts + "\n" + hp5pts
                        outputfile = open(os.path.join(fileDirTemp, "hstatpts.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = hp1name + "\n" + hp2name + "\n" + hp3name + "\n" + hp4name + "\n" + hp5name
                        outputfile = open(os.path.join(fileDirTemp, "hstatname.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = vp1name + "\n" + vp2name + "\n" + vp3name + "\n" + vp4name + "\n" + vp5name
                        outputfile = open(os.path.join(fileDirTemp, "vstatname.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        if spaces == 1:
                            if len(vp1no) == 2:
                                if vp1no[0] == ' ':
                                    vp1no = vp1no[1:]
                            if len(vp2no) == 2:
                                if vp2no[0] == ' ':
                                    vp2no = vp2no[1:]
                            if len(vp3no) == 2:
                                if vp3no[0] == ' ':
                                    vp3no = vp3no[1:]
                            if len(vp4no) == 2:
                                if vp4no[0] == ' ':
                                    vp4no = vp4no[1:]
                            if len(vp5no) == 2:
                                if vp5no[0] == ' ':
                                    vp5no = vp5no[1:]
                        temp = vp1no + "\n" + vp2no + "\n" + vp3no + "\n" + vp4no + "\n" + vp5no
                        outputfile = open(os.path.join(fileDirTemp, "vstatno.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        temp = vp1fls + "\n" + vp2fls + "\n" + vp3fls + "\n" + vp4fls + "\n" + vp5fls
                        outputfile = open(os.path.join(fileDirTemp, "vstatfls.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        if spaces == 1:
                            if len(vp1pts) == 2:
                                if vp1pts[0] == ' ':
                                    vp1pts = vp1pts[1:]
                            if len(vp2pts) == 2:
                                if vp2pts[0] == ' ':
                                    vp2pts = vp2pts[1:]
                            if len(vp3pts) == 2:
                                if vp3pts[0] == ' ':
                                    vp3pts = vp3pts[1:]
                            if len(vp4pts) == 2:
                                if vp4pts[0] == ' ':
                                    vp4pts = vp4pts[1:]
                            if len(vp5pts) == 2:
                                if vp5pts[0] == ' ':
                                    vp5pts = vp5pts[1:]
                        temp = vp1pts + "\n" + vp2pts + "\n" + vp3pts + "\n" + vp4pts + "\n" + vp5pts
                        outputfile = open(os.path.join(fileDirTemp, "vstatpts.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                        if config["UIStats"] == "Y":
                            ui = 1
                    if sport == "WR":
                        fileDirTemp = wrDir
                        if spaces == 1:
                            if len(hteamscore) == 2:
                                if hteamscore[0] == ' ':
                                    hteamscore = hteamscore[1:]
                            if len(vteamscore) == 2:
                                if vteamscore[0] == ' ':
                                    vteamscore = vteamscore[1:]
                        outputfile = open(os.path.join(fileDirTemp, "hteampts.txt"), "w")
                        outputfile.write(hteamscore)
                        outputfile.close()
                        outputfile = open(os.path.join(fileDirTemp, "vteampts.txt"), "w")
                        outputfile.write(vteamscore)
                        outputfile.close()
                        if spaces == 1:
                            if len(match) == 3:
                                if match[0] == ' ':
                                    match = match[1:]
                            if len(match) == 2:
                                if match[0] == ' ':
                                    match = match[1:]
                        outputfile = open(os.path.join(fileDirTemp, "match.txt"), "w")
                        outputfile.write(match)
                        outputfile.close()
                        roster = json.load(open("rosters.json"))
                        if match == "   ":
                            hwrname = " "
                        else:
                            try:
                                hwrname = roster[hrost][match]
                            except:
                                hwrname = " "
                        if match == "   ":
                            vwrname = " "
                        else:
                            try:
                                vwrname = roster[vrost][match]
                            except:
                                vwrname = " "
                        outputfile = open(os.path.join(fileDirTemp, "hwrestler.txt"), "w")
                        outputfile.write(hwrname)
                        outputfile.close()
                        outputfile = open(os.path.join(fileDirTemp, "vwrestler.txt"), "w")
                        outputfile.write(vwrname)
                        outputfile.close()
                    if sport == "HK":
                        fileDirTemp = hkDir
                        if spaces == 1:
                            if len(hp1no) == 2:
                                if hp1no[0] == ' ':
                                    hp1no = hp1no[1:]
                            if len(hp2no) == 2:
                                if hp2no[0] == ' ':
                                    hp2no = hp2no[1:]
                            if len(vp1no) == 2:
                                if vp1no[0] == ' ':
                                    vp1no = vp1no[1:]
                            if len(vp2no) == 2:
                                if vp2no[0] == ' ':
                                    vp2no = vp2no[1:]
                        outputfile = open(os.path.join(fileDirTemp, "hp1no.txt"), "w")
                        outputfile.write(hp1no)
                        outputfile.close()
                        outputfile = open(os.path.join(fileDirTemp, "hp2no.txt"), "w")
                        outputfile.write(hp2no)
                        outputfile.close()
                        outputfile = open(os.path.join(fileDirTemp, "vp1no.txt"), "w")
                        outputfile.write(vp1no)
                        outputfile.close()
                        outputfile = open(os.path.join(fileDirTemp, "vp2no.txt"), "w")
                        outputfile.write(vp2no)
                        outputfile.close()
                        outputfile = open(os.path.join(fileDirTemp, "vp2no.txt"), "w")
                        outputfile.write(vp2no)
                        outputfile.close()
                        if spaces == 1:
                            if len(hsog) == 2:
                                if hsog[0] == ' ':
                                    hsog = hsog[1:]
                            if len(vsog) == 2:
                                if vsog[0] == ' ':
                                    vsog = vsog[1:]
                        outputfile = open(os.path.join(fileDirTemp, "vsog.txt"), "w")
                        outputfile.write(vsog)
                        outputfile.close()
                        outputfile = open(os.path.join(fileDirTemp, "hsog.txt"), "w")
                        outputfile.write(hsog)
                        outputfile.close()
                        if hksaves == 1:
                            htempsog = hsog
                            vtempsog = vsog
                            htempscore = hscore
                            vtempscore = vscore
                            if len(htempsog) == 2:
                                if htempsog[0] == ' ':
                                    htempsog = htempsog[1:]
                            if len(vtempsog) == 2:
                                if vtempsog[0] == ' ':
                                    vtempsog = vtempsog[1:]
                            if len(htempscore) == 2:
                                if htempscore[0] == ' ':
                                    htempscore = htempscore[1:]
                            if len(vtempscore) == 2:
                                if vtempscore[0] == ' ':
                                    vtempscore = vtempscore[1:]
                            try:
                                hsaves = int(vtempsog) - int(vtempscore)
                            except:
                                hsaves = "0"
                            try:
                                vsaves = int(htempsog) - int(htempscore)
                            except:
                                vsaves = "0"
                            hsaves = str(hsaves)
                            vsaves = str(vsaves)
                            outputfile = open(os.path.join(fileDirTemp, "vsaves.txt"), "w")
                            outputfile.write(vsaves)
                            outputfile.close()
                            outputfile = open(os.path.join(fileDirTemp, "hsaves.txt"), "w")
                            outputfile.write(hsaves)
                            outputfile.close()




                        if hp1min == "  " and hp1sec == "  ":
                            temp = "     "
                        else:
                            temp = hp1min + ":" + hp1sec
                        if spaces == 1:
                            if len(temp) == 5:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "hp1time.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                   
                        if hp2min == "  " and hp2sec == "  ":
                            temp = "     "
                        else:
                            temp = hp2min + ":" + hp2sec
                        if spaces == 1:
                            if len(temp) == 5:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "hp2time.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                   
                        if vp1min == "  " and vp1sec == "  ":
                            temp = "     "
                        else:
                            temp = vp1min + ":" + vp1sec
                        if spaces == 1:
                            if len(temp) == 5:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "vp1time.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                   
                        if vp2min == "  " and vp2sec == "  ":
                            temp = "     "
                        else:
                            temp = vp2min + ":" + vp2sec
                        if spaces == 1:
                            if len(temp) == 5:
                                if temp[0] == ' ':
                                    temp = temp[1:]
                        outputfile = open(os.path.join(fileDirTemp, "vp2time.txt"), "w")
                        outputfile.write(temp)
                        outputfile.close()
                    sstxt = 0
                if time != time2:
                    ui = 1
                    if min == " 0" and ts != " " and zeros == "0":
                        if sec == "01":
                            guisec = " 1"
                        elif sec == "02":
                            guisec = " 2"
                        elif sec == "03":
                            guisec = " 3"
                        elif sec == "04":
                            guisec = " 4"
                        elif sec == "05":
                            guisec = " 5"
                        elif sec == "06":
                            guisec = " 6"
                        elif sec == "07":
                            guisec = " 7"
                        elif sec == "08":
                            guisec = " 8"
                        elif sec == "09":
                            guisec = " 9"
                        elif sec == "00":
                            guisec = " 0"
                        else:
                            guisec = sec
                        google = guisec + "." + ts
                    elif min == " 0" and ts != " " and zeros == "00":
                        if sec == "01":
                            guisec = "01"
                        elif sec == "02":
                            guisec = "02"
                        elif sec == "03":
                            guisec = "03"
                        elif sec == "04":
                            guisec = "04"
                        elif sec == "05":
                            guisec = "05"
                        elif sec == "06":
                            guisec = "06"
                        elif sec == "07":
                            guisec = "07"
                        elif sec == "08":
                            guisec = "08"
                        elif sec == "09":
                            guisec = "09"
                        elif sec == "00":
                            guisec = "00"
                        else:
                            guisec = sec
                        google = guisec + "." + ts
                    elif min and sec == "  ":
                        google = "     "
                    else:
                        google = min+":"+sec
                    if min == " " and sec == " ":
                        txttime = "     "
                    else:
                        txttime = min + ":" + sec
                    if spaces == 1:
                        if len(txttime) == 5:
                            if txttime[0] == ' ':
                                txttime = txttime[1:]
                        if len(google) == 5:
                            if google[0] == ' ':
                                google = google[1:]
                        if len(google) == 4:
                            if google[0] == ' ':
                                google = google[1:]
                    if txttime2 != txttime and txt10ths == 0:
                        outputfile = open(os.path.join(basicDir,"clock.txt"), "w")
                        outputfile.write(txttime)
                        outputfile.close()
                        txttime2 = txttime
                    if txttime2 != google and txt10ths == 1:
                        outputfile = open(os.path.join(basicDir,"clock.txt"), "w")
                        outputfile.write(google)
                        outputfile.close()
                        txttime2 = google
                if timer2 != timer:
                    ui = 1
                    temp = timer
                    if spaces == 1:
                        if len(temp) == 2:
                            if temp[0] == ' ':
                                temp = temp[1:]
                    outputfile = open(os.path.join(basicDir,"timer.txt"), "w")
                    outputfile.write(temp)
                    outputfile.close()
                    timer2 = timer
                if min == " 0" and ts != " ":
                    if sec == "01":
                        uisec = " 1"
                    elif sec == "02":
                        uisec = " 2"
                    elif sec == "03":
                        uisec = " 3"
                    elif sec == "04":
                        uisec = " 4"
                    elif sec == "05":
                        uisec = " 5"
                    elif sec == "06":
                        uisec = " 6"
                    elif sec == "07":
                        uisec = " 7"
                    elif sec == "08":
                        uisec = " 8"
                    elif sec == "09":
                        uisec = " 9"
                    elif sec == "00":
                        uisec = " 0"
                    else:
                        uisec = sec
                    uitime = uisec + "." + ts + " "
                elif min and sec == "  ":
                    uitime = "     "
                else:
                    uitime = min+":"+sec
                time2 = time
            else:
                if min == " 0" and ts != " ":
                    if sec == "01":
                        uisec = " 1"
                    elif sec == "02":
                        uisec = " 2"
                    elif sec == "03":
                        uisec = " 3"
                    elif sec == "04":
                        uisec = " 4"
                    elif sec == "05":
                        uisec = " 5"
                    elif sec == "06":
                        uisec = " 6"
                    elif sec == "07":
                        uisec = " 7"
                    elif sec == "08":
                        uisec = " 8"
                    elif sec == "09":
                        uisec = " 9"
                    elif sec == "00":
                        uisec = " 0"
                    else:
                        uisec = sec
                    uitime = uisec + "." + ts + " "
                elif min and sec == "  ":
                    uitime = "     "
                else:
                    uitime = min+":"+sec

                if uistatyn == 1:
                    try:
                        ui2 = "NO F PT " + hname + " " + uitime + " " + vname + " NO F PT\n" + hp1no + " " + hp1fls + " " + hp1pts + "    " + hscore + "     PER " + per + "     " + vscore + "    " + vp1no + " " + vp1fls + " " + vp1pts + "\n"+ hp2no + " " + hp2fls + " " + hp2pts + "                             "+vp2no + " " + vp2fls + " " + vp2pts +"\n" + hp3no + " " + hp3fls + " " + hp3pts +"   " + line1 +"  " + vp3no + " " + vp3fls + " " + vp3pts+ "\n"+hp4no + " " + hp4fls + " " + hp4pts+"   " + line2+ "  "+vp4no + " " + vp4fls + " " + vp4pts+"\n"+hp5no + " " + hp5fls + " " + hp5pts+"   " + line3+ "  " + vp5no + " " + vp5fls + " " + vp5pts+"\n          " + line4
                    except:
                        ui2 = hname + " " + uitime + " " + vname + "\n    " + hscore + "     PER " + per + "     " + vscore + "\n\n " + line1+ "\n " + line2+ "\n " + line3+ "\n " + line4
                else:
                    ui2 = hname + " " + uitime + " " + vname + "\n    " + hscore + "     PER " + per + "     " + vscore + "\n\n " + line1+ "\n " + line2+ "\n " + line3+ "\n " + line4    
                
                if ui2 != uivar:
                    ui = 1
                
            if ui == 2:
                os.system('clear')
                ui == 1
            if ui == 1:
                LINE_UP = '\033[1A'
                titlevar = "title " + hname + " vs " + vname

                if uitimeryn == 1:
                    uivar = hname + " " + uitime + " " + vname + "   " + timer + "\n    " + hscore + "     PER " + per + "     " + vscore + "\n" + blank  + "\n " + line1+ "\n " + line2+ "\n " + line3+ "\n " + line4
                elif uistatyn == 1:
                    try:
                        uivar = "NO F PT " + hname + " " + uitime + " " + vname + " NO F PT\n" + hp1no + " " + hp1fls + " " + hp1pts + "    " + hscore + "     PER " + per + "     " + vscore + "    " + vp1no + " " + vp1fls + " " + vp1pts + "\n"+ hp2no + " " + hp2fls + " " + hp2pts + "                             "+vp2no + " " + vp2fls + " " + vp2pts +"\n" + hp3no + " " + hp3fls + " " + hp3pts +"   " + line1 +"  " + vp3no + " " + vp3fls + " " + vp3pts+ "\n"+hp4no + " " + hp4fls + " " + hp4pts+"   " + line2+ "  "+vp4no + " " + vp4fls + " " + vp4pts+"\n"+hp5no + " " + hp5fls + " " + hp5pts+"   " + line3+ "  " + vp5no + " " + vp5fls + " " + vp5pts+"\n          " + line4
                    except:
                        uivar = hname + " " + uitime + " " + vname + "\n    " + hscore + "     PER " + per + "     " + vscore + "\n" + blank  + "\n " + line1+ "\n " + line2+ "\n " + line3+ "\n " + line4    
                else:
                    if sport == "BB":
                        uivar = hname + " " + uitime + " " + vname + "\n    " + hscore + "     PER " + per + "     " + vscore + "\n" + blank  + "\n " + line1+ "\n " + line2+ "\n " + line3+ "\n " + line4
                    else:
                        uivar = hname + " " + uitime + " " + vname + "\n    " + hscore + "     PER " + per + "     " + vscore + "\n" + blank  + "\n " + line1+ "\n " + line2+ "\n " + line3+ "\n " + line4
                print(LINE_UP, LINE_UP, LINE_UP, LINE_UP, LINE_UP, LINE_UP, LINE_UP, end="\r")
                print(uivar)
                outputfile = open(os.path.join(basicDir,"ui.txt"), "w")
                outputfile.write(uivar)
                outputfile.close()
                ui = 0
                error = 1
    except:
        if error == 1:
            print("Error Detected, try again\nlater")
            post = 0
            error = 0
        ser.close()
        try:
            ser = serial.Serial(port, baud)
        except:
            print(f"No Connections, verify settings and try again\n{port}, {baud}")
        ui=2