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

# (Line 1) import util.utilEud;
from util import utilEud
# (Line 3) function getVxy(unitEpd)
# (Line 4) {
@EUDFunc
def f_getVxy(unitEpd):
    # (Line 5) const vx = dwread_epd(unitEpd + 0xF8/4);
    vx = f_dwread_epd(unitEpd + 0xF8 // 4)
    # (Line 6) const vy = dwread_epd(unitEpd + 0xFC/4);
    vy = f_dwread_epd(unitEpd + 0xFC // 4)
    # (Line 8) return vx, vy;
    EUDReturn(vx, vy)
    # (Line 9) }
    # (Line 11) function setVxy(unitEpd, vx, vy)

# (Line 12) {
@EUDFunc
def f_setVxy(unitEpd, vx, vy):
    # (Line 13) dwwrite_epd(unitEpd + 0xF8/4, vx);
    f_dwwrite_epd(unitEpd + 0xF8 // 4, vx)
    # (Line 14) dwwrite_epd(unitEpd + 0xFC/4, vy);
    f_dwwrite_epd(unitEpd + 0xFC // 4, vy)
    # (Line 15) }
    # (Line 17) function renderUnit(unitEpd, option)

# (Line 18) {// move unit
@EUDFunc
def f_renderUnit(unitEpd, option):
    # (Line 19) const vx, vy = getVxy(unitEpd);
    vx, vy = List2Assignable([f_getVxy(unitEpd)])
    # (Line 20) if(vx != 0 || vy != 0)
    if EUDIf()(EUDSCOr()(vx == 0, neg=True)(vy == 0, neg=True)()):
        # (Line 21) {
        # (Line 22) const unitX, unitY = utilEud.getUnitXY(unitEpd);
        unitX, unitY = List2Assignable([utilEud.f_getUnitXY(unitEpd)])
        # (Line 23) const unitPos = (unitX + vx) + (unitY + vy)*65536;
        unitPos = (unitX + vx) + (unitY + vy) * 65536
        # (Line 24) utilEud.moveLocationXY($L('locPre'), unitX, unitY);
        utilEud.f_moveLocationXY(GetLocationIndex('locPre'), unitX, unitY)
        # (Line 25) utilEud.moveLocationXY($L('locDst'), unitX + vx, unitY + vy);
        utilEud.f_moveLocationXY(GetLocationIndex('locDst'), unitX + vx, unitY + vy)
        # (Line 26) MoveUnit(1, utilEud.getUnitType(unitEpd), utilEud.getPlayerID(unitEpd), $L('locPre')+1, $L('locDst')+1);
        DoActions(MoveUnit(1, utilEud.f_getUnitType(unitEpd), utilEud.f_getPlayerID(unitEpd), GetLocationIndex('locPre') + 1, GetLocationIndex('locDst') + 1))
        # (Line 27) if(option)
        if EUDIf()(option):
            # (Line 28) {
            # (Line 30) bwrite_epd(unitEpd + 0x021 / 4,  0x021 % 4, (atan2(vy, vx)*256/360 + 64)%256);
            f_bwrite_epd(unitEpd + 0x021 // 4, 0x021 % 4, (f_atan2(vy, vx) * 256 // 360 + 64) % 256)
            # (Line 31) }
            # (Line 33) }
        EUDEndIf()
        # (Line 34) }
    EUDEndIf()
