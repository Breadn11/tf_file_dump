import pymem
import time
import pyperclip

WAIT_TIME = 0.25
printMode = False

pm = pymem.Pymem('Transformers2.exe')
module = pymem.process.module_from_name(pm.process_handle, 'Transformers2.exe').lpBaseOfDll

adr_Player = pm.read_uint(module + 0x0093FF64)
adr_Player = pm.read_uint(adr_Player + 0xF0)
adr_Player = pm.read_uint(adr_Player + 0x20)
adr_Player = pm.read_uint(adr_Player + 0x24)
adr_Player = pm.read_uint(adr_Player + 0x1C)
adr_Player = pm.read_uint(adr_Player + 0x0)

adr_X = adr_Player + 0x7C
adr_Y = adr_Player + 0x78
adr_Z = adr_Player + 0x80

def printPosition():
    X = str(pm.read_float(adr_X))
    Y = str(pm.read_float(adr_Y))
    Z = str(pm.read_float(adr_Z))

    print('- - - - -')
    print('X: ' + X)
    print('Y: ' + Y)
    print('Z: ' + Z)

    pyperclip.copy(f'teleportPlayer(*({X}, {Y}, {Z}))')

def teleportPlayer(posX, posY, posZ):
    print(f'Teleporting to ({posX}, {posY}, {posZ})')
    pm.write_float(adr_X, posX)
    pm.write_float(adr_Y, posY)
    pm.write_float(adr_Z, posZ)
    time.sleep(WAIT_TIME)

def doTeleportSequence():
    teleportPlayer(*(111.83826446533203, -410.873779296875, 14.297599792480469))
    teleportPlayer(*(107.88711547851562, -337.6497497558594, 14.309518814086914))
    teleportPlayer(*(109.7603530883789, -278.3379211425781, 14.302570343017578))
    teleportPlayer(*(182.40904235839844, -275.50927734375, 14.302570343017578))
    teleportPlayer(*(179.76336669921875, -227.59042358398438, 14.302576065063477))
    teleportPlayer(*(172.30935668945312, -146.9273681640625, 14.302576065063477))
    teleportPlayer(*(138.9256134033203, -121.7109146118164, 14.30258560180664))
    teleportPlayer(*(114.18777465820312, -116.3575210571289, 14.30258560180664))
    teleportPlayer(*(114.25257873535156, -26.53213119506836, 14.30258560180664))

    # now at the corner with the enemy

    teleportPlayer(*(101.69269561767578, -27.182323455810547, 14.310038566589355))
    teleportPlayer(*(14.904593467712402, -24.288408279418945, 33.02690887451172))
    teleportPlayer(*(9.837270736694336, -7.9873576164245605, 32.16506576538086))
    teleportPlayer(*(-14.06889820098877, 26.853727340698242, 38.58561325073242))
    teleportPlayer(*(-63.92791748046875, 103.9234848022461, 25.702865600585938))
    
    # now just before the ramp orb leading to sand pit

    teleportPlayer(*(-89.5237808227539, 113.01980590820312, 25.874013900756836))
    teleportPlayer(*(-229.2867889404297, 121.47899627685547, 25.15878677368164))
    teleportPlayer(*(-238.56130981445312, 182.63241577148438, 6.458903789520264))
    teleportPlayer(*(-140.16921997070312, 216.7320556640625, 30.944765090942383))
    teleportPlayer(*(-30.790918350219727, 242.88458251953125, 22.608549118041992))
    teleportPlayer(*(31.617534637451172, 393.0925598144531, 22.45695686340332))

    # now just after short bridge, before orb #9 (at 8/17)

    teleportPlayer(*(35.1148796081543, 392.69927978515625, 18.316289901733398))
    teleportPlayer(*(37.948856353759766, 532.272216796875, 22.725534439086914))
    teleportPlayer(*(33.30051803588867, 556.5670776367188, 18.273099899291992))
    teleportPlayer(*(13.094801902770996, 554.7396850585938, 22.603984832763672))
    teleportPlayer(*(-46.839141845703125, 556.6304931640625, 18.313602447509766))
    teleportPlayer(*(-62.82613754272461, 553.9163208007812, 22.027984619140625))
    teleportPlayer(*(-141.09939575195312, 537.1319580078125, 18.319933891296387))
    teleportPlayer(*(-184.33180236816406, 494.8110656738281, 23.411928176879883))

    # just collected 13/17, need to go above small passage

    teleportPlayer(*(-190.58319091796875, 452.657470703125, 33.30009460449219))
    teleportPlayer(*(-201.19107055664062, 380.97357177734375, 14.314251899719238))
    teleportPlayer(*(-159.13534545898438, 399.38018798828125, 34.88617706298828))
    teleportPlayer(*(-77.89188385009766, 419.92327880859375, 14.311485290527344))

    # now at 15/17

    

printMode = True

if printMode == True:
    while True:
        printPosition()
        time.sleep(0.1)

#input("ready ")
doTeleportSequence()
input()