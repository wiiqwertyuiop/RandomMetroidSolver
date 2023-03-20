from utils.parameters import infinity
import copy
from rando.RoomSpriteInfo import RoomSpriteInfo

class Location:
    graph_slots = (
        'distance', 'accessPoint', 'difficulty', 'path',
        'pathDifficulty', 'locDifficulty' )
    
    rando_slots = (
        'restricted', )

    solver_slots = (
        'itemName', 'comeBack', 'areaWeight' )

    __slots__ = graph_slots + rando_slots + solver_slots

    def __init__(
            self, distance=None, accessPoint=None,
            difficulty=None, path=None, pathDifficulty=None,
            locDifficulty=None, restricted=None, itemName=None,
            itemType=None, comeBack=None, areaWeight=None):
        self.distance = distance
        self.accessPoint = accessPoint
        self.difficulty = difficulty
        self.path = path
        self.pathDifficulty = pathDifficulty
        self.locDifficulty = locDifficulty
        self.restricted = restricted
        self.itemName = itemName
        self.itemType = itemType
        self.comeBack = comeBack
        self.areaWeight = areaWeight

    def isMajor(self):
        return self._isMajor

    def isChozo(self):
        return self._isChozo

    def isMinor(self):
        return self._isMinor

    def isBoss(self):
        return self._isBoss

    def isScavenger(self):
        return self._isScavenger

    def isClass(self, _class):
        return _class in self.Class

    def setClass(self, _class):
        self.Class = _class
        self._isChozo = 'Chozo' in _class
        self._isMajor = 'Major' in _class
        self._isMinor = 'Minor' in _class
        self._isBoss = 'Boss' in _class
        self._isScavenger = 'Scavenger' in _class

    def evalPostAvailable(self, smbm):
        if self.difficulty.bool == True and self.PostAvailable is not None:
            smbm.addItem(self.itemName)
            postAvailable = self.PostAvailable(smbm)
            smbm.removeItem(self.itemName)

            self.difficulty = self.difficulty & postAvailable
            if self.locDifficulty is not None:
                self.locDifficulty = self.locDifficulty & postAvailable

    def evalComeBack(self, smbm, areaGraph, ap):
        if self.difficulty.bool == True:
            # check if we can come back to given ap from the location
            self.comeBack = areaGraph.canAccess(smbm, self.accessPoint, ap, infinity, self.itemName)

    def json(self):
        # to return after plando rando
        ret = {'Name': self.Name, 'accessPoint': self.accessPoint}
        if self.difficulty is not None:
            ret['difficulty'] = self.difficulty.json()
        return ret

    def __repr__(self):
        return "Location({}: {})".format(self.Name,
            '. '.join(
                (repr(getattr(self, slot)) for slot in Location.__slots__ if getattr(self, slot) is not None)))

    def __copy__(self):
        d = self.difficulty
        difficulty = copy.copy(d) if d is not None else None
        ret = type(self)(
            self.distance, self.accessPoint, difficulty, self.path,
            self.pathDifficulty, self.locDifficulty, self.restricted,
            self.itemName, self.itemType, self.comeBack,
            self.areaWeight)
        ret.AccessFrom = self.AccessFrom
        ret.Available = self.Available
        ret.PostAvailable = self.PostAvailable
        ret.setClass(self.Class)

        return ret

    def __eq__(self, other):
        return self.Name == other.Name

def define_location(
        Area, GraphArea, SolveArea, Name, Class, CanHidden, Address, Id,
        Visibility, Room, VanillaItemType=None, BossItemType=None, AccessFrom=None, Available=None, PostAvailable=None, HUD=None, NearbyRoomsWithSprites=[]):
    name = Name.replace(' ', '').replace(',', '') + 'Location'
    subclass = type(name, (Location,), {
        'Area': Area,
        'GraphArea': GraphArea,
        'SolveArea': SolveArea,
        'Name': Name,
        'Class': Class,
        'CanHidden': CanHidden,
        'Address': Address,
        'Id': Id,
        'Visibility': Visibility,
        'Room': Room,
        'VanillaItemType': VanillaItemType,
        'BossItemType': BossItemType,
        'HUD': HUD,
        'AccessFrom': AccessFrom,
        'Available': Available,
        'PostAvailable': PostAvailable,
        'NearbyRoomsWithSprites': NearbyRoomsWithSprites,
        '_isMajor': 'Major' in Class,
        '_isChozo': 'Chozo' in Class,
        '_isMinor': 'Minor' in Class,
        '_isBoss': 'Boss' in Class,
        '_isScavenger': 'Scavenger' in Class
    })
    return subclass()


# all the items locations with the prerequisites to access them
locationsDict = {
    # MAJORS
    "Energy Tank, Gauntlet":
    define_location(
        Area="Crateria",
        GraphArea="Crateria",
        SolveArea="Crateria Gauntlet",
        Name="Energy Tank, Gauntlet",
        Class=["Major", "Chozo"],
        CanHidden=False,
        Address=0x78264,
        Id=0x5,
        Visibility="Visible",
        Room='Gauntlet Energy Tank Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A01FD, 0x1089F2),  # Pop	CR	7965B [Standard]
            RoomSpriteInfo(0x1A00A1, 0x10847A),  # Pop	CR	792B3 [Standard]
        ]
    ),
    "Bomb":
    define_location(
        Area="Crateria",
        GraphArea="Crateria",
        SolveArea="Crateria Bombs",
        Name="Bomb",
        Address=0x78404,
        Id=0x7,
        Class=["Major", "Chozo", "Scavenger"],
        CanHidden=False,
        Visibility="Chozo",
        Room='Bomb Torizo Room',
        VanillaItemType='Bomb',
        HUD=1,
    ),
    "Energy Tank, Terminator":
    define_location(
        Area="Crateria",
        GraphArea="Crateria",
        SolveArea="Crateria Terminator",
        Name="Energy Tank, Terminator",
        Class=["Major"],
        CanHidden=False,
        Address=0x78432,
        Id=0x8,
        Visibility="Visible",
        Room='Terminator Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0031, 0x108108),  # Pop	CR	7990D [Standard]
            RoomSpriteInfo(0x1A00C1, 0x108500),  # Pop	CR	799BD [Standard]
            RoomSpriteInfo(0x1A0271, 0x108BCA),  # Pop	CR	79969 [Standard]
        ]
    ),
    "Reserve Tank, Brinstar":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Green Brinstar Reserve",
        Name="Reserve Tank, Brinstar",
        Class=["Major", "Chozo"],
        CanHidden=False,
        Address=0x7852C,
        Id=0x11,
        Visibility="Chozo",
        Room='Brinstar Reserve Tank Room',
    ),
    "Charge Beam":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Pink Brinstar",
        Name="Charge Beam",
        Class=["Major", "Chozo", "Scavenger"],
        CanHidden=False,
        Address=0x78614,
        Id=0x17,
        Visibility="Chozo",
        Room='Big Pink',
        VanillaItemType='Charge',
        HUD=2,
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0429, 0x10953E),  # Pop	BR	79D19 [Standard]
            RoomSpriteInfo(0x1A05B9, 0x109D5C),  # Pop	BR	79CB3 [Standard]
            RoomSpriteInfo(0x1A02FB, 0x108FC5),  # Pop	BR	79D9C [Standard]
            RoomSpriteInfo(0x1A04F7, 0x1097FB),  # Pop	BR	7A130 [Standard]
        ]
    ),
    "Morphing Ball":
    define_location(
        Area="Brinstar",
        GraphArea="Crateria",
        SolveArea="Blue Brinstar",
        Name="Morphing Ball",
        Class=["Major", "Chozo", "Scavenger"],
        CanHidden=False,
        Address=0x786DE,
        Id=0x1a,
        Visibility="Visible",
        Room='Morph Ball Room',
        VanillaItemType='Morph',
        HUD=0,
    ),
    "Energy Tank, Brinstar Ceiling":
    define_location(
        Area="Brinstar",
        GraphArea="Crateria",
        SolveArea="Blue Brinstar",
        Name="Energy Tank, Brinstar Ceiling",
        Class=["Major"],
        CanHidden=False,
        Address=0x7879E,
        Id=0x1d,
        Visibility="Hidden",
        Room='Blue Brinstar Energy Tank Room',
    ),
    "Energy Tank, Etecoons":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Green Brinstar",
        Name="Energy Tank, Etecoons",
        Class=["Major"],
        CanHidden=True,
        Address=0x787C2,
        Id=0x1e,
        Visibility="Visible",
        Room='Etecoon Energy Tank Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A04E5, 0x109778),  # Pop	BR	7A011 [Standard]
        ]
    ),
    "Energy Tank, Waterway":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Pink Brinstar",
        Name="Energy Tank, Waterway",
        Class=["Major"],
        CanHidden=True,
        Address=0x787FA,
        Id=0x21,
        Visibility="Visible",
        Room='Waterway Energy Tank Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0361, 0x10911A),  # Pop	BR	7A0D2 [Standard]
        ]
    ),
    "Energy Tank, Brinstar Gate":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Pink Brinstar",
        Name="Energy Tank, Brinstar Gate",
        Class=["Major"],
        CanHidden=True,
        Address=0x78824,
        Id=0x23,
        Visibility="Visible",
        Room='Hopper Energy Tank Room',
    ),
    "X-Ray Scope":
    define_location(
        Area="Brinstar",
        GraphArea="RedBrinstar",
        SolveArea="Red Brinstar",
        Name="X-Ray Scope",
        Class=["Major", "Chozo", "Scavenger"],
        CanHidden=False,
        Address=0x78876,
        Id=0x26,
        Visibility="Chozo",
        Room='X-Ray Scope Room',
        VanillaItemType='XRayScope',
        HUD=10,
    ),
    "Spazer":
    define_location(
        Area="Brinstar",
        GraphArea="RedBrinstar",
        SolveArea="Red Brinstar",
        Name="Spazer",
        Class=["Major", "Chozo", "Scavenger"],
        CanHidden=False,
        Address=0x7896E,
        Id=0x2a,
        Visibility="Chozo",
        Room='Spazer Room',
        VanillaItemType='Spazer',
        HUD=3,
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A03F1, 0x109452),  # Pop	BR	7A253 [Standard]
            RoomSpriteInfo(0x1A057F, 0x109B13),  # Pop	BR	7A293 [Standard]
            RoomSpriteInfo(0x1A0671, 0x10A110),  # Pop	BR	7A3DD [Standard]
            RoomSpriteInfo(0x1A0449, 0x1095E4),  # Pop	BR	7A408 [Standard]
        ]
    ),
    "Energy Tank, Kraid":
    define_location(
        Area="Brinstar",
        GraphArea="Kraid",
        SolveArea="Kraid",
        Name="Energy Tank, Kraid",
        Class=["Major"],
        CanHidden=False,
        Address=0x7899C,
        Id=0x2b,
        Visibility="Hidden",
        Room='Warehouse Energy Tank Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A050D, 0x10988E),  # Pop	BR	7A4B1 [Standard]
        ]
    ),
    "Kraid":
    define_location(
        Area="Brinstar",
        GraphArea="Kraid",
        SolveArea="Kraid Boss",
        Name="Kraid",
        Class=["Boss"],
        CanHidden=False,
        Address=0xB055B055,
        Id=None,
        Visibility="Hidden",
        Room='Kraid Room',
        BossItemType="Kraid"
    ),
    "Varia Suit":
    define_location(
        Area="Brinstar",
        GraphArea="Kraid",
        SolveArea="Kraid Boss",
        Name="Varia Suit",
        Class=["Major", "Chozo", "Scavenger"],
        CanHidden=False,
        Address=0x78ACA,
        Id=0x30,
        Visibility="Chozo",
        Room='Varia Suit Room',
        VanillaItemType='Varia',
        HUD=4,
    ),
    "Ice Beam":
    define_location(
        Area="Norfair",
        GraphArea="Norfair",
        SolveArea="Norfair Ice",
        Name="Ice Beam",
        Class=["Major", "Chozo", "Scavenger"],
        CanHidden=False,
        Address=0x78B24,
        Id=0x32,
        Visibility="Chozo",
        Room='Ice Beam Room',
        VanillaItemType='Ice',
        HUD=6,
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0A5B, 0x10B6AD),  # Pop	NO	7A8B9 [Standard]
            RoomSpriteInfo(0x1A0A01, 0x10B48E),  # Pop	NO	7A865 [Standard]
            RoomSpriteInfo(0x1A09F3, 0x10B45B),  # Pop	NO	7A75D [Standard]
        ]  # 14
    ),
    "Energy Tank, Crocomire":
    define_location(
        Area="Norfair",
        GraphArea="Crocomire",
        SolveArea="Crocomire",
        Name="Energy Tank, Crocomire",
        Class=["Major"],
        CanHidden=True,
        Address=0x78BA4,
        Id=0x34,
        Visibility="Visible",
        Room="Crocomire's Room",
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A07DF, 0x10A7BB),  # Pop	NO	7AA82 [Standard]
            RoomSpriteInfo(0x1A0695, 0x10A1D6),  # Pop	NO	7AB07 [Standard]
        ]
    ),
    "Hi-Jump Boots":
    define_location(
        Area="Norfair",
        GraphArea="Norfair",
        SolveArea="Norfair Entrance",
        Name="Hi-Jump Boots",
        Class=["Major", "Chozo", "Scavenger"],
        CanHidden=False,
        Address=0x78BAC,
        Id=0x35,
        Visibility="Chozo",
        Room='Hi Jump Boots Room',
        VanillaItemType='HiJump',
        HUD=5,
    ),
    "Grapple Beam":
    define_location(
        Area="Norfair",
        GraphArea="Crocomire",
        SolveArea="Crocomire",
        Name="Grapple Beam",
        Class=["Major", "Chozo", "Scavenger"],
        CanHidden=False,
        Address=0x78C36,
        Id=0x3c,
        Visibility="Chozo",
        Room='Grapple Beam Room',
        VanillaItemType='Grapple',
        HUD=9,
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A09B7, 0x10B3BF),  # Pop	NO	7AC00 [Standard]
            RoomSpriteInfo(0x1A0A49, 0x10B67A),  # Pop	NO	7ABD2 [Standard]
        ]
    ),
    "Reserve Tank, Norfair":
    define_location(
        Area="Norfair",
        GraphArea="Norfair",
        SolveArea="Bubble Norfair Reserve",
        Name="Reserve Tank, Norfair",
        Class=["Major"],
        CanHidden=False,
        Address=0x78C3E,
        Id=0x3d,
        Visibility="Chozo",
        Room='Norfair Reserve Tank Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0A37, 0x10B5E7),  # Pop	NO	7AC5A [Standard]
        ]
    ),
    "Speed Booster":
    define_location(
        Area="Norfair",
        GraphArea="Norfair",
        SolveArea="Bubble Norfair Speed",
        Name="Speed Booster",
        Class=["Major", "Chozo", "Scavenger"],
        CanHidden=False,
        Address=0x78C82,
        Id=0x42,
        Visibility="Chozo",
        Room='Speed Booster Room',
        VanillaItemType='SpeedBooster',
        HUD=7,
    ),
    "Wave Beam":
    define_location(
        Area="Norfair",
        GraphArea="Norfair",
        SolveArea="Bubble Norfair Wave",
        Name="Wave Beam",
        Class=["Major", "Chozo", "Scavenger"],
        CanHidden=False,
        Address=0x78CCA,
        Id=0x44,
        Visibility="Chozo",
        Room='Wave Beam Room',
        VanillaItemType='Wave',
        HUD=8,
    ),
    "Ridley":
    define_location(
        Area="LowerNorfair",
        GraphArea="LowerNorfair",
        SolveArea="Ridley Boss",
        Name="Ridley",
        Class=["Boss", "Scavenger"],
        CanHidden=False,
        Address=0xB055B056,
        Id=0xaa,
        Visibility="Hidden",
        Room="Ridley's Room",
        VanillaItemType="Ridley",
        BossItemType="Ridley",
        HUD=16
    ),
    "Energy Tank, Ridley":
    define_location(
        Area="LowerNorfair",
        GraphArea="LowerNorfair",
        SolveArea="Ridley Boss",
        Name="Energy Tank, Ridley",
        Class=["Major", "Chozo"],
        CanHidden=False,
        Address=0x79108,
        Id=0x4e,
        Visibility="Hidden",
        Room='Ridley Tank Room',
    ),
    "Screw Attack":
    define_location(
        Area="LowerNorfair",
        GraphArea="LowerNorfair",
        SolveArea="Lower Norfair Screw Attack",
        Name="Screw Attack",
        Class=["Major", "Chozo", "Scavenger"],
        CanHidden=False,
        Address=0x79110,
        Id=0x4f,
        Visibility="Chozo",
        Room='Screw Attack Room',
        VanillaItemType='ScrewAttack',
        HUD=15,
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A070F, 0x10A48B),  # Pop	NO	7B2DA [Standard]
        ]
    ),
    "Energy Tank, Firefleas":
    define_location(
        Area="LowerNorfair",
        GraphArea="LowerNorfair",
        SolveArea="Lower Norfair After Amphitheater",
        Name="Energy Tank, Firefleas",
        Class=["Major"],
        CanHidden=True,
        Address=0x79184,
        Id=0x50,
        Visibility="Visible",
        Room='Lower Norfair Fireflea Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0871, 0x10AB80),  # Pop	NO	7B6EE [Standard]
            RoomSpriteInfo(0x1A06FD, 0x10A428),  # Pop	NO	7B585 [Standard]
        ]
    ),
    "Reserve Tank, Wrecked Ship":
    define_location(
        Area="WreckedShip",
        GraphArea="WreckedShip",
        SolveArea="WreckedShip Gravity",
        Name="Reserve Tank, Wrecked Ship",
        Class=["Major"],
        CanHidden=False,
        Address=0x7C2E9,
        Id=0x81,
        Visibility="Chozo",
        Room='Bowling Alley',
    ),
    "Energy Tank, Wrecked Ship":
    define_location(
        Area="WreckedShip",
        GraphArea="WreckedShip",
        SolveArea="WreckedShip Back",
        Name="Energy Tank, Wrecked Ship",
        Class=["Major", "Chozo"],
        CanHidden=True,
        Address=0x7C337,
        Id=0x84,
        Visibility="Visible",
        Room='Wrecked Ship Energy Tank Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0B5B, 0x10BC4D),  # Pop	WS	7CC27 [Bosses]
            RoomSpriteInfo(0x1A0BF7, 0x10C1AB),  # Pop	WS	7CBD5 [Standard]
            RoomSpriteInfo(0x1A0CEB, 0x10CB3B),  # Pop	WS	7CBD5 [Bosses]
            RoomSpriteInfo(0x1A0C27, 0x10C1E7),  # Pop	WS	7CC27 [Standard]
        ]
    ),
    "Phantoon":
    define_location(
        Area="WreckedShip",
        GraphArea="WreckedShip",
        SolveArea="Phantoon Boss",
        Name="Phantoon",
        Class=["Boss"],
        CanHidden=False,
        Address=0xB055B057,
        Id=None,
        Visibility="Hidden",
        Room="Phantoon's Room",
        BossItemType="Phantoon"
    ),
    "Right Super, Wrecked Ship":
    define_location(
        Area="WreckedShip",
        GraphArea="WreckedShip",
        SolveArea="WreckedShip Main",
        Name="Right Super, Wrecked Ship",
        Class=["Major", "Chozo"],
        CanHidden=True,
        Address=0x7C365,
        Id=0x86,
        Visibility="Visible",
        Room='Wrecked Ship East Super Room',
    ),
    "Gravity Suit":
    define_location(
        Area="WreckedShip",
        GraphArea="WreckedShip",
        SolveArea="WreckedShip Gravity",
        Name="Gravity Suit",
        Class=["Major", "Scavenger"],
        CanHidden=False,
        Address=0x7C36D,
        Id=0x87,
        Visibility="Chozo",
        Room='Gravity Suit Room',
        VanillaItemType='Gravity',
        HUD=11,
    ),
    "Energy Tank, Mama turtle":
    define_location(
        Area="Maridia",
        GraphArea="WestMaridia",
        SolveArea="Maridia Green",
        Name="Energy Tank, Mama turtle",
        Class=["Major"],
        CanHidden=True,
        Address=0x7C47D,
        Id=0x8a,
        Visibility="Visible",
        Room='Mama Turtle Room',
        # NearbyRoomsWithSprites=[
        #    RoomSpriteInfo(0x1A0EA8, 0x10D5E2),  # Pop	MA	7D055 [Standard]
        # ]
    ),
    "Plasma Beam":
    define_location(
        Area="Maridia",
        GraphArea="EastMaridia",
        SolveArea="Maridia Forgotten Highway",
        Name="Plasma Beam",
        Class=["Major", "Chozo", "Scavenger"],
        CanHidden=False,
        Address=0x7C559,
        Id=0x8f,
        Visibility="Chozo",
        Room='Plasma Room',
        VanillaItemType='Plasma',
        HUD=14,
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0E42, 0x10D3ED),  # Pop	MA	7D2AA [Standard]
            RoomSpriteInfo(0x1A0EFA, 0x10D801),  # Pop	MA	7D27E [Standard]
            RoomSpriteInfo(0x1A0FE6, 0x10DD9B),  # Pop	MA	7D387 [Standard]
            RoomSpriteInfo(0x1A0F22, 0x10D957),  # Pop	MA	7D340 [Standard]
            RoomSpriteInfo(0x1A0F0C, 0x10D864),  # Pop	MA	7D2D9 [Standard]
            RoomSpriteInfo(0x1A0D85, 0x10D006),  # Pop	MA	7D30B [Standard]
            RoomSpriteInfo(0x1A0DE3, 0x10D1BB),  # Pop	MA	7D86E [Standard]
        ]
    ),
    "Reserve Tank, Maridia":
    define_location(
        Area="Maridia",
        GraphArea="EastMaridia",
        SolveArea="Left Sandpit",
        Name="Reserve Tank, Maridia",
        Class=["Major"],
        CanHidden=False,
        Address=0x7C5E3,
        Id=0x91,
        Visibility="Chozo",
        Room='West Sand Hole',
    ),
    "Spring Ball":
    define_location(
        Area="Maridia",
        GraphArea="EastMaridia",
        SolveArea="Maridia Sandpits",
        Name="Spring Ball",
        Class=["Major", "Chozo", "Scavenger"],
        CanHidden=False,
        Address=0x7C6E5,
        Id=0x96,
        Visibility="Chozo",
        Room='Spring Ball Room',
        VanillaItemType='SpringBall',
        HUD=13,
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0FB8, 0x10DCE2),  # Pop	MA	7D69A [Standard]
            RoomSpriteInfo(0x1A0E5E, 0x10D453),  # Pop	MA	7D646 [Standard]
            RoomSpriteInfo(0x1A0F6A, 0x10DAD3),  # Pop	MA	7D4C2 [Standard]
            RoomSpriteInfo(0x1A0F52, 0x10DA3D),  # Pop	MA	7D461 [Standard]
            RoomSpriteInfo(0x1A0EEC, 0x10D7EE),  # Pop	MA	7D252 [Standard]
        ]
    ),
    "Energy Tank, Botwoon":
    define_location(
        Area="Maridia",
        GraphArea="EastMaridia",
        SolveArea="Maridia Pink Top",
        Name="Energy Tank, Botwoon",
        Class=["Major"],
        CanHidden=True,
        Address=0x7C755,
        Id=0x98,
        Visibility="Visible",
        Room='Botwoon Energy Tank Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0DB9, 0x10D112),  # Pop	MA	7D7E4 [Standard]
            RoomSpriteInfo(0x1A0DF1, 0x10D1EE),  # Pop	MA	7D898 [Standard]
            RoomSpriteInfo(0x1A0D53, 0x10CF2D),  # Pop	MA	7D913 [Standard]
            RoomSpriteInfo(0x1A0D97, 0x10D089),  # Pop	MA	7D72A [Standard]
            RoomSpriteInfo(0x1A107A, 0x10DFD9),  # Pop	MA	7D9FE [Standard]
            RoomSpriteInfo(0x1A0FD4, 0x10DD38),  # Pop	MA	7D6FD [Standard]
            RoomSpriteInfo(0x1A108C, 0x10E01C),  # Pop	MA	7DA2B [Standard]
            RoomSpriteInfo(0x1A0F94, 0x10DC3C),  # Pop	MA	7D5EC [Standard]
        ]
    ),
    "Draygon":
    define_location(
        Area="Maridia",
        GraphArea="EastMaridia",
        SolveArea="Draygon Boss",
        Name="Draygon",
        Class=["Boss"],
        CanHidden=False,
        Address=0xB055B058,
        Id=None,
        Visibility="Hidden",
        Room="Draygon's Room",
        BossItemType="Draygon"
    ),
    "Space Jump":
    define_location(
        Area="Maridia",
        GraphArea="EastMaridia",
        SolveArea="Draygon Boss",
        Name="Space Jump",
        Class=["Major", "Chozo", "Scavenger"],
        CanHidden=False,
        Address=0x7C7A7,
        Id=0x9a,
        Visibility="Chozo",
        Room='Space Jump Room',
        VanillaItemType='SpaceJump',
        HUD=12,
    ),
    "Mother Brain":
    define_location(
        Area="Tourian",
        GraphArea="Tourian",
        SolveArea="Tourian",
        Name="Mother Brain",
        Class=["Boss"],
        Address=0xB055B059,
        Id=None,
        Visibility="Hidden",
        CanHidden=False,
        Room='Mother Brain Room',
        BossItemType="MotherBrain"
    ),
    "Spore Spawn":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Pink Brinstar",
        Name="Spore Spawn",
        Class=["Boss"],
        CanHidden=False,
        Address=0xB055B055,
        Id=None,
        Visibility="Hidden",
        Room='Spore Spawn Room',
        BossItemType="SporeSpawn"
    ),
    "Botwoon":
    define_location(
        Area="Maridia",
        GraphArea="EastMaridia",
        SolveArea="Maridia Pink Top",
        Name="Botwoon",
        Class=["Boss"],
        CanHidden=False,
        Address=0xB055B055,
        Id=None,
        Visibility="Hidden",
        Room="Botwoon's Room",
        BossItemType="Botwoon"
    ),
    "Crocomire":
    define_location(
        Area="Norfair",
        GraphArea="Crocomire",
        SolveArea="Crocomire",
        Name="Crocomire",
        Class=["Boss"],
        CanHidden=False,
        Address=0xB055B055,
        Id=None,
        Visibility="Hidden",
        Room="Crocomire's Room",
        BossItemType="Crocomire"
    ),
    "Golden Torizo":
    define_location(
        Area="LowerNorfair",
        GraphArea="LowerNorfair",
        SolveArea="Lower Norfair Screw Attack",
        Name="Golden Torizo",
        Class=["Boss"],
        CanHidden=False,
        Address=0xB055B055,
        Id=None,
        Visibility="Hidden",
        Room="Golden Torizo's Room",
        BossItemType="GoldenTorizo"
    ),
    # MINORS
    "Power Bomb (Crateria surface)":
    define_location(
        Area="Crateria",
        GraphArea="Crateria",
        SolveArea="Crateria Landing Site",
        Name="Power Bomb (Crateria surface)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x781CC,
        Id=0x0,
        Visibility="Visible",
        Room='Crateria Power Bomb Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A001F, 0x1080D5),  # Pop	CR	793AA [Standard]
        ]
    ),
    "Missile (outside Wrecked Ship bottom)":
    define_location(
        Area="Crateria",
        GraphArea="WreckedShip",
        SolveArea="WreckedShip Bottom",
        Name="Missile (outside Wrecked Ship bottom)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x781E8,
        Id=0x1,
        Visibility="Visible",
        Room='West Ocean',
    ),
    "Missile (outside Wrecked Ship top)":
    define_location(
        Area="Crateria",
        GraphArea="WreckedShip",
        SolveArea="WreckedShip Top",
        Name="Missile (outside Wrecked Ship top)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x781EE,
        Id=0x2,
        Visibility="Hidden",
        Room='West Ocean',
    ),
    "Missile (outside Wrecked Ship middle)":
    define_location(
        Area="Crateria",
        GraphArea="WreckedShip",
        SolveArea="WreckedShip Top",
        Name="Missile (outside Wrecked Ship middle)",
        CanHidden=True,
        Class=["Minor"],
        Address=0x781F4,
        Id=0x3,
        Visibility="Visible",
        Room='West Ocean',
    ),
    "Missile (Crateria moat)":
    define_location(
        Area="Crateria",
        GraphArea="Crateria",
        SolveArea="Crateria Landing Site",
        Name="Missile (Crateria moat)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x78248,
        Id=0x4,
        Visibility="Visible",
        Room='The Moat',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A02BF, 0x108F19),  # Pop	CR	7948C [Standard]
            RoomSpriteInfo(0x1A0161, 0x108684),  # Pop	CR	793FE [Standard]
            RoomSpriteInfo(0x1A0009, 0x108002),  # Pop	CR	794FD [Standard]
            RoomSpriteInfo(0x1A023D, 0x108B3E),  # Pop	CR	79552 [Standard]
            RoomSpriteInfo(0x1A0221, 0x108AB8),  # Pop	CR	7957D [Standard]
            RoomSpriteInfo(0x1A0C6D, 0x10C3E6),  # Pop	WS	7CA08 [Standard]
        ]
    ),
    "Missile (Crateria bottom)":
    define_location(
        Area="Crateria",
        GraphArea="Crateria",
        SolveArea="Crateria Landing Site",
        Name="Missile (Crateria bottom)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x783EE,
        Id=0x6,
        Visibility="Visible",
        Room='Pit Room',
    ),
    "Missile (Crateria gauntlet right)":
    define_location(
        Area="Crateria",
        GraphArea="Crateria",
        SolveArea="Crateria Gauntlet",
        Name="Missile (Crateria gauntlet right)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78464,
        Id=0x9,
        Visibility="Visible",
        Room='Green Pirates Shaft',
    ),
    "Missile (Crateria gauntlet left)":
    define_location(
        Area="Crateria",
        GraphArea="Crateria",
        SolveArea="Crateria Gauntlet",
        Name="Missile (Crateria gauntlet left)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7846A,
        Id=0xa,
        Visibility="Visible",
        Room='Green Pirates Shaft',
    ),
    "Super Missile (Crateria)":
    define_location(
        Area="Crateria",
        GraphArea="Crateria",
        SolveArea="Crateria Landing Site",
        Name="Super Missile (Crateria)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78478,
        Id=0xb,
        Visibility="Visible",
        Room='Crateria Super Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A01A5, 0x108870),  # Pop	CR	799F9 [Standard]
        ]
    ),
    "Missile (Crateria middle)":
    define_location(
        Area="Crateria",
        GraphArea="Crateria",
        SolveArea="Crateria Landing Site",
        Name="Missile (Crateria middle)",
        Class=["Minor", "Chozo"],
        CanHidden=True,
        Address=0x78486,
        Id=0xc,
        Visibility="Visible",
        Room='The Final Missile',
    ),
    "Power Bomb (green Brinstar bottom)":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Green Brinstar",
        Name="Power Bomb (green Brinstar bottom)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x784AC,
        Id=0xd,
        Visibility="Chozo",
        Room='Green Brinstar Main Shaft',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0541, 0x10997A),  # Pop	BR	79AD9 [Standard]
            RoomSpriteInfo(0x1A02D5, 0x108F7C),  # Pop	BR	79B9D [Standard]
            RoomSpriteInfo(0x1A04C9, 0x1096E2),  # Pop	BR	79C5E [Standard]
            RoomSpriteInfo(0x1A04D7, 0x109735),  # Pop	BR	79FE5 [Standard]
        ]
    ),
    "Super Missile (pink Brinstar)":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Pink Brinstar",
        Name="Super Missile (pink Brinstar)",
        Class=["Minor", "Chozo"],
        CanHidden=False,
        Address=0x784E4,
        Id=0xe,
        Visibility="Chozo",
        Room='Spore Spawn Super Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0557, 0x109A2D),  # Pop	BR	79B5B [Standard]
            RoomSpriteInfo(0x1A0321, 0x10902E),  # Pop	BR	7A0A4 [Standard]
        ]
    ),
    "Missile (green Brinstar below super missile)":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Green Brinstar",
        Name="Missile (green Brinstar below super missile)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x78518,
        Id=0xf,
        Visibility="Visible",
        Room='Early Supers Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0565, 0x109A40),  # Pop	BR	79BC8 [Standard]
        ]
    ),
    "Super Missile (green Brinstar top)":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Green Brinstar Reserve",
        Name="Super Missile (green Brinstar top)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7851E,
        Id=0x10,
        Visibility="Visible",
        Room='Early Supers Room',
    ),
    "Missile (green Brinstar behind missile)":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Green Brinstar Reserve",
        Name="Missile (green Brinstar behind missile)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x78532,
        Id=0x12,
        Visibility="Hidden",
        Room='Brinstar Reserve Tank Room',
    ),
    "Missile (green Brinstar behind reserve tank)":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Green Brinstar Reserve",
        Name="Missile (green Brinstar behind reserve tank)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78538,
        Id=0x13,
        Visibility="Visible",
        Room='Brinstar Reserve Tank Room',
    ),
    "Missile (pink Brinstar top)":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Pink Brinstar",
        Name="Missile (pink Brinstar top)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78608,
        Id=0x15,
        Visibility="Visible",
        Room='Big Pink',
    ),
    "Missile (pink Brinstar bottom)":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Pink Brinstar",
        Name="Missile (pink Brinstar bottom)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7860E,
        Id=0x16,
        Visibility="Visible",
        Room='Big Pink',
    ),
    "Power Bomb (pink Brinstar)":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Pink Brinstar",
        Name="Power Bomb (pink Brinstar)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7865C,
        Id=0x18,
        Visibility="Visible",
        Room='Pink Brinstar Power Bomb Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A046F, 0x10961D)  # Pop	BR	79E11 [Standard]
        ],
    ),
    "Missile (green Brinstar pipe)":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Brinstar Hills",
        Name="Missile (green Brinstar pipe)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78676,
        Id=0x19,
        Visibility="Visible",
        Room='Green Hill Zone',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A05A7, 0x109CB9),  # Pop	BR	79E52 [Standard]
            RoomSpriteInfo(0x1A03A3, 0x1092A3),  # Pop	BR	79FBA [Standard]
        ]
    ),
    "Power Bomb (blue Brinstar)":
    define_location(
        Area="Brinstar",
        GraphArea="Crateria",
        SolveArea="Blue Brinstar",
        Name="Power Bomb (blue Brinstar)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7874C,
        Id=0x1b,
        Visibility="Visible",
        Room='Morph Ball Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A03B5, 0x109326),  # Pop	BR	79E9F [Standard]
            RoomSpriteInfo(0x1A0595, 0x109BC6),  # Pop	BR	79F11 [Standard]
            RoomSpriteInfo(0x1A020F, 0x108A15),  # Pop	CR	7975C [Standard]
            RoomSpriteInfo(0x1A014F, 0x1085E1),  # Pop	CR	796BA [Standard]
            RoomSpriteInfo(0x1A0185, 0x1086FA),  # Pop	CR	792FD [Standard]
        ]
    ),
    "Missile (blue Brinstar middle)":
    define_location(
        Area="Brinstar",
        GraphArea="Crateria",
        SolveArea="Blue Brinstar",
        Name="Missile (blue Brinstar middle)",
        Address=0x78798,
        Id=0x1c,
        Class=["Minor"],
        CanHidden=True,
        Visibility="Visible",
        Room='Blue Brinstar Energy Tank Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A008F, 0x108427),  # Pop	CR	7975C [Awake]
            RoomSpriteInfo(0x1A01D3, 0x1088C9),  # Pop	CR	796BA [Awake]
            RoomSpriteInfo(0x1A0067, 0x108261),  # Pop	CR	792FD [Awake]
            RoomSpriteInfo(0x1A007D, 0x108364),  # Pop	CR	79879 [Standard]
            RoomSpriteInfo(0x1A025F, 0x108B87),  # Pop	CR	798E2 [Standard]
            RoomSpriteInfo(0x1A0043, 0x10819B),  # Pop	CR	79A44 [Events 1]
            RoomSpriteInfo(0x1A0055, 0x1081FE),  # Pop	CR	79A44 [Standard]
            RoomSpriteInfo(0x1A0377, 0x10918D),  # Pop	BR	79F11 [Events 1]
            RoomSpriteInfo(0x1A0389, 0x109200),  # Pop	BR	79F64 [Events 1]
            RoomSpriteInfo(0x1A03D1, 0x1093AC),  # Pop	BR	79E9F [Standard]
        ]
    ),
    "Super Missile (green Brinstar bottom)":
    define_location(
        Area="Brinstar",
        GraphArea="GreenPinkBrinstar",
        SolveArea="Green Brinstar",
        Name="Super Missile (green Brinstar bottom)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x787D0,
        Id=0x1f,
        Visibility="Visible",
        Room='Etecoon Super Room',
    ),
    "Missile (blue Brinstar bottom)":
    define_location(
        Area="Brinstar",
        GraphArea="Crateria",
        SolveArea="Blue Brinstar",
        Name="Missile (blue Brinstar bottom)",
        Class=["Minor", "Chozo"],
        CanHidden=False,
        Address=0x78802,
        Id=0x22,
        Visibility="Chozo",
        Room='First Missile Room',
    ),
    "Missile (blue Brinstar top)":
    define_location(
        Area="Brinstar",
        GraphArea="Crateria",
        SolveArea="Blue Brinstar",
        Name="Missile (blue Brinstar top)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78836,
        Id=0x24,
        Visibility="Visible",
        Room='Billy Mays Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0407, 0x109505),  # Pop	BR	7A1AD [Standard]
        ]
    ),
    "Missile (blue Brinstar behind missile)":
    define_location(
        Area="Brinstar",
        GraphArea="Crateria",
        SolveArea="Blue Brinstar",
        Name="Missile (blue Brinstar behind missile)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x7883C,
        Id=0x25,
        Visibility="Hidden",
        Room='Billy Mays Room',
    ),
    "Power Bomb (red Brinstar sidehopper room)":
    define_location(
        Area="Brinstar",
        GraphArea="RedBrinstar",
        SolveArea="Red Brinstar Top",
        Name="Power Bomb (red Brinstar sidehopper room)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x788CA,
        Id=0x27,
        Visibility="Visible",
        Room='Beta Power Bomb Room',
    ),
    "Power Bomb (red Brinstar spike room)":
    define_location(
        Area="Brinstar",
        GraphArea="RedBrinstar",
        SolveArea="Red Brinstar Top",
        Name="Power Bomb (red Brinstar spike room)",
        Class=["Minor", "Chozo"],
        CanHidden=False,
        Address=0x7890E,
        Id=0x28,
        Visibility="Chozo",
        Room='Alpha Power Bomb Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A061F, 0x109F61),  # Pop	BR	7A3AE [Standard]
            RoomSpriteInfo(0x1A063F, 0x10A057),  # Pop	BR	7A322 [Standard]
            RoomSpriteInfo(0x1A034F, 0x1090C7),  # Pop	BR	7A37C [Standard]
            RoomSpriteInfo(0x1A05D3, 0x109E2F),  # Pop	BR	7A2F7 [Standard]
        ]
    ),
    "Missile (red Brinstar spike room)":
    define_location(
        Area="Brinstar",
        GraphArea="RedBrinstar",
        SolveArea="Red Brinstar Top",
        Name="Missile (red Brinstar spike room)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78914,
        Id=0x29,
        Visibility="Visible",
        Room='Alpha Power Bomb Room',
    ),
    "Missile (Kraid)":
    define_location(
        Area="Brinstar",
        GraphArea="Kraid",
        SolveArea="Kraid",
        Name="Missile (Kraid)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x789EC,
        Id=0x2c,
        Visibility="Hidden",
        Room='Warehouse Keyhunter Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0533, 0x1098F7),  # Pop	BR	7A4DA [Standard]
            RoomSpriteInfo(0x1A0651, 0x10A0BA),  # Pop	BR	7A521 [Standard]
            RoomSpriteInfo(0x1A062D, 0x109FA4),  # Pop	BR	7A56B [Standard]
            RoomSpriteInfo(0x1A03E3, 0x10941F),  # Pop	BR	7A471 [Standard]
        ]
    ),
    "Missile (lava room)":
    define_location(
        Area="Norfair",
        GraphArea="Norfair",
        SolveArea="Norfair Entrance",
        Name="Missile (lava room)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x78AE4,
        Id=0x31,
        Visibility="Hidden",
        Room='Cathedral',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0A25, 0x10B544),  # Pop	NO	7A788 [Standard]
            RoomSpriteInfo(0x1A092B, 0x10AF87),  # Pop	NO	7A7B3 [Standard]
        ]
    ),
    "Missile (below Ice Beam)":
    define_location(
        Area="Norfair",
        GraphArea="Norfair",
        SolveArea="Norfair Ice",
        Name="Missile (below Ice Beam)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x78B46,
        Id=0x33,
        Visibility="Hidden",
        Room='Crumble Shaft',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A097D, 0x10B1F6),  # Pop	NO	7A8F8 [Standard]
            RoomSpriteInfo(0x1A06D5, 0x10A332),  # Pop	NO	7A815 [Standard]
        ]
    ),
    "Missile (above Crocomire)":
    define_location(
        Area="Norfair",
        GraphArea="Norfair",
        SolveArea="Norfair Grapple Escape",
        Name="Missile (above Crocomire)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x78BC0,
        Id=0x36,
        Visibility="Visible",
        Room='Crocomire Escape',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A08BF, 0x10AD8F),  # Pop	NO	7AA0E [Standard]
            RoomSpriteInfo(0x1A0845, 0x10A9DA),  # Pop	NO	7A923 [Standard]
            RoomSpriteInfo(0x1A09A5, 0x10B32C),  # Pop	NO	7AFCE [Standard]
            RoomSpriteInfo(0x1A06EF, 0x10A3F5),  # Pop	NO	7AFFB [Standard]
            RoomSpriteInfo(0x1A0683, 0x10A133),  # Pop	NO	7AB64 [Standard]
        ]
    ),
    "Missile (Hi-Jump Boots)":
    define_location(
        Area="Norfair",
        GraphArea="Norfair",
        SolveArea="Norfair Entrance",
        Name="Missile (Hi-Jump Boots)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78BE6,
        Id=0x37,
        Visibility="Visible",
        Room='Hi Jump Energy Tank Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A09CB, 0x10B3C5),  # Pop	NO	7AA41 [Standard]
            RoomSpriteInfo(0x1A0AED, 0x10B9D8),  # Pop	NO	7A7DE [Standard]
        ]
    ),
    "Energy Tank (Hi-Jump Boots)":
    define_location(
        Area="Norfair",
        GraphArea="Norfair",
        SolveArea="Norfair Entrance",
        Name="Energy Tank (Hi-Jump Boots)",
        CanHidden=True,
        Class=["Minor"],
        Address=0x78BEC,
        Id=0x38,
        Visibility="Visible",
        Room='Hi Jump Energy Tank Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A09CB, 0x10B3C5),  # Pop	NO	7AA41 [Standard]
            RoomSpriteInfo(0x1A0AED, 0x10B9D8),  # Pop	NO	7A7DE [Standard]
        ]
    ),
    "Power Bomb (Crocomire)":
    define_location(
        Area="Norfair",
        GraphArea="Crocomire",
        SolveArea="Crocomire",
        Name="Power Bomb (Crocomire)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78C04,
        Id=0x39,
        Visibility="Visible",
        Room='Post Crocomire Power Bomb Room',
    ),
    "Missile (below Crocomire)":
    define_location(
        Area="Norfair",
        GraphArea="Crocomire",
        SolveArea="Crocomire",
        Name="Missile (below Crocomire)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78C14,
        Id=0x3a,
        Visibility="Visible",
        Room='Post Crocomire Missile Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0A13, 0x10B4D1),  # Pop	NO	7AB3B [Standard]
        ]
    ),
    "Missile (Grapple Beam)":
    define_location(
        Area="Norfair",
        GraphArea="Crocomire",
        SolveArea="Crocomire",
        Name="Missile (Grapple Beam)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78C2A,
        Id=0x3b,
        Visibility="Visible",
        Room='Post Crocomire Jump Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0953, 0x10B11D),  # Pop	NO	7AB8F [Standard]
        ]
    ),
    "Missile (Norfair Reserve Tank)":
    define_location(
        Area="Norfair",
        GraphArea="Norfair",
        SolveArea="Bubble Norfair Reserve",
        Name="Missile (Norfair Reserve Tank)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x78C44,
        Id=0x3e,
        Visibility="Hidden",
        Room='Norfair Reserve Tank Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0A37, 0x10B5E7),  # Pop	NO	7AC5A [Standard]
        ]
    ),
    "Missile (bubble Norfair green door)":
    define_location(
        Area="Norfair",
        GraphArea="Norfair",
        SolveArea="Bubble Norfair Reserve",
        Name="Missile (bubble Norfair green door)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78C52,
        Id=0x3f,
        Visibility="Visible",
        Room='Green Bubbles Missile Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0907, 0x10AEB1),  # Pop	NO	7AC83 [Standard]
        ]
    ),
    "Missile (bubble Norfair)":
    define_location(
        Area="Norfair",
        GraphArea="Norfair",
        SolveArea="Bubble Norfair Bottom",
        Name="Missile (bubble Norfair)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78C66,
        Id=0x40,
        Visibility="Visible",
        Room='Bubble Mountain',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A09D9, 0x10B3D8),  # Pop	NO	7ACB3 [Standard]
            RoomSpriteInfo(0x1A07C9, 0x10A6A8),  # Pop	NO	7AFA3 [Standard]
            RoomSpriteInfo(0x1A08E9, 0x10AEA8),  # Pop	NO	7AEDF [Standard]
            RoomSpriteInfo(0x1A06C7, 0x10A2DF),  # Pop	NO	7B051 [Standard]
            RoomSpriteInfo(0x1A0887, 0x10AC53),  # Pop	NO	7AEB4 [Standard]
            RoomSpriteInfo(0x1A0ADF, 0x10B995),  # Pop	NO	7AE74 [Standard]
            RoomSpriteInfo(0x1A07BB, 0x10A645),  # Pop	NO	7B106 [Standard]
            RoomSpriteInfo(0x1A0B3B, 0x10BBD7),  # Pop	NO	7AF72 [Standard]
            RoomSpriteInfo(0x1A0833, 0x10A967),  # Pop	NO	7B139 [Standard]
            RoomSpriteInfo(0x1A08A3, 0x10AD09),  # Pop	NO	7AF14 [Standard]
        ]
    ),
    "Missile (Speed Booster)":
    define_location(
        Area="Norfair",
        GraphArea="Norfair",
        SolveArea="Bubble Norfair Speed",
        Name="Missile (Speed Booster)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x78C74,
        Id=0x41,
        Visibility="Hidden",
        Room='Speed Booster Hall',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0ABB, 0x10B88F),  # Pop	NO	7ACF0 [Standard]
            RoomSpriteInfo(0x1A0ACD, 0x10B912),  # Pop	NO	7B07A [Standard]
        ]
    ),
    "Missile (Wave Beam)":
    define_location(
        Area="Norfair",
        GraphArea="Norfair",
        SolveArea="Bubble Norfair Wave",
        Name="Missile (Wave Beam)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78CBC,
        Id=0x43,
        Visibility="Visible",
        Room='Double Chamber',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A080B, 0x10A8E1),  # Pop	NO	7ADAD [Standard]
            RoomSpriteInfo(0x1A0AA9, 0x10B81C),  # Pop	NO	7AD5E [Standard]
            RoomSpriteInfo(0x1A0A7B, 0x10B733),  # Pop	NO	7AE07 [Standard]
            RoomSpriteInfo(0x1A0B29, 0x10BB34),  # Pop	NO	7AE32 [Standard]
        ]
    ),
    "Missile (Gold Torizo)":
    define_location(
        Area="LowerNorfair",
        GraphArea="LowerNorfair",
        SolveArea="Lower Norfair Screw Attack",
        Name="Missile (Gold Torizo)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78E6E,
        Id=0x46,
        Visibility="Visible",
        Room="Golden Torizo's Room",
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A06B1, 0x10A23C),  # Pop	NO	7B1E5 [Standard]
            RoomSpriteInfo(0x1A093D, 0x10AFEA),  # Pop	NO	7B236 [Standard]
            RoomSpriteInfo(0x1A0727, 0x10A4F1),  # Pop	NO	7B3A5 [Standard]
            RoomSpriteInfo(0x1A08B1, 0x10AD6C),  # Pop	NO	7B457 [Standard]
        ]
    ),
    "Super Missile (Gold Torizo)":
    define_location(
        Area="LowerNorfair",
        GraphArea="LowerNorfair",
        SolveArea="Lower Norfair Screw Attack",
        Name="Super Missile (Gold Torizo)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x78E74,
        Id=0x47,
        Visibility="Hidden",
        Room="Golden Torizo's Room",
    ),
    "Missile (Mickey Mouse room)":
    define_location(
        Area="LowerNorfair",
        GraphArea="LowerNorfair",
        SolveArea="Lower Norfair Before Amphitheater",
        Name="Missile (Mickey Mouse room)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78F30,
        Id=0x49,
        Visibility="Visible",
        Room='Mickey Mouse Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0765, 0x10A560),  # Pop	NO	7B40A [Standard]
            RoomSpriteInfo(0x1A07F5, 0x10A82E),  # Pop	NO	7B4AD [Standard]
            RoomSpriteInfo(0x1A091D, 0x10AEF4),  # Pop	NO	7B4E5 [Standard]
        ]
    ),
    "Missile (lower Norfair above fire flea room)":
    define_location(
        Area="LowerNorfair",
        GraphArea="LowerNorfair",
        SolveArea="Lower Norfair After Amphitheater",
        Name="Missile (lower Norfair above fire flea room)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x78FCA,
        Id=0x4a,
        Visibility="Visible",
        Room='Lower Norfair Spring Ball Maze Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A08D1, 0x10AE52),  # Pop	NO	7B510 [Standard]
        ]
    ),
    "Power Bomb (lower Norfair above fire flea room)":
    define_location(
        Area="LowerNorfair",
        GraphArea="LowerNorfair",
        SolveArea="Lower Norfair After Amphitheater",
        Name="Power Bomb (lower Norfair above fire flea room)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x78FD2,
        Id=0x4b,
        Visibility="Visible",
        Room='Lower Norfair Escape Power Bomb Room',
    ),
    "Power Bomb (Power Bombs of shame)":
    define_location(
        Area="LowerNorfair",
        GraphArea="LowerNorfair",
        SolveArea="Lower Norfair After Amphitheater",
        Name="Power Bomb (Power Bombs of shame)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x790C0,
        Id=0x4c,
        Visibility="Visible",
        Room='Wasteland',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A098B, 0x10B259),  # Pop	NO	7B5D5 [Standard]
            RoomSpriteInfo(0x1A06A3, 0x10A219),  # Pop	NO	7B62B [Standard]
            RoomSpriteInfo(0x1A085F, 0x10AA8D),  # Pop	NO	7B482 [Standard]
            RoomSpriteInfo(0x1A0A97, 0x10B769),  # Pop	NO	7B37A [Standard]
        ]
    ),
    "Missile (lower Norfair near Wave Beam)":
    define_location(
        Area="LowerNorfair",
        GraphArea="LowerNorfair",
        SolveArea="Lower Norfair After Amphitheater",
        Name="Missile (lower Norfair near Wave Beam)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x79100,
        Id=0x4d,
        Visibility="Visible",
        Room="Three Muskateers' Room",
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0AFB, 0x10BA4B),  # Pop	NO	7B656 [Standard]
        ]
    ),
    "Missile (Wrecked Ship middle)":
    define_location(
        Area="WreckedShip",
        GraphArea="WreckedShip",
        SolveArea="WreckedShip Main",
        Name="Missile (Wrecked Ship middle)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7C265,
        Id=0x80,
        Visibility="Visible",
        Room='Wrecked Ship Main Shaft',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0B6D, 0x10BCA0),  # Pop	WS	7CAF6 [Standard]
            RoomSpriteInfo(0x1A0D2B, 0x10CD17),  # Pop	WS	7CAF6 [Bosses]
            RoomSpriteInfo(0x1A0B99, 0x10BFE6),  # Pop	WS	7CA52 [Bosses]
            RoomSpriteInfo(0x1A0CA9, 0x10C6F2),  # Pop	WS	7CA52 [Standard]
            RoomSpriteInfo(0x1A0B4D, 0x10BC3A),  # Pop	WS	7CD5C [Bosses]
            RoomSpriteInfo(0x1A0BE3, 0x10C1A5),  # Pop	WS	7CD5C [Standard]
            RoomSpriteInfo(0x1A0C5B, 0x10C283),  # Pop	WS	7CC6F [Standard]
            RoomSpriteInfo(0x1A0BAF, 0x10C139),  # Pop	WS	7CC6F [Bosses]
            RoomSpriteInfo(0x1A0CBF, 0x10C8C5),  # Pop	WS	7CDF1 [Standard]
            RoomSpriteInfo(0x1A0D07, 0x10CC51),  # Pop	WS	7CDF1 [Bosses]
            RoomSpriteInfo(0x1A0C13, 0x10C1E1),  # Pop	WS	7CAAE [Standard]
            RoomSpriteInfo(0x1A0C7B, 0x10C5E9),  # Pop	WS	7CAAE [Bosses]
            RoomSpriteInfo(0x1A0CF9, 0x10CBAE),  # Pop	WS	7CB8B [Bosses]
            RoomSpriteInfo(0x1A0BD9, 0x10C1A2),  # Pop	WS	7CB8B [Standard]
            RoomSpriteInfo(0x1A0C01, 0x10C1AE),  # Pop	WS	7C98E [Bosses]
        ]
    ),
    "Missile (Gravity Suit)":
    define_location(
        Area="WreckedShip",
        GraphArea="WreckedShip",
        SolveArea="WreckedShip Gravity",
        Name="Missile (Gravity Suit)",
        Class=["Minor", "Chozo"],
        CanHidden=False,
        Address=0x7C2EF,
        Id=0x82,
        Visibility="Visible",
        Room='Bowling Alley',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0B87, 0x10BE93),  # Pop	WS	7C98E [Standard]
            RoomSpriteInfo(0x1A01C1, 0x1088B6),  # Pop	CR	7968F [Standard]
            RoomSpriteInfo(0x1A01E1, 0x10897C),  # Pop	CR	79461 [Standard]
        ]
    ),
    "Missile (Wrecked Ship top)":
    define_location(
        Area="WreckedShip",
        GraphArea="WreckedShip",
        SolveArea="WreckedShip Top",
        Name="Missile (Wrecked Ship top)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7C319,
        Id=0x83,
        Visibility="Visible",
        Room='Wrecked Ship East Missile Room',
    ),
    "Super Missile (Wrecked Ship left)":
    define_location(
        Area="WreckedShip",
        GraphArea="WreckedShip",
        SolveArea="WreckedShip Main",
        Name="Super Missile (Wrecked Ship left)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7C357,
        Id=0x85,
        Visibility="Visible",
        Room='Wrecked Ship West Super Room',
    ),
    "Missile (green Maridia shinespark)":
    define_location(
        Area="Maridia",
        GraphArea="WestMaridia",
        SolveArea="Maridia Green",
        Name="Missile (green Maridia shinespark)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x7C437,
        Id=0x88,
        Visibility="Visible",
        Room='Main Street',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A103A, 0x10DE6D),  # Pop	MA	7CFC9 [Standard]
            RoomSpriteInfo(0x1A0EB6, 0x10D635),  # Pop	MA	7D08A [Standard]
            RoomSpriteInfo(0x1A101A, 0x10DE17),  # Pop	MA	7D21C [Standard]
            RoomSpriteInfo(0x1A0E96, 0x10D53F),  # Pop	MA	7CF80 [Standard]
            RoomSpriteInfo(0x1A0D41, 0x10CE6A),  # Pop	MA	7D0B9 [Standard]
            RoomSpriteInfo(0x1A109E, 0x10E07F),  # Pop	MA	7D017 [Standard]
            RoomSpriteInfo(0x1A0E2C, 0x10D3AA),  # Pop	MA	7D104 [Standard]
            RoomSpriteInfo(0x1A0D77, 0x10CFC3),  # Pop	MA	7D1A3 [Standard]
        ]
    ),
    "Super Missile (green Maridia)":
    define_location(
        Area="Maridia",
        GraphArea="WestMaridia",
        SolveArea="Maridia Green",
        Name="Super Missile (green Maridia)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7C43D,
        Id=0x89,
        Visibility="Visible",
        Room='Main Street',
    ),
    "Missile (green Maridia tatori)":
    define_location(
        Area="Maridia",
        GraphArea="WestMaridia",
        SolveArea="Maridia Green",
        Name="Missile (green Maridia tatori)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x7C483,
        Id=0x8b,
        Visibility="Hidden",
        Room='Mama Turtle Room',
    ),
    "Super Missile (yellow Maridia)":
    define_location(
        Area="Maridia",
        GraphArea="WestMaridia",
        SolveArea="Maridia Pink Bottom",
        Name="Super Missile (yellow Maridia)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7C4AF,
        Id=0x8c,
        Visibility="Visible",
        Room='Watering Hole',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0D65, 0x10CF90),  # Pop	MA	7D13B [Standard]
        ]
    ),
    "Missile (yellow Maridia super missile)":
    define_location(
        Area="Maridia",
        GraphArea="WestMaridia",
        SolveArea="Maridia Pink Bottom",
        Name="Missile (yellow Maridia super missile)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7C4B5,
        Id=0x8d,
        Visibility="Visible",
        Room='Watering Hole',
    ),
    "Missile (yellow Maridia false wall)":
    define_location(
        Area="Maridia",
        GraphArea="WestMaridia",
        SolveArea="Maridia Pink Bottom",
        Name="Missile (yellow Maridia false wall)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7C533,
        Id=0x8e,
        Visibility="Visible",
        Room='Pseudo Plasma Spark Room',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0ED6, 0x10D75B),  # Pop	MA	7D1DD [Standard]
            RoomSpriteInfo(0x1A0EC4, 0x10D698),  # Pop	MA	7D16D [Standard]
        ]
    ),
    "Missile (left Maridia sand pit room)":
    define_location(
        Area="Maridia",
        GraphArea="EastMaridia",
        SolveArea="Left Sandpit",
        Name="Missile (left Maridia sand pit room)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7C5DD,
        Id=0x90,
        Visibility="Visible",
        Room='West Sand Hole',
    ),
    "Missile (right Maridia sand pit room)":
    define_location(
        Area="Maridia",
        GraphArea="EastMaridia",
        SolveArea="Right Sandpit",
        Name="Missile (right Maridia sand pit room)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7C5EB,
        Id=0x92,
        Visibility="Visible",
        Room='East Sand Hole',
    ),
    "Power Bomb (right Maridia sand pit room)":
    define_location(
        Area="Maridia",
        GraphArea="EastMaridia",
        SolveArea="Right Sandpit",
        Name="Power Bomb (right Maridia sand pit room)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7C5F1,
        Id=0x93,
        Visibility="Visible",
        Room='East Sand Hole',
    ),
    "Missile (pink Maridia)":
    define_location(
        Area="Maridia",
        GraphArea="EastMaridia",
        SolveArea="Maridia Pink Bottom",
        Name="Missile (pink Maridia)",
        Address=0x7C603,
        Id=0x94,
        Class=["Minor"],
        CanHidden=True,
        Visibility="Visible",
        Room='Aqueduct',
        NearbyRoomsWithSprites=[
            RoomSpriteInfo(0x1A0E1E, 0x10D357),  # Pop	MA	7D5A7 [Standard]
            RoomSpriteInfo(0x1A0F78, 0x10DB66),  # Pop	MA	7D54D [Standard]
            RoomSpriteInfo(0x1A0FA2, 0x10DC6F),  # Pop	MA	7D617 [Standard]
            RoomSpriteInfo(0x1A106C, 0x10DF96),  # Pop	MA	7D4EF [Standard]
            RoomSpriteInfo(0x1A105E, 0x10DF63),  # Pop	MA	7D51E [Standard]
        ]
    ),
    "Super Missile (pink Maridia)":
    define_location(
        Area="Maridia",
        GraphArea="EastMaridia",
        SolveArea="Maridia Pink Bottom",
        Name="Super Missile (pink Maridia)",
        Class=["Minor"],
        CanHidden=True,
        Address=0x7C609,
        Id=0x95,
        Visibility="Visible",
        Room='Aqueduct',
    ),
    "Missile (Draygon)":
    define_location(
        Area="Maridia",
        GraphArea="EastMaridia",
        SolveArea="Maridia Pink Top",
        Name="Missile (Draygon)",
        Class=["Minor"],
        CanHidden=False,
        Address=0x7C74D,
        Id=0x97,
        Visibility="Hidden",
        Room='The Precious Room',
    )
}