class RoomSpriteInfo:
    __slots__ = ('header', 'spriteData')

    def __init__(self, header, spriteData):
        self.header = header
        self.spriteData = spriteData

    
def getTourianRooms() -> list[RoomSpriteInfo]:
    return [
        RoomSpriteInfo(0x1A10B0, 0x10E102), # Pop	TO	7DEDE [Standard]
        RoomSpriteInfo(0x1A10CC, 0x10E1D8), # Pop	TO	7DAE1 [Standard]
        RoomSpriteInfo(0x1A116C, 0x10E516), # Pop	TO	7DAE1 [Events 1]
        RoomSpriteInfo(0x1A10DE, 0x10E25B), # Pop	TO	7DC65 [Standard/Events 1]
        RoomSpriteInfo(0x1A1122, 0x10E387), # Pop	TO	7DC19 [Standard/Events 1]
        RoomSpriteInfo(0x1A1148, 0x10E440), # Pop	TO	7DB31 [Standard]
        RoomSpriteInfo(0x1A117A, 0x10E559), # Pop	TO	7DB31 [Events 1]
        RoomSpriteInfo(0x1A115A, 0x10E4A3), # Pop	TO	7DBCD [Standard]
        RoomSpriteInfo(0x1A11A4, 0x10E652), # Pop	TO	7DBCD [Events 1]
        RoomSpriteInfo(0x1A1188, 0x10E59C), # Pop	TO	7DE7A [Standard]
        RoomSpriteInfo(0x1A1196, 0x10E5BF), # Pop	TO	7DB7D [Events 1]
        RoomSpriteInfo(0x1A11F8, 0x10E794), # Pop	TO	7DB7D [Standard]
        RoomSpriteInfo(0x1A11B2, 0x10E695), # Pop	TO	7DEA7 [Standard]
        RoomSpriteInfo(0x1A120A, 0x10E857), # Pop	TO	7DDF3 [Standard]
    ]
