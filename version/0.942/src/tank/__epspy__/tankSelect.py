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
# (Line 2) import header;
import header
# (Line 3) import customText3 as ct;
import customText3 as ct
# (Line 7) function showTankInfo(unitType, targetPlayer);
# (Line 8) function isSelecting()
# (Line 9) {
@EUDFunc
def f_isSelecting():
    # (Line 10) if(Bring($Force1, AtLeast, 1, header.Flag, $L('preTurn')+1)
    _t1 = EUDIf()
    # (Line 11) || Bring($Force3, AtLeast, 1, header.Flag, $L('preTurn')+1))
    if _t1(EUDSCOr()(Bring(18, AtLeast, 1, header.Flag, GetLocationIndex('preTurn') + 1))(Bring(20, AtLeast, 1, header.Flag, GetLocationIndex('preTurn') + 1))()):
        # (Line 12) return 1;
        EUDReturn(1)
        # (Line 13) else
        # (Line 14) return 0;
    if EUDElse()():
        EUDReturn(0)
        # (Line 15) }
    EUDEndIf()
    # (Line 17) function getSelection(targetPlayer)

# (Line 18) {
@EUDFunc
def f_getSelection(targetPlayer):
    # (Line 19) const selectedUnitEpd = dwread_epd_safe(EPD(0x6284E8 + 48*targetPlayer));
    selectedUnitEpd = f_dwread_epd_safe(EPD(0x6284E8 + 48 * targetPlayer))
    # (Line 20) if(selectedUnitEpd != 0)
    if EUDIf()(selectedUnitEpd == 0, neg=True):
        # (Line 21) {
        # (Line 22) const unitType = utilEud.getUnitType(EPD(selectedUnitEpd));
        unitType = utilEud.f_getUnitType(EPD(selectedUnitEpd))
        # (Line 23) return unitType;
        EUDReturn(unitType)
        # (Line 24) }
        # (Line 25) else
        # (Line 26) return 0;
    if EUDElse()():
        EUDReturn(0)
        # (Line 27) }
    EUDEndIf()
    # (Line 30) function isListed(unitType)

# (Line 31) {
@EUDFunc
def f_isListed(unitType):
    # (Line 32) for(var i=0; i<10; i++)
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= 10, neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 33) {
        # (Line 34) if(header.List[i*3] == unitType) return 1;
        if EUDIf()(header.List[i * 3] == unitType):
            EUDReturn(1)
            # (Line 35) }
        EUDEndIf()
        # (Line 36) return 0;
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    EUDReturn(0)
    # (Line 37) }
    # (Line 38) function selectScreen()

# (Line 39) {
@EUDFunc
def f_selectScreen():
    # (Line 40) EUDPlayerLoop()();
    EUDPlayerLoop()()
    # (Line 41) const i = getcurpl();
    i = f_getcurpl()
    # (Line 42) if(i<6)
    if EUDIf()(i >= 6, neg=True):
        # (Line 43) {
        # (Line 45) if(Command(i, Exactly, 1, header.Flag))
        if EUDIf()(Command(i, Exactly, 1, header.Flag)):
            # (Line 46) {
            # (Line 47) const key = utilEud.getDeath(i, 0);
            key = utilEud.f_getDeath(i, 0)
            # (Line 48) CenterView($L('select')+1);
            DoActions(CenterView(GetLocationIndex('select') + 1))
            # (Line 49) const unitType = showTankInfo(getSelection(i), i);
            unitType = f_showTankInfo(f_getSelection(i), i)
            # (Line 51) if(key == 8 && isListed(unitType)) // L
            if EUDIf()(EUDSCAnd()(key == 8)(f_isListed(unitType))()):
                # (Line 52) {// confirm
                # (Line 53) RemoveUnit(header.Flag, i);
                DoActions(RemoveUnit(header.Flag, i))
                # (Line 55) SetDeaths(i, SetTo, unitType, header.tankType);
                DoActions(SetDeaths(i, SetTo, unitType, header.tankType))
                # (Line 56) }
                # (Line 58) }
            EUDEndIf()
            # (Line 59) }
        EUDEndIf()
        # (Line 60) EUDEndPlayerLoop();
    EUDEndIf()
    EUDEndPlayerLoop()
    # (Line 61) }
    # (Line 63) function showTankInfo(unitType, targetPlayer)

# (Line 64) {
@EUDFunc
def f_showTankInfo(unitType, targetPlayer):
    # (Line 67) if (unitType == 0)
    if EUDIf()(unitType == 0):
        # (Line 68) {
        # (Line 69) const chatPtr = dwread_epd(EPD(0x640B58));
        chatPtr = f_dwread_epd(EPD(0x640B58))
        # (Line 70) ct.printP(targetPlayer, ""); // ct.cp는 모두에게 출력
        ct.f_printP(targetPlayer, "")
        # (Line 71) ct.printP(targetPlayer, "\x13원하는 탱크를 마우스로 클릭해주세요");
        ct.f_printP(targetPlayer, "\x13원하는 탱크를 마우스로 클릭해주세요")
        # (Line 72) dwwrite_epd(EPD(0x640B58), chatPtr);
        f_dwwrite_epd(EPD(0x640B58), chatPtr)
        # (Line 73) }
        # (Line 74) else
        # (Line 75) {
    if EUDElse()():
        # (Line 76) const chatPtr = dwread_epd(EPD(0x640B58));
        chatPtr = f_dwread_epd(EPD(0x640B58))
        # (Line 78) if(unitType == header.tankDr)
        if EUDIf()(unitType == header.tankDr):
            # (Line 79) {
            # (Line 80) ct.printP(targetPlayer, ""); // ct.cp는 모두에게 출력
            ct.f_printP(targetPlayer, "")
            # (Line 81) ct.printP(targetPlayer, "\x13[ \x07빡탱\x01 ]");
            ct.f_printP(targetPlayer, "\x13[ \x07빡탱\x01 ]")
            # (Line 82) ct.printP(targetPlayer, "\x13일반탄: 사람 잘 죽임");
            ct.f_printP(targetPlayer, "\x13일반탄: 사람 잘 죽임")
            # (Line 83) ct.printP(targetPlayer, "\x13특수탄: 지형도 잘 부숨");
            ct.f_printP(targetPlayer, "\x13특수탄: 지형도 잘 부숨")
            # (Line 84) ct.printP(targetPlayer, "\x03특징: \x01길 못찾음");
            ct.f_printP(targetPlayer, "\x03특징: \x01길 못찾음")
            # (Line 85) }
            # (Line 87) else if(unitType == header.tankRe)
        if EUDElseIf()(unitType == header.tankRe):
            # (Line 88) {
            # (Line 89) ct.printP(targetPlayer, ""); // ct.cp는 모두에게 출력
            ct.f_printP(targetPlayer, "")
            # (Line 90) ct.printP(targetPlayer, "\x13[ \x07립탱\x01 ]");
            ct.f_printP(targetPlayer, "\x13[ \x07립탱\x01 ]")
            # (Line 91) ct.printP(targetPlayer, "\x13일반탄: 사람 좀 죽임");
            ct.f_printP(targetPlayer, "\x13일반탄: 사람 좀 죽임")
            # (Line 92) ct.printP(targetPlayer, "\x13특수탄: 지형은 잘 부숨");
            ct.f_printP(targetPlayer, "\x13특수탄: 지형은 잘 부숨")
            # (Line 93) ct.printP(targetPlayer, "\x03특징: \x01기어다님");
            ct.f_printP(targetPlayer, "\x03특징: \x01기어다님")
            # (Line 94) }
            # (Line 96) else if(unitType == header.tankUr)
        if EUDElseIf()(unitType == header.tankUr):
            # (Line 97) {
            # (Line 98) ct.printP(targetPlayer, ""); // ct.cp는 모두에게 출력
            ct.f_printP(targetPlayer, "")
            # (Line 99) ct.printP(targetPlayer, "\x13[ \x07곰탱\x01 ]");
            ct.f_printP(targetPlayer, "\x13[ \x07곰탱\x01 ]")
            # (Line 100) ct.printP(targetPlayer, "\x13일반탄: 사람 좀 죽임");
            ct.f_printP(targetPlayer, "\x13일반탄: 사람 좀 죽임")
            # (Line 101) ct.printP(targetPlayer, "\x13특수탄: 지랄 발광함");
            ct.f_printP(targetPlayer, "\x13특수탄: 지랄 발광함")
            # (Line 102) ct.printP(targetPlayer, "\x03특징: \x01귀여움");
            ct.f_printP(targetPlayer, "\x03특징: \x01귀여움")
            # (Line 103) }
            # (Line 105) else if(unitType == header.tankDA)
        if EUDElseIf()(unitType == header.tankDA):
            # (Line 106) {
            # (Line 107) ct.printP(targetPlayer, ""); // ct.cp는 모두에게 출력
            ct.f_printP(targetPlayer, "")
            # (Line 108) ct.printP(targetPlayer, "\x13[ \x07빨탱\x01 ]");
            ct.f_printP(targetPlayer, "\x13[ \x07빨탱\x01 ]")
            # (Line 109) ct.printP(targetPlayer, "\x13일반탄: 마엘스톰 검");
            ct.f_printP(targetPlayer, "\x13일반탄: 마엘스톰 검")
            # (Line 110) ct.printP(targetPlayer, "\x13특수탄: 지형 좀 부숨");
            ct.f_printP(targetPlayer, "\x13특수탄: 지형 좀 부숨")
            # (Line 111) ct.printP(targetPlayer, "\x03참고: \x01난 큰게 좋더라");
            ct.f_printP(targetPlayer, "\x03참고: \x01난 큰게 좋더라")
            # (Line 112) }
            # (Line 114) else if(unitType == header.tankDe)
        if EUDElseIf()(unitType == header.tankDe):
            # (Line 115) {
            # (Line 116) ct.printP(targetPlayer, ""); // ct.cp는 모두에게 출력
            ct.f_printP(targetPlayer, "")
            # (Line 117) ct.printP(targetPlayer, "\x13[ \x07딥탱\x01 ]");
            ct.f_printP(targetPlayer, "\x13[ \x07딥탱\x01 ]")
            # (Line 118) ct.printP(targetPlayer, "\x13일반탄: 사람 확 죽임");
            ct.f_printP(targetPlayer, "\x13일반탄: 사람 확 죽임")
            # (Line 119) ct.printP(targetPlayer, "\x13특수탄: 지형 꽤 부숨");
            ct.f_printP(targetPlayer, "\x13특수탄: 지형 꽤 부숨")
            # (Line 120) ct.printP(targetPlayer, "\x03문제: \x01디바가 울면?");
            ct.f_printP(targetPlayer, "\x03문제: \x01디바가 울면?")
            # (Line 121) }
            # (Line 123) else if(unitType == header.tankST)
        if EUDElseIf()(unitType == header.tankST):
            # (Line 124) {
            # (Line 125) ct.printP(targetPlayer, ""); // ct.cp는 모두에게 출력
            ct.f_printP(targetPlayer, "")
            # (Line 126) ct.printP(targetPlayer, "\x13[ \x07시즈탱\x01 ]");
            ct.f_printP(targetPlayer, "\x13[ \x07시즈탱\x01 ]")
            # (Line 127) ct.printP(targetPlayer, "\x13일반탄: 쾅");
            ct.f_printP(targetPlayer, "\x13일반탄: 쾅")
            # (Line 128) ct.printP(targetPlayer, "\x13특수탄: 콰쾅");
            ct.f_printP(targetPlayer, "\x13특수탄: 콰쾅")
            # (Line 129) ct.printP(targetPlayer, "\x03특징: \x01근데 시즈 못함");
            ct.f_printP(targetPlayer, "\x03특징: \x01근데 시즈 못함")
            # (Line 130) }
            # (Line 132) else if(unitType == header.tankGo)
        if EUDElseIf()(unitType == header.tankGo):
            # (Line 133) {
            # (Line 134) ct.printP(targetPlayer, ""); // ct.cp는 모두에게 출력
            ct.f_printP(targetPlayer, "")
            # (Line 135) ct.printP(targetPlayer, "\x13[ \x07골탱\x01 ]");
            ct.f_printP(targetPlayer, "\x13[ \x07골탱\x01 ]")
            # (Line 136) ct.printP(targetPlayer, "\x13일반탄: 준 저격탄");
            ct.f_printP(targetPlayer, "\x13일반탄: 준 저격탄")
            # (Line 137) ct.printP(targetPlayer, "\x13특수탄: 지형만 부숨");
            ct.f_printP(targetPlayer, "\x13특수탄: 지형만 부숨")
            # (Line 138) ct.printP(targetPlayer, "\x03특징: \x01길 못찾음");
            ct.f_printP(targetPlayer, "\x03특징: \x01길 못찾음")
            # (Line 139) }
            # (Line 141) else if(unitType == header.tankVu)
        if EUDElseIf()(unitType == header.tankVu):
            # (Line 142) {
            # (Line 143) ct.printP(targetPlayer, ""); // ct.cp는 모두에게 출력
            ct.f_printP(targetPlayer, "")
            # (Line 144) ct.printP(targetPlayer, "\x13[ \x07벌탱\x01 ]");
            ct.f_printP(targetPlayer, "\x13[ \x07벌탱\x01 ]")
            # (Line 145) ct.printP(targetPlayer, "\x13일반탄: 마인 야캐요");
            ct.f_printP(targetPlayer, "\x13일반탄: 마인 야캐요")
            # (Line 146) ct.printP(targetPlayer, "\x13특수탄: 지형 ㄹㅇ 잘 부숨");
            ct.f_printP(targetPlayer, "\x13특수탄: 지형 ㄹㅇ 잘 부숨")
            # (Line 147) ct.printP(targetPlayer, "\x03특징: \x01마인 시벌탱");
            ct.f_printP(targetPlayer, "\x03특징: \x01마인 시벌탱")
            # (Line 148) }
            # (Line 150) else if(unitType == header.tankLu)
        if EUDElseIf()(unitType == header.tankLu):
            # (Line 151) {
            # (Line 152) ct.printP(targetPlayer, ""); // ct.cp는 모두에게 출력
            ct.f_printP(targetPlayer, "")
            # (Line 153) ct.printP(targetPlayer, "\x13[ \x07럴탱\x01 ]");
            ct.f_printP(targetPlayer, "\x13[ \x07럴탱\x01 ]")
            # (Line 154) ct.printP(targetPlayer, "\x13일반탄: 탄이 다섯개!");
            ct.f_printP(targetPlayer, "\x13일반탄: 탄이 다섯개!")
            # (Line 155) ct.printP(targetPlayer, "\x13특수탄: 맞으면 느려짐");
            ct.f_printP(targetPlayer, "\x13특수탄: 맞으면 느려짐")
            # (Line 156) ct.printP(targetPlayer, "\x03특징: \x01숨어있음");
            ct.f_printP(targetPlayer, "\x03특징: \x01숨어있음")
            # (Line 157) }
            # (Line 159) else if(unitType == header.tankUl)
        if EUDElseIf()(unitType == header.tankUl):
            # (Line 160) {
            # (Line 161) ct.printP(targetPlayer, ""); // ct.cp는 모두에게 출력
            ct.f_printP(targetPlayer, "")
            # (Line 162) ct.printP(targetPlayer, "\x13[ \x07울탱\x01 ]");
            ct.f_printP(targetPlayer, "\x13[ \x07울탱\x01 ]")
            # (Line 163) ct.printP(targetPlayer, "\x13일반탄: 사람 죽임?");
            ct.f_printP(targetPlayer, "\x13일반탄: 사람 죽임?")
            # (Line 164) ct.printP(targetPlayer, "\x13특수탄: 고춧가루");
            ct.f_printP(targetPlayer, "\x13특수탄: 고춧가루")
            # (Line 165) ct.printP(targetPlayer, "\x03상식: \x01돼지는 하늘을 못본다");
            ct.f_printP(targetPlayer, "\x03상식: \x01돼지는 하늘을 못본다")
            # (Line 166) }
            # (Line 167) else
            # (Line 168) {
        if EUDElse()():
            # (Line 169) ct.printP(targetPlayer, ""); // ct.cp는 모두에게 출력
            ct.f_printP(targetPlayer, "")
            # (Line 170) ct.printP(targetPlayer, "\x13유닛을 마우스로 선택해주세요");
            ct.f_printP(targetPlayer, "\x13유닛을 마우스로 선택해주세요")
            # (Line 171) }
            # (Line 172) ct.printP(targetPlayer, "");
        EUDEndIf()
        ct.f_printP(targetPlayer, "")
        # (Line 173) ct.printP(targetPlayer, "\x13\x07[ L ] : \x01선택");
        ct.f_printP(targetPlayer, "\x13\x07[ L ] : \x01선택")
        # (Line 174) dwwrite_epd(EPD(0x640B58), chatPtr);
        f_dwwrite_epd(EPD(0x640B58), chatPtr)
        # (Line 175) }
        # (Line 176) return unitType;
    EUDEndIf()
    EUDReturn(unitType)
    # (Line 177) }
