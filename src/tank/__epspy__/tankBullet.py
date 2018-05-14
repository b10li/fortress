## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY
from eudplib import *

def _IGVA(vList, exprListGen):
    def _():
        exprList = exprListGen()
        SetVariables(vList, exprList)
    EUDOnStart(_)

def _CGFW(exprf, retn):
    rets = [ExprProxy(None) for _ in range(retn)]
    def _():
        vals = exprf()
        for ret, val in zip(rets, vals):
            ret._value = val
    EUDOnStart(_)
    return rets

def _ARR(items):
    k = EUDArray(len(items))
    for i, item in enumerate(items):
        k[i] = item
    return k

def _SRET(v, klist):
    return List2Assignable([v[k] for k in klist])

def _SV(dL, sL):
    [d << s for d, s in zip(FlattenList(dL), FlattenList(sL))]

class _ATTW:
    def __init__(self, obj, attrName):
        self.obj = obj
        self.attrName = attrName

    def __lshift__(self, r):
        setattr(self.obj, self.attrName, r)

    def __iadd__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov + v)

    def __isub__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov - v)

    def __imul__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov * v)

    def __idiv__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov / v)

    def __iand__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov & v)

    def __ior__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov | v)

    def __ixor__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov ^ v)

class _ARRW:
    def __init__(self, obj, index):
        self.obj = obj
        self.index = index

    def __lshift__(self, r):
        self.obj[self.index] = r

    def __iadd__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov + v

    def __isub__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov - v

    def __imul__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov * v

    def __idiv__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov / v

    def __iand__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov & v

    def __ior__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov | v

    def __ixor__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov ^ v

def _L2V(l):
    ret = EUDVariable()
    if EUDIf()(l):
        ret << 1
    if EUDElse()():
        ret << 0
    EUDEndIf()
    return ret

def _MVAR(vs):
    return List2Assignable([
        v.makeL() if IsEUDVariable(v) else EUDVariable() << v
        for v in FlattenList(vs)])

def _LSH(l, r):
    if IsEUDVariable(l):  return f_bitlshift(l, r)
    else: return l << r

## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY

# (Line 1) import header;
import header
# (Line 2) import util.utilEud;
from util import utilEud
# (Line 3) import util.utilMath;
from util import utilMath
# (Line 4) import tank.tankAim;
from tank import tankAim
# (Line 5) import tank.tankWeapon;
from tank import tankWeapon
# (Line 6) import physics;
import physics
# (Line 7) import sound.emplayer;
from sound import emplayer
# (Line 9) const TOPSPEED = 46;
TOPSPEED = _CGFW(lambda: [46], 1)[0]
# (Line 10) const BOTSPEED = 2;
BOTSPEED = _CGFW(lambda: [2], 1)[0]
# (Line 12) const gravity = 1;
gravity = _CGFW(lambda: [1], 1)[0]
# (Line 13) const pTargetArray = EUDArray(10);
pTargetArray = _CGFW(lambda: [EUDArray(10)], 1)[0]
# (Line 14) var epdnum = 0;
epdnum = EUDCreateVariables(1)
_IGVA([epdnum], lambda: [0])
# (Line 15) var framebool = 0;
framebool = EUDCreateVariables(1)
_IGVA([framebool], lambda: [0])
# (Line 17) function push(unitEpd)
# (Line 18) {
@EUDFunc
def f_push(unitEpd):
    # (Line 19) pTargetArray[epdnum] = unitEpd;
    _ARRW(pTargetArray, epdnum) << (unitEpd)
    # (Line 20) epdnum = epdnum + 1;
    epdnum << (epdnum + 1)
    # (Line 21) }
    # (Line 22) function popmid(unitEpd)

# (Line 23) {
@EUDFunc
def f_popmid(unitEpd):
    # (Line 24) for(var i=0; i<10; i++)
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= 10, neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 25) {
        # (Line 26) if(pTargetArray[i] == unitEpd)
        if EUDIf()(pTargetArray[i] == unitEpd):
            # (Line 27) {
            # (Line 28) pTargetArray[i] = 0;
            _ARRW(pTargetArray, i) << (0)
            # (Line 29) epdnum = epdnum - 1;
            epdnum << (epdnum - 1)
            # (Line 30) }
            # (Line 31) }
        EUDEndIf()
        # (Line 32) }
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    # (Line 33) function boom(unitType, locID);

# (Line 34) function speedLimit(v);
# (Line 35) function renderBullet(wind)
# (Line 36) {//bullet physics
@EUDFunc
def f_renderBullet(wind):
    # (Line 37) for(var i=0; i<10; i++)
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= 10, neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 38) {
        # (Line 39) if(pTargetArray[i])
        if EUDIf()(pTargetArray[i]):
            # (Line 40) {
            # (Line 41) const locID = $L('locBullet');
            locID = GetLocationIndex('locBullet')
            # (Line 42) const unitEpd = pTargetArray[i];
            unitEpd = pTargetArray[i]
            # (Line 43) const unitType = utilEud.getUnitType(unitEpd);
            unitType = utilEud.f_getUnitType(unitEpd)
            # (Line 45) physics.renderUnit(unitEpd, 1);
            physics.f_renderUnit(unitEpd, 1)
            # (Line 46) MoveLocation(locID+1, unitType, $P7, $L('locDst')+1);
            DoActions(MoveLocation(locID + 1, unitType, 6, GetLocationIndex('locDst') + 1))
            # (Line 47) if(pTargetArray[0]) utilEud.CenterViewAll(locID);
            if EUDIf()(pTargetArray[0]):
                utilEud.CenterViewAll(locID)
                # (Line 50) if(Bring($P8, AtLeast, 1, '(buildings)', locID+1)
            EUDEndIf()
            _t5 = EUDIf()
            # (Line 51) || Bring($Force1, AtLeast, 1, '(men)', locID+1)
            # (Line 52) /*|| Bring($Force3, AtLeast, 1, '(men)', locID+1)*/)
            if _t5(EUDSCOr()(Bring(7, AtLeast, 1, '(buildings)', locID + 1))(Bring(18, AtLeast, 1, '(men)', locID + 1))()):
                # (Line 53) {//collision
                # (Line 54) popmid(unitEpd);
                f_popmid(unitEpd)
                # (Line 55) if(unitType == header.List[2*3+1]
                _t6 = EUDIf()
                # (Line 56) || unitType == header.List[2*3+2]
                # (Line 57) || unitType == header.List[9*3+1])
                if _t6(EUDSCOr()(unitType == header.List[2 * 3 + 1])(unitType == header.List[2 * 3 + 2])(unitType == header.List[9 * 3 + 1])()):
                    # (Line 58) {
                    # (Line 59) KillUnit(unitType, $P7);
                    DoActions(KillUnit(unitType, 6))
                    # (Line 60) }
                    # (Line 61) else RemoveUnitAt(1, '(men)', locID+1, $P7);
                if EUDElse()():
                    DoActions(RemoveUnitAt(1, '(men)', locID + 1, 6))
                    # (Line 63) if(unitType == header.List[7*3+2])
                EUDEndIf()
                if EUDIf()(unitType == header.List[7 * 3 + 2]):
                    # (Line 64) CreateUnitWithProperties(1, 13, locID+1, $P8, UnitProperty(invincible = true));
                    DoActions(CreateUnitWithProperties(1, 13, locID + 1, 7, UnitProperty(invincible=True)))
                    # (Line 65) else if(unitType == header.List[9*3+2])
                if EUDElseIf()(unitType == header.List[9 * 3 + 2]):
                    # (Line 66) {//overlord
                    # (Line 67) const gasEpd = epdread_epd(EPD(0x628438));
                    gasEpd = f_epdread_epd(EPD(0x628438))
                    # (Line 68) CreateUnitWithProperties(1, 84, locID+1, $P8, UnitProperty(invincible = true));
                    DoActions(CreateUnitWithProperties(1, 84, locID + 1, 7, UnitProperty(invincible=True)))
                    # (Line 69) bwrite_epd(gasEpd + 0x118 / 4,  0x118 % 4, 1000);
                    f_bwrite_epd(gasEpd + 0x118 // 4, 0x118 % 4, 1000)
                    # (Line 70) wwrite_epd(gasEpd + 0x110 / 4,  0x110 % 4, 1010);
                    f_wwrite_epd(gasEpd + 0x110 // 4, 0x110 % 4, 1010)
                    # (Line 71) }
                    # (Line 72) else boom(unitType, locID);
                if EUDElse()():
                    f_boom(unitType, locID)
                    # (Line 73) }
                EUDEndIf()
                # (Line 74) else if(!utilEud.isAtLocation(unitEpd, $L('PlayArea')))
            if EUDElseIf()(utilEud.f_isAtLocation(unitEpd, GetLocationIndex('PlayArea')), neg=True):
                # (Line 75) {// out of playarea
                # (Line 76) popmid(unitEpd);
                f_popmid(unitEpd)
                # (Line 77) RemoveUnitAt(1, '(men)', locID+1, $P7);
                DoActions(RemoveUnitAt(1, '(men)', locID + 1, 6))
                # (Line 78) }
                # (Line 79) else
                # (Line 80) {
            if EUDElse()():
                # (Line 81) var vx, vy = physics.getVxy(unitEpd);
                vx, vy = _MVAR([physics.f_getVxy(unitEpd)])
                # (Line 83) vx = speedLimit(vx);
                vx << (f_speedLimit(vx))
                # (Line 84) vy = speedLimit(vy);
                vy << (f_speedLimit(vy))
                # (Line 86) var nw, ng;
                nw, ng = EUDCreateVariables(2)
                # (Line 88) if(framebool % 2) ng = 0;
                if EUDIf()(framebool % 2):
                    ng << (0)
                    # (Line 89) else ng = 1;
                if EUDElse()():
                    ng << (1)
                    # (Line 90) if(framebool == 0) nw = 2- wind/2;
                EUDEndIf()
                if EUDIf()(framebool == 0):
                    nw << (2 - wind // 2)
                    # (Line 91) else nw = 0;
                if EUDElse()():
                    nw << (0)
                    # (Line 92) physics.setVxy(unitEpd, vx + nw, vy + gravity);
                EUDEndIf()
                physics.f_setVxy(unitEpd, vx + nw, vy + gravity)
                # (Line 93) }
                # (Line 94) }
            EUDEndIf()
            # (Line 95) }
        EUDEndIf()
        # (Line 96) framebool = (framebool+1)%6;
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    framebool << ((framebool + 1) % 6)
    # (Line 97) }
    # (Line 98) function speedLimit(v)

# (Line 99) {
@EUDFunc
def f_speedLimit(v):
    # (Line 100) var num = v;
    num = EUDVariable()
    num << (v)
    # (Line 101) if(utilMath.abs(num) > (TOPSPEED + BOTSPEED))
    if EUDIf()(utilMath.f_abs(num) <= (TOPSPEED + BOTSPEED), neg=True):
        # (Line 102) {
        # (Line 103) if(num >= 0x80000000) num = -(TOPSPEED + BOTSPEED);
        if EUDIf()(num >= 0x80000000):
            num << (-(TOPSPEED + BOTSPEED))
            # (Line 104) else num = (TOPSPEED + BOTSPEED);
        if EUDElse()():
            num << ((TOPSPEED + BOTSPEED))
            # (Line 105) }
        EUDEndIf()
        # (Line 106) return num;
    EUDEndIf()
    EUDReturn(num)
    # (Line 107) }
    # (Line 111) function getBullet(unitType, num);

# (Line 112) function toggleBullet(unitEpd)
# (Line 113) {
@EUDFunc
def f_toggleBullet(unitEpd):
    # (Line 114) const unitType = utilEud.getUnitType(unitEpd);
    unitType = utilEud.f_getUnitType(unitEpd)
    # (Line 115) const player = utilEud.getPlayerID(unitEpd);
    player = utilEud.f_getPlayerID(unitEpd)
    # (Line 117) const nextQ = (utilEud.getDeath(player, header.bulletQ)+1)%2;
    nextQ = (utilEud.f_getDeath(player, header.bulletQ) + 1) % 2
    # (Line 118) SetDeaths(player, SetTo, nextQ, header.bulletQ);
    DoActions(SetDeaths(player, SetTo, nextQ, header.bulletQ))
    # (Line 119) const bullet = getBullet(unitType, nextQ);
    bullet = f_getBullet(unitType, nextQ)
    # (Line 121) utilEud.setBuildQueue1(unitEpd, bullet);
    utilEud.f_setBuildQueue1(unitEpd, bullet)
    # (Line 122) }
    # (Line 124) function makeBullet(unitType, x, y, angle, speed)

# (Line 125) {
@EUDFunc
def f_makeBullet(unitType, x, y, angle, speed):
    # (Line 126) const locID = $L('locBullet');
    locID = GetLocationIndex('locBullet')
    # (Line 127) utilEud.moveLocationXY(locID, x, y);
    utilEud.f_moveLocationXY(locID, x, y)
    # (Line 128) const unitEpd = epdread_epd(EPD(0x628438));
    unitEpd = f_epdread_epd(EPD(0x628438))
    # (Line 129) CreateUnitWithProperties(1, unitType, locID+1, $P7, UnitProperty(invincible=true));
    DoActions(CreateUnitWithProperties(1, unitType, locID + 1, 6, UnitProperty(invincible=True)))
    # (Line 132) const changedSpeed = TOPSPEED * speed/100 + BOTSPEED;
    changedSpeed = TOPSPEED * speed // 100 + BOTSPEED
    # (Line 133) const vx, vy = lengthdir(changedSpeed, angle);
    vx, vy = List2Assignable([f_lengthdir(changedSpeed, angle)])
    # (Line 134) physics.setVxy(unitEpd, vx, vy);
    physics.f_setVxy(unitEpd, vx, vy)
    # (Line 135) push(unitEpd);
    f_push(unitEpd)
    # (Line 136) }
    # (Line 138) function shoot(unitEpd)

# (Line 139) {
@EUDFunc
def f_shoot(unitEpd):
    # (Line 140) const x, y = utilEud.getUnitXY(unitEpd);
    x, y = List2Assignable([utilEud.f_getUnitXY(unitEpd)])
    # (Line 142) const speed = utilEud.getKillCount(unitEpd); //killcount
    speed = utilEud.f_getKillCount(unitEpd)
    # (Line 143) const angle = tankAim.getAngle(unitEpd);
    angle = tankAim.f_getAngle(unitEpd)
    # (Line 145) const targetPlayer = utilEud.getPlayerID(unitEpd);
    targetPlayer = utilEud.f_getPlayerID(unitEpd)
    # (Line 146) const unitType = utilEud.getUnitType(unitEpd);
    unitType = utilEud.f_getUnitType(unitEpd)
    # (Line 147) const bullet = getBullet(unitType, utilEud.getDeath(targetPlayer, header.bulletQ));
    bullet = f_getBullet(unitType, utilEud.f_getDeath(targetPlayer, header.bulletQ))
    # (Line 149) emplayer.shootEffectMusic(bullet);
    emplayer.f_shootEffectMusic(bullet)
    # (Line 151) var dx, dy = lengthdir(32, angle);
    dx, dy = _MVAR([f_lengthdir(32, angle)])
    # (Line 152) makeBullet(bullet, x+dx, y+dy, angle, speed);
    f_makeBullet(bullet, x + dx, y + dy, angle, speed)
    # (Line 153) if(bullet == header.List[8*3+2]) // tankLu 2
    if EUDIf()(bullet == header.List[8 * 3 + 2]):
        # (Line 154) {
        # (Line 155) for (var i=1; i<4; i++)
        i = EUDVariable()
        i << (1)
        if EUDWhile()(i >= 4, neg=True):
            def _t3():
                i.__iadd__(1)
            # (Line 156) {
            # (Line 157) dx, dy = lengthdir(32 + i*8, angle);
            _SV([dx, dy], [f_lengthdir(32 + i * 8, angle)])
            # (Line 158) makeBullet(bullet, x+dx, y+dy, angle, speed);
            f_makeBullet(bullet, x + dx, y + dy, angle, speed)
            # (Line 159) }
            # (Line 160) }
            EUDSetContinuePoint()
            _t3()
        EUDEndWhile()
        # (Line 161) }
    EUDEndIf()
    # (Line 162) function boom(unitType, locID)

# (Line 163) {
@EUDFunc
def f_boom(unitType, locID):
    # (Line 164) const bombUnit = 50;
    bombUnit = 50
    # (Line 166) const effectUnit = tankWeapon.setWeapon(unitType);
    effectUnit = tankWeapon.f_setWeapon(unitType)
    # (Line 168) const unitEpd = epdread_epd(EPD(0x628438));
    unitEpd = f_epdread_epd(EPD(0x628438))
    # (Line 170) CreateUnitWithProperties(1, bombUnit, locID+1, $P7, UnitProperty(invincible=true));
    DoActions(CreateUnitWithProperties(1, bombUnit, locID + 1, 6, UnitProperty(invincible=True)))
    # (Line 171) const unitPos = dwread_epd(unitEpd + 0x28/4);
    unitPos = f_dwread_epd(unitEpd + 0x28 // 4)
    # (Line 173) dwwrite_epd(unitEpd + 0x58/4, unitPos);
    f_dwwrite_epd(unitEpd + 0x58 // 4, unitPos)
    # (Line 174) utilEud.setOrderID(unitEpd, 135);
    utilEud.f_setOrderID(unitEpd, 135)
    # (Line 175) if(effectUnit != -1)
    if EUDIf()(effectUnit == -1, neg=True):
        # (Line 176) {
        # (Line 177) const effectEpd = epdread_epd(EPD(0x628438));
        effectEpd = f_epdread_epd(EPD(0x628438))
        # (Line 178) CreateUnitWithProperties(1, effectUnit, locID+1, $P7, UnitProperty(invincible=true));
        DoActions(CreateUnitWithProperties(1, effectUnit, locID + 1, 6, UnitProperty(invincible=True)))
        # (Line 179) dwwrite_epd(effectEpd + 0x58/4, unitPos);
        f_dwwrite_epd(effectEpd + 0x58 // 4, unitPos)
        # (Line 180) utilEud.setOrderID(effectEpd, 135);
        utilEud.f_setOrderID(effectEpd, 135)
        # (Line 181) }
        # (Line 182) }
    EUDEndIf()
    # (Line 184) function getBullet(unitType, num)

# (Line 185) {
@EUDFunc
def f_getBullet(unitType, num):
    # (Line 186) for (var i = 0; i<header.ListNum; i++)
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= header.ListNum, neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 187) {
        # (Line 188) const index = i*3;
        index = i * 3
        # (Line 189) if(header.List[index] == unitType)
        if EUDIf()(header.List[index] == unitType):
            # (Line 190) if(num) return header.List[index+1];
            if EUDIf()(num):
                EUDReturn(header.List[index + 1])
                # (Line 191) else return header.List[index+2];
            if EUDElse()():
                EUDReturn(header.List[index + 2])
                # (Line 192) }
            EUDEndIf()
        EUDEndIf()
        # (Line 193) }
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
