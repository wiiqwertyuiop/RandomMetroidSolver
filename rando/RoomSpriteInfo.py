class RoomSpriteInfo:
    __slots__ = ('header', 'spriteData')

    def __init__(self, header, spriteData) -> None:
        self.header = header
        self.spriteData = spriteData


pathConnector = {
    "Landing Site": [
        RoomSpriteInfo(0x1A0185, 0x1086FA),  # Pop	CR	792FD [Standard]
        RoomSpriteInfo(0x1A0067, 0x108261),  # Pop	CR	792FD [Awake]
        RoomSpriteInfo(0x1A007D, 0x108364),  # Pop	CR	79879 [Standard]
        RoomSpriteInfo(0x1A025F, 0x108B87),  # Pop	CR	798E2 [Standard]
        RoomSpriteInfo(0x1A0043, 0x10819B),  # Pop	CR	79A44 [Events 1]
        RoomSpriteInfo(0x1A0055, 0x1081FE),  # Pop	CR	79A44 [Standard]
        RoomSpriteInfo(0x1A0031, 0x108108),  # Pop	CR	7990D [Standard]
        RoomSpriteInfo(0x1A014F, 0x1085E1),  # Pop	CR	796BA [Standard]
        RoomSpriteInfo(0x1A01D3, 0x1088C9),  # Pop	CR	796BA [Awake]
        RoomSpriteInfo(0x1A03B5, 0x109326),  # Pop	BR	79E9F [Standard]
        RoomSpriteInfo(0x1A03D1, 0x1093AC),  # Pop	BR	79E9F [Standard]
        RoomSpriteInfo(0x1A0595, 0x109BC6),  # Pop	BR	79F11 [Standard]
        RoomSpriteInfo(0x1A0377, 0x10918D),  # Pop	BR	79F11 [Events 1]
        RoomSpriteInfo(0x1A020F, 0x108A15),  # Pop	CR	7975C [Standard]
        RoomSpriteInfo(0x1A008F, 0x108427),  # Pop	CR	7975C [Awake]
        RoomSpriteInfo(0x1A001F, 0x1080D5),  # Pop	CR	793AA [Standard]
        RoomSpriteInfo(0x1A01FD, 0x1089F2),  # Pop	CR	7965B [Standard]
        RoomSpriteInfo(0x1A00A1, 0x10847A),  # Pop	CR	792B3 [Standard]
    ],
    "Blue Brinstar Elevator Bottom": [
        RoomSpriteInfo(0x1A03B5, 0x109326),  # Pop	BR	79E9F [Standard]
        RoomSpriteInfo(0x1A03D1, 0x1093AC),  # Pop	BR	79E9F [Standard]
        RoomSpriteInfo(0x1A0595, 0x109BC6),  # Pop	BR	79F11 [Standard]
        RoomSpriteInfo(0x1A0377, 0x10918D),  # Pop	BR	79F11 [Events 1]
        RoomSpriteInfo(0x1A0389, 0x109200),  # Pop	BR	79F64 [Events 1]
        RoomSpriteInfo(0x1A0407, 0x109505),  # Pop	BR	7A1AD [Standard]
    ],
    "Gauntlet Top": [
        RoomSpriteInfo(0x1A01FD, 0x1089F2),  # Pop	CR	7965B [Standard]
        RoomSpriteInfo(0x1A00A1, 0x10847A),  # Pop	CR	792B3 [Standard]
    ],
    "Lower Mushrooms Left": [
        RoomSpriteInfo(0x1A0271, 0x108BCA),  # Pop	CR	79969 [Standard]
    ],
    "Green Pirates Shaft Bottom Right": [
        RoomSpriteInfo(0x1A00C1, 0x108500),  # Pop	CR	799BD [Standard]
        RoomSpriteInfo(0x1A0271, 0x108BCA),  # Pop	CR	79969 [Standard]
    ],
    "Moat Right": [
        RoomSpriteInfo(0x1A02BF, 0x108F19),  # Pop	CR	7948C [Standard]
    ],
    "Moat Left": [
        RoomSpriteInfo(0x1A02BF, 0x108F19),  # Pop	CR	7948C [Standard]
    ],
    "Keyhunter Room Bottom": [
        RoomSpriteInfo(0x1A02BF, 0x108F19),  # Pop	CR	7948C [Standard]
    ],
    "Morph Ball Room Left": [
        RoomSpriteInfo(0x1A03B5, 0x109326),  # Pop	BR	79E9F [Standard]
        RoomSpriteInfo(0x1A03D1, 0x1093AC),  # Pop	BR	79E9F [Standard]
    ],
    "Green Brinstar Elevator": [
        # RoomSpriteInfo(0x1A00D3,, 0x108573), // Pop	CR	79938 [Standard]
        RoomSpriteInfo(0x1A0541, 0x10997A),  # Pop	BR	79AD9 [Standard]
        RoomSpriteInfo(0x1A02D5, 0x108F7C),  # Pop	BR	79B9D [Standard]
        RoomSpriteInfo(0x1A04C9, 0x1096E2),  # Pop	BR	79C5E [Standard]
        RoomSpriteInfo(0x1A04D7, 0x109735),  # Pop	BR	79FE5 [Standard]
        RoomSpriteInfo(0x1A0565, 0x109A40),  # Pop	BR	79BC8 [Standard]
        RoomSpriteInfo(0x1A05B9, 0x109D5C),  # Pop	BR	79CB3 [Standard]
    ],
    "Big Pink": [
        RoomSpriteInfo(0x1A0429, 0x10953E),  # Pop	BR	79D19 [Standard]
        RoomSpriteInfo(0x1A02FB, 0x108FC5),  # Pop	BR	79D9C [Standard]
        RoomSpriteInfo(0x1A04F7, 0x1097FB),  # Pop	BR	7A130 [Standard]
        RoomSpriteInfo(0x1A046F, 0x10961D),  # Pop	BR	79E11 [Standard]
        RoomSpriteInfo(0x1A0361, 0x10911A),  # Pop	BR	7A0D2 [Standard]
        RoomSpriteInfo(0x1A0557, 0x109A2D),  # Pop	BR	79B5B [Standard]
        RoomSpriteInfo(0x1A0321, 0x10902E),  # Pop	BR	7A0A4 [Standard]
    ],
    "Green Hill Zone Top Right": [
        RoomSpriteInfo(0x1A05A7, 0x109CB9),  # Pop	BR	79E52 [Standard]
    ],
    "Noob Bridge Right": [
        RoomSpriteInfo(0x1A03A3, 0x1092A3),  # Pop	BR	79FBA [Standard]
    ],
    "West Ocean Left": [
        RoomSpriteInfo(0x1A0161, 0x108684),  # Pop	CR	793FE [Standard]
    ],
    "Wrecked Ship Main": [
        RoomSpriteInfo(0x1A0161, 0x108684),  # Pop	CR	793FE [Standard]
        RoomSpriteInfo(0x1A0B6D, 0x10BCA0),  # Pop	WS	7CAF6 [Standard]
        RoomSpriteInfo(0x1A0D2B, 0x10CD17),  # Pop	WS	7CAF6 [Bosses]
        RoomSpriteInfo(0x1A0B99, 0x10BFE6),  # Pop	WS	7CA52 [Bosses]
        RoomSpriteInfo(0x1A0CA9, 0x10C6F2),  # Pop	WS	7CA52 [Standard]
        RoomSpriteInfo(0x1A0B4D, 0x10BC3A),  # Pop	WS	7CD5C [Bosses]
        RoomSpriteInfo(0x1A0BE3, 0x10C1A5),  # Pop	WS	7CD5C [Standard]
        RoomSpriteInfo(0x1A0CBF, 0x10C8C5),  # Pop	WS	7CDF1 [Standard]
        RoomSpriteInfo(0x1A0D07, 0x10CC51),  # Pop	WS	7CDF1 [Bosses]
        RoomSpriteInfo(0x1A0C13, 0x10C1E1),  # Pop	WS	7CAAE [Standard]
        RoomSpriteInfo(0x1A0C7B, 0x10C5E9),  # Pop	WS	7CAAE [Bosses]
        RoomSpriteInfo(0x1A0CF9, 0x10CBAE),  # Pop	WS	7CB8B [Bosses]
        RoomSpriteInfo(0x1A0BD9, 0x10C1A2),  # Pop	WS	7CB8B [Standard]
        RoomSpriteInfo(0x1A0C6D, 0x10C3E6),  # Pop	WS	7CA08 [Standard]
    ],
    "Wrecked Ship Back": [
        RoomSpriteInfo(0x1A0B5B, 0x10BC4D),  # Pop	WS	7CC27 [Bosses]
    ],
    "PhantoonRoomOut": [
        RoomSpriteInfo(0x1A0C5B, 0x10C283),  # Pop	WS	7CC6F [Standard]
        RoomSpriteInfo(0x1A0BAF, 0x10C139),  # Pop	WS	7CC6F [Bosses]
    ],
    "Bowling": [
        RoomSpriteInfo(0x1A01E1, 0x10897C),  # Pop	CR	79461 [Standard]
        RoomSpriteInfo(0x1A0C01, 0x10C1AE),  # Pop	WS	7C98E [Bosses]
        RoomSpriteInfo(0x1A01C1, 0x1088B6),  # Pop	CR	7968F [Standard])
    ],
    "Crab Maze Left": [
        RoomSpriteInfo(0x1A0221, 0x108AB8),  # Pop	CR	7957D [Standard]
        RoomSpriteInfo(0x1A023D, 0x108B3E),  # Pop	CR	79552 [Standard]
        RoomSpriteInfo(0x1A0009, 0x108002),  # Pop	CR	794FD [Standard]
    ],
    "Lava Dive Right": [
        RoomSpriteInfo(0x1A08A3, 0x10AD09),  # Pop	NO	7AF14 [Standard]
    ],
    "LN Entrance": [
        RoomSpriteInfo(0x1A06B1, 0x10A23C),  # Pop	NO	7B1E5 [Standard]
        RoomSpriteInfo(0x1A093D, 0x10AFEA),  # Pop	NO	7B236 [Standard]
        RoomSpriteInfo(0x1A0727, 0x10A4F1),  # Pop	NO	7B3A5 [Standard]
        RoomSpriteInfo(0x1A08B1, 0x10AD6C),  # Pop	NO	7B457 [Standard]
        RoomSpriteInfo(0x1A0765, 0x10A560),  # Pop	NO	7B40A [Standard]
        RoomSpriteInfo(0x1A07F5, 0x10A82E),  # Pop	NO	7B4AD [Standard]
        RoomSpriteInfo(0x1A091D, 0x10AEF4),  # Pop	NO	7B4E5 [Standard]
        RoomSpriteInfo(0x1A06FD, 0x10A428),  # Pop	NO	7B585 [Standard]
    ],
    "LN Above GT": [
    ],
    "Firefleas": [
        RoomSpriteInfo(0x1A0871, 0x10AB80),  # Pop	NO	7B6EE [Standard]
        RoomSpriteInfo(0x1A0AFB, 0x10BA4B),  # Pop	NO	7B656 [Standard]
        RoomSpriteInfo(0x1A08D1, 0x10AE52),  # Pop	NO	7B510 [Standard]
    ],
    "Crocomire Room Top": [
        RoomSpriteInfo(0x1A0953, 0x10B11D),  # Pop	NO	7AB8F [Standard]
        RoomSpriteInfo(0x1A07DF, 0x10A7BB),  # Pop	NO	7AA82 [Standard]
        RoomSpriteInfo(0x1A0695, 0x10A1D6),  # Pop	NO	7AB07 [Standard]
        RoomSpriteInfo(0x1A0A13, 0x10B4D1),  # Pop	NO	7AB3B [Standard]
        RoomSpriteInfo(0x1A09B7, 0x10B3BF),  # Pop	NO	7AC00 [Standard]
        RoomSpriteInfo(0x1A0A49, 0x10B67A),  # Pop	NO	7ABD2 [Standard]
        RoomSpriteInfo(0x1A0683, 0x10A133),  # Pop	NO	7AB64 [Standard]
    ],
    "Three Muskateers Room Left": [
        # RoomSpriteInfo(0x1A06B1, 0x10A23C),  # Pop	NO	7B1E5 [Standard]
        # RoomSpriteInfo(0x1A093D, 0x10AFEA),  # Pop	NO	7B236 [Standard]
        # RoomSpriteInfo(0x1A0727, 0x10A4F1),  # Pop	NO	7B3A5 [Standard]
        # RoomSpriteInfo(0x1A08B1, 0x10AD6C),  # Pop	NO	7B457 [Standard]
        # RoomSpriteInfo(0x1A0765, 0x10A560),  # Pop	NO	7B40A [Standard]
        # RoomSpriteInfo(0x1A07F5, 0x10A82E),  # Pop	NO	7B4AD [Standard]
        # RoomSpriteInfo(0x1A091D, 0x10AEF4),  # Pop	NO	7B4E5 [Standard]
        # RoomSpriteInfo(0x1A06FD, 0x10A428),  # Pop	NO	7B585 [Standard]
        # RoomSpriteInfo(0x1A098B, 0x10B259),  # Pop	NO	7B5D5 [Standard]
        # RoomSpriteInfo(0x1A06A3, 0x10A219),  # Pop	NO	7B62B [Standard]
        # RoomSpriteInfo(0x1A085F, 0x10AA8D),  # Pop	NO	7B482 [Standard]
        # RoomSpriteInfo(0x1A0A97, 0x10B769),  # Pop	NO	7B37A [Standard]
        # RoomSpriteInfo(0x1A0871, 0x10AB80),  # Pop	NO	7B6EE [Standard]
        RoomSpriteInfo(0x1A0AFB, 0x10BA4B),  # Pop	NO	7B656 [Standard]
        RoomSpriteInfo(0x1A08D1, 0x10AE52),  # Pop	NO	7B510 [Standard]
    ],
    "Wasteland": [
        RoomSpriteInfo(0x1A06FD, 0x10A428),  # Pop	NO	7B585 [Standard]
        RoomSpriteInfo(0x1A098B, 0x10B259),  # Pop	NO	7B5D5 [Standard]
    ],
    "Ridley Zone": [
        RoomSpriteInfo(0x1A098B, 0x10B259),  # Pop	NO	7B5D5 [Standard]
        RoomSpriteInfo(0x1A06A3, 0x10A219),  # Pop	NO	7B62B [Standard]
        RoomSpriteInfo(0x1A085F, 0x10AA8D),  # Pop	NO	7B482 [Standard]
    ],
    "RidleyRoomOut": [
        RoomSpriteInfo(0x1A0A97, 0x10B769),  # Pop	NO	7B37A [Standard]
    ],
    "Crocomire Speedway Bottom": [
        RoomSpriteInfo(0x1A0845, 0x10A9DA),  # Pop	NO	7A923 [Standard]
        RoomSpriteInfo(0x1A09A5, 0x10B32C),  # Pop	NO	7AFCE [Standard]
        RoomSpriteInfo(0x1A0833, 0x10A967),  # Pop	NO	7B139 [Standard]
        RoomSpriteInfo(0x1A0B3B, 0x10BBD7),  # Pop	NO	7AF72 [Standard]
    ],
    "Bubble Mountain Bottom": [
        RoomSpriteInfo(0x1A09D9, 0x10B3D8),  # Pop	NO	7ACB3 [Standard]
    ],
    "Bubble Mountain": [
        RoomSpriteInfo(0x1A09D9, 0x10B3D8),  # Pop	NO	7ACB3 [Standard]
        RoomSpriteInfo(0x1A07C9, 0x10A6A8),  # Pop	NO	7AFA3 [Standard]
        RoomSpriteInfo(0x1A0A25, 0x10B544),  # Pop	NO	7A788 [Standard]
        RoomSpriteInfo(0x1A092B, 0x10AF87),  # Pop	NO	7A7B3 [Standard]
        RoomSpriteInfo(0x1A0A37, 0x10B5E7),  # Pop	NO	7AC5A [Standard]
        RoomSpriteInfo(0x1A0907, 0x10AEB1),  # Pop	NO	7AC83 [Standard]
    ],
    "Bubble Mountain Top": [
        RoomSpriteInfo(0x1A09D9, 0x10B3D8),  # Pop	NO	7ACB3 [Standard]
        RoomSpriteInfo(0x1A0ABB, 0x10B88F),  # Pop	NO	7ACF0 [Standard]
        RoomSpriteInfo(0x1A0ACD, 0x10B912),  # Pop	NO	7B07A [Standard]
        RoomSpriteInfo(0x1A0A37, 0x10B5E7),  # Pop	NO	7AC5A [Standard]
        RoomSpriteInfo(0x1A0907, 0x10AEB1),  # Pop	NO	7AC83 [Standard]
        # RoomSpriteInfo(0x1A0AA9, 0x10B81C),  # Pop	NO	7AD5E [Standard]
        # Pop	NO	7ADAD [Standard]
        RoomSpriteInfo(0x1A080B, 0x10A8E1),
        # Pop	NO	7AE07 [Standard]
        RoomSpriteInfo(0x1A0A7B, 0x10B733),
        # Pop	NO	7AE32 [Standard]
        RoomSpriteInfo(0x1A0B29, 0x10BB34),
    ],
    "Single Chamber Top Right": [
        RoomSpriteInfo(0x1A0AA9, 0x10B81C),  # Pop	NO	7AD5E [Standard]
    ],
    "Warehouse Zeela Room Left": [
        RoomSpriteInfo(0x1A03E3, 0x10941F),  # Pop	BR	7A471 [Standard]
        RoomSpriteInfo(0x1A050D, 0x10988E),  # Pop	BR	7A4B1 [Standard]
        RoomSpriteInfo(0x1A0533, 0x1098F7),  # Pop	BR	7A4DA [Standard]
    ],
    "KraidRoomOut": [
        RoomSpriteInfo(0x1A0651, 0x10A0BA),  # Pop	BR	7A521 [Standard]
        RoomSpriteInfo(0x1A062D, 0x109FA4),  # Pop	BR	7A56B [Standard]
    ],
    "Etecoons Bottom": [
        RoomSpriteInfo(0x1A04E5, 0x109778),  # Pop	BR	7A011 [Standard]
    ],
    "Grapple Escape": [
        RoomSpriteInfo(0x1A08BF, 0x10AD8F),  # Pop	NO	7AA0E [Standard]
    ],
    "Business Center": [
        RoomSpriteInfo(0x1A0AED, 0x10B9D8),  # Pop	NO	7A7DE [Standard]
        RoomSpriteInfo(0x1A09CB, 0x10B3C5),  # Pop	NO	7AA41 [Standard]
        RoomSpriteInfo(0x1A0A5B, 0x10B6AD),  # Pop	NO	7A8B9 [Standard]
        RoomSpriteInfo(0x1A0A01, 0x10B48E),  # Pop	NO	7A865 [Standard]
        RoomSpriteInfo(0x1A09F3, 0x10B45B),  # Pop	NO	7A75D [Standard]
        RoomSpriteInfo(0x1A06D5, 0x10A332),  # Pop	NO	7A815 [Standard]
        RoomSpriteInfo(0x1A097D, 0x10B1F6),  # Pop	NO	7A8F8 [Standard]
    ],
    "Caterpillar Room Top Right": [
        RoomSpriteInfo(0x1A063F, 0x10A057),  # Pop	BR	7A322 [Standard]
    ],
    "Red Brinstar Elevator": [
        RoomSpriteInfo(0x1A061F, 0x109F61),  # Pop	BR	7A3AE [Standard]
        RoomSpriteInfo(0x1A063F, 0x10A057),  # Pop	BR	7A322 [Standard]
        RoomSpriteInfo(0x1A034F, 0x1090C7),  # Pop	BR	7A37C [Standard]
    ],
    "Red Tower Top Left": [
        RoomSpriteInfo(0x1A05D3, 0x109E2F),  # Pop	BR	7A2F7 [Standard]
        RoomSpriteInfo(0x1A03F1, 0x109452),  # Pop	BR	7A253 [Standard]
    ],
    "East Tunnel Right": [
        RoomSpriteInfo(0x1A0671, 0x10A110),  # Pop	BR	7A3DD [Standard]
        RoomSpriteInfo(0x1A0449, 0x1095E4),  # Pop	BR	7A408 [Standard]
    ],
    "East Tunnel Top Right": [
        RoomSpriteInfo(0x1A0E96, 0x10D53F),  # Pop	MA	7CF80 [Standard]
    ],
    "Crab Shaft Right": [
        RoomSpriteInfo(0x1A0D77, 0x10CFC3),  # Pop	MA	7D1A3 [Standard]
    ],
    "Crab Shaft Left": [
        RoomSpriteInfo(0x1A0D77, 0x10CFC3),  # Pop	MA	7D1A3 [Standard]
        # RoomSpriteInfo(0x1A0D41, 0x10CE6A),  # Pop	MA	7D0B9 [Standard]
        # RoomSpriteInfo(0x1A109E, 0x10E07F),  # Pop	MA	7D017 [Standard]
        # RoomSpriteInfo(0x1A103A, 0x10DE6D),  # Pop	MA	7CFC9 [Standard]
    ],
    "Aqueduct Top Left": [
        RoomSpriteInfo(0x1A0E1E, 0x10D357),  # Pop	MA	7D5A7 [Standard]
    ],
    "Aqueduct Bottom": [
        RoomSpriteInfo(0x1A0E1E, 0x10D357),  # Pop	MA	7D5A7 [Standard]
        RoomSpriteInfo(0x1A0FA2, 0x10DC6F),  # Pop	MA	7D617 [Standard]
        RoomSpriteInfo(0x1A0FD4, 0x10DD38),  # Pop	MA	7D6FD [Standard]
    ],
    "Aqueduct": [
        RoomSpriteInfo(0x1A0E1E, 0x10D357),  # Pop	MA	7D5A7 [Standard]
    ],
    "Right Sandpit": [
        RoomSpriteInfo(0x1A105E, 0x10DF63),  # Pop	MA	7D51E [Standard]
    ],
    "Oasis Bottom": [
        RoomSpriteInfo(0x1A0F6A, 0x10DAD3),  # Pop	MA	7D4C2 [Standard]
        RoomSpriteInfo(0x1A0F52, 0x10DA3D),  # Pop	MA	7D461 [Standard]
        RoomSpriteInfo(0x1A0FB8, 0x10DCE2),  # Pop	MA	7D69A [Standard]
        RoomSpriteInfo(0x1A0E5E, 0x10D453),  # Pop	MA	7D646 [Standard]
    ],
    "West Sand Hall Left": [
        RoomSpriteInfo(0x1A0F52, 0x10DA3D),  # Pop	MA	7D461 [Standard]
        RoomSpriteInfo(0x1A0EEC, 0x10D7EE),  # Pop	MA	7D252 [Standard]
    ],
    "Cathedral": [
        RoomSpriteInfo(0x1A092B, 0x10AF87),  # Pop	NO	7A7B3 [Standard]
        RoomSpriteInfo(0x1A0A25, 0x10B544),  # Pop	NO	7A788 [Standard]
    ],
    "Toilet Top": [
        RoomSpriteInfo(0x1A0D85, 0x10D006),  # Pop	MA	7D30B [Standard]
        RoomSpriteInfo(0x1A0F0C, 0x10D864),  # Pop	MA	7D2D9 [Standard]
        RoomSpriteInfo(0x1A104C, 0x10DF30),  # Pop  MA  7D433 [Standard]
        RoomSpriteInfo(0x1A0F22, 0x10D957),  # Pop	MA	7D340 [Standard]
        RoomSpriteInfo(0x1A0FE6, 0x10DD9B),  # Pop	MA	7D387 [Standard]
        RoomSpriteInfo(0x1A0E42, 0x10D3ED),  # Pop	MA	7D2AA [Standard]
        RoomSpriteInfo(0x1A0EFA, 0x10D801),  # Pop	MA	7D27E [Standard]
        RoomSpriteInfo(0x1A0F94, 0x10DC3C),  # Pop	MA	7D5EC [Standard]
        RoomSpriteInfo(0x1A0DE3, 0x10D1BB),  # Pop	MA	7D86E [Standard]
    ],
    "Post Botwoon": [
        RoomSpriteInfo(0x1A0DB9, 0x10D112),  # Pop	MA	7D7E4 [Standard]
        RoomSpriteInfo(0x1A0D53, 0x10CF2D),  # Pop	MA	7D913 [Standard]
        RoomSpriteInfo(0x1A108C, 0x10E01C),  # Pop	MA	7DA2B [Standard]
        RoomSpriteInfo(0x1A107A, 0x10DFD9),  # Pop	MA	7D9FE [Standard]
        RoomSpriteInfo(0x1A0DF1, 0x10D1EE),  # Pop	MA	7D898 [Standard]
    ],
    "Beach": [
        RoomSpriteInfo(0x1A0ED6, 0x10D75B),  # Pop	MA	7D1DD [Standard]
        RoomSpriteInfo(0x1A0EC4, 0x10D698),  # Pop	MA	7D16D [Standard]
    ],
    "Watering Hole": [
        RoomSpriteInfo(0x1A0D65, 0x10CF90),  # Pop	MA	7D13B [Standard]
    ],
    "Main Street Bottom": [
        RoomSpriteInfo(0x1A0D41, 0x10CE6A),  # Pop	MA	7D0B9 [Standard]
        RoomSpriteInfo(0x1A109E, 0x10E07F),  # Pop	MA	7D017 [Standard]
        RoomSpriteInfo(0x1A103A, 0x10DE6D),  # Pop	MA	7CFC9 [Standard]
    ],
    "Colosseum Top Right": [
        RoomSpriteInfo(0x1A0D97, 0x10D089),  # Pop	MA	7D72A [Standard]
    ],
    "Kronic Boost Room Bottom Left": [
        RoomSpriteInfo(0x1A08E9, 0x10AEA8),  # Pop	NO	7AEDF [Standard]
        RoomSpriteInfo(0x1A06C7, 0x10A2DF),  # Pop	NO	7B051 [Standard]
        RoomSpriteInfo(0x1A0887, 0x10AC53),  # Pop	NO	7AEB4 [Standard]
        RoomSpriteInfo(0x1A0ADF, 0x10B995),  # Pop	NO	7AE74 [Standard]
        RoomSpriteInfo(0x1A0A7B, 0x10B733),  # Pop	NO	7AE07 [Standard]
        RoomSpriteInfo(0x1A0B29, 0x10BB34),  # Pop	NO	7AE32 [Standard]
    ],
    "Left Sandpit": [
        RoomSpriteInfo(0x1A106C, 0x10DF96),  # Pop	MA	7D4EF [Standard]
    ],
    "Crab Hole Bottom Left": [
        RoomSpriteInfo(0x1A101A, 0x10DE17),  # Pop	MA	7D21C [Standard]
    ],
    "Golden Four": [
        RoomSpriteInfo(0x1A10B0, 0x10E102),  # Pop	TO	7DEDE [Standard]
        RoomSpriteInfo(0x1A10CC, 0x10E1D8),  # Pop	TO	7DAE1 [Standard]
        RoomSpriteInfo(0x1A116C, 0x10E516),  # Pop	TO	7DAE1 [Events 1]
        RoomSpriteInfo(0x1A10DE, 0x10E25B),  # Pop	TO	7DC65 [Standard/Events 1]
        RoomSpriteInfo(0x1A1122, 0x10E387),  # Pop	TO	7DC19 [Standard/Events 1]
        RoomSpriteInfo(0x1A1148, 0x10E440),  # Pop	TO	7DB31 [Standard]
        RoomSpriteInfo(0x1A117A, 0x10E559),  # Pop	TO	7DB31 [Events 1]
        RoomSpriteInfo(0x1A115A, 0x10E4A3),  # Pop	TO	7DBCD [Standard]
        RoomSpriteInfo(0x1A11A4, 0x10E652),  # Pop	TO	7DBCD [Events 1]
        RoomSpriteInfo(0x1A1188, 0x10E59C),  # Pop	TO	7DE7A [Standard]
        RoomSpriteInfo(0x1A1196, 0x10E5BF),  # Pop	TO	7DB7D [Events 1]
        RoomSpriteInfo(0x1A11F8, 0x10E794),  # Pop	TO	7DB7D [Standard]
        RoomSpriteInfo(0x1A11B2, 0x10E695),  # Pop	TO	7DEA7 [Standard]
        RoomSpriteInfo(0x1A120A, 0x10E857),  # Pop	TO	7DDF3 [Standard]
    ],
}
