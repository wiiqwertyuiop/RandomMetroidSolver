class RoomSpriteInfo:
    __slots__ = ('header', 'spriteData', 'numbOfEnemies', 'doorSpawn')

    def __init__(self, header, spriteData, numbOfEnemies=[99, 99, 99, 99], doorSpawn=False) -> None:
        self.header = header
        self.spriteData = spriteData
        self.numbOfEnemies=numbOfEnemies
        self.doorSpawn = doorSpawn

SpritePathConnector = {
"Landing Site": [
  RoomSpriteInfo(1704325, 1083130, numbOfEnemies=[20, 99, 99, 99], doorSpawn=True),     # Pop  CR  792FD [Standard]
  RoomSpriteInfo(1704039, 1081953, numbOfEnemies=[11, 3, 2, 99]),       # Pop  CR  792FD [Awake]
  RoomSpriteInfo(1704061, 1082212, numbOfEnemies=[12, 99, 99, 99]),       # Pop  CR  79879 [Standard]
  RoomSpriteInfo(1704543, 1084295, numbOfEnemies=[3, 1, 99, 99]),        # Pop  CR  798E2 [Standard]
  RoomSpriteInfo(1704003, 1081755, numbOfEnemies=[6, 99, 99, 99]),        # Pop  CR  79A44 [Events 1]
  RoomSpriteInfo(1704021, 1081854, numbOfEnemies=[6, 99, 99, 99]),        # Pop  CR  79A44 [Standard]
  RoomSpriteInfo(1703985, 1081608, numbOfEnemies=[3, 6, 99, 99]),        # Pop  CR  7990D [Standard]
  RoomSpriteInfo(1704271, 1082849, numbOfEnemies=[10, 99, 99, 99]),       # Pop  CR  796BA [Standard]
  RoomSpriteInfo(1704403, 1083593, numbOfEnemies=[11, 99, 99, 99]),       # Pop  CR  796BA [Awake]
  RoomSpriteInfo(1704885, 1086246, numbOfEnemies=[3, 4, 99, 99]),        # Pop  BR  79E9F [Standard]
  RoomSpriteInfo(1704913, 1086380, numbOfEnemies=[2, 4, 99, 99]),        # Pop  BR  79E9F [Standard]
  RoomSpriteInfo(1705365, 1088454, numbOfEnemies=[10, 5, 99, 99], doorSpawn=True),     # Pop  BR  79F11 [Standard]
  RoomSpriteInfo(1704823, 1085837, numbOfEnemies=[2, 5, 99, 99], doorSpawn=True),      # Pop  BR  79F11 [Events 1]
  RoomSpriteInfo(1704463, 1083925, numbOfEnemies=[10, 99, 99, 99]),       # Pop  CR  7975C [Standard]
  RoomSpriteInfo(1704079, 1082407, numbOfEnemies=[4, 1, 99, 99]),        # Pop  CR  7975C [Awake]
  RoomSpriteInfo(1703967, 1081557, numbOfEnemies=[3, 99, 99, 99]),        # Pop  CR  793AA [Standard]
  RoomSpriteInfo(1704445, 1083890, numbOfEnemies=[1, 1, 99, 99]),        # Pop  CR  7965B [Standard]
  RoomSpriteInfo(1704097, 1082490, numbOfEnemies=[4, 3, 99, 99]),        # Pop  CR  792B3 [Standard]
],                                                                                  
"Blue Brinstar Elevator Bottom": [                                                  
  RoomSpriteInfo(1704885, 1086246, numbOfEnemies=[3, 4, 99, 99]),        # Pop  BR  79E9F [Standard]
  RoomSpriteInfo(1704913, 1086380, numbOfEnemies=[2, 4, 99, 99]),        # Pop  BR  79E9F [Standard]
  RoomSpriteInfo(1705365, 1088454, numbOfEnemies=[10, 5, 99, 99]),       # Pop  BR  79F11 [Standard]
  RoomSpriteInfo(1704823, 1085837, numbOfEnemies=[2, 5, 99, 99]),        # Pop  BR  79F11 [Events 1]
  RoomSpriteInfo(1704841, 1085952, numbOfEnemies=[2, 2, 5, 99], doorSpawn=True),        # Pop  BR  79F64 [Events 1]
  RoomSpriteInfo(1704967, 1086725, numbOfEnemies=[3, 99, 99, 99]),        # Pop  BR  7A1AD [Standard]
],                                                                                  
"Gauntlet Top": [                                                                   
  RoomSpriteInfo(0x1A01FD, 0x1089F2),  # Pop	CR	7965B [Standard]   # Pop  CR  7965B [Standard]
  RoomSpriteInfo(0x1A00A1, 0x10847A),  # Pop	CR	792B3 [Standard]   # Pop  CR  792B3 [Standard]
],                                                                                  
"Lower Mushrooms Left": [                                                           
  RoomSpriteInfo(1704561, 1084362, numbOfEnemies=[2, 2, 99, 99]),        # Pop  CR  79969 [Standard]
],                                                                                  
"Green Pirates Shaft Bottom Right": [                                               
  RoomSpriteInfo(1704129, 1082624, numbOfEnemies=[5, 2, 99, 99]),        # Pop  CR  799BD [Standard]
  RoomSpriteInfo(1704561, 1084362, numbOfEnemies=[2, 2, 99, 99]),        # Pop  CR  79969 [Standard]
],                                                                                  
"Moat Right": [                                                                     
  RoomSpriteInfo(1704639, 1085209, numbOfEnemies=[2, 2, 99, 99]),        # Pop  CR  7948C [Standard]
],                                                                                  
"Moat Left": [                                                                      
  RoomSpriteInfo(1704639, 1085209, numbOfEnemies=[2, 2, 99, 99]),        # Pop  CR  7948C [Standard]
],                                                                                  
"Keyhunter Room Bottom": [                                                          
  RoomSpriteInfo(1704639, 1085209, numbOfEnemies=[2, 2, 99, 99]),        # Pop  CR  7948C [Standard]
],                                                                                  
"Morph Ball Room Left": [                                                           
  RoomSpriteInfo(1704885, 1086246, numbOfEnemies=[3, 4, 99, 99]),        # Pop  BR  79E9F [Standard]
  RoomSpriteInfo(1704913, 1086380, numbOfEnemies=[2, 4, 99, 99]),        # Pop  BR  79E9F [Standard]
],                                                                                  
"Green Brinstar Elevator": [                                                        
  RoomSpriteInfo(1705281, 1087866, numbOfEnemies=[5, 2, 3, 99]),        # Pop  BR  79AD9 [Standard]
  RoomSpriteInfo(1704661, 1085308, numbOfEnemies=[1, 3, 99, 99]),        # Pop  BR  79B9D [Standard]
  RoomSpriteInfo(1705161, 1087202, numbOfEnemies=[5, 99, 99, 99]),        # Pop  BR  79C5E [Standard]
  RoomSpriteInfo(1705175, 1087285, numbOfEnemies=[4, 99, 99, 99]),        # Pop  BR  79FE5 [Standard]
  RoomSpriteInfo(1705317, 1088064, numbOfEnemies=[5, 4, 1, 99]),        # Pop  BR  79BC8 [Standard]
  RoomSpriteInfo(1705401, 1088860, numbOfEnemies=[2, 3, 3, 5]),        # Pop  BR  79CB3 [Standard]
],                                                                                  
"Big Pink": [                                                                       
  RoomSpriteInfo(1705001, 1086782, numbOfEnemies=[3, 4, 3, 99]),        # Pop  BR  79D19 [Standard]
  RoomSpriteInfo(1704699, 1085381, numbOfEnemies=[3, 99, 99, 99]),        # Pop  BR  79D9C [Standard]
  RoomSpriteInfo(1705207, 1087483, numbOfEnemies=[1, 2, 99, 99]),        # Pop  BR  7A130 [Standard]
  RoomSpriteInfo(1705071, 1087005, numbOfEnemies=[2, 99, 99, 99]),        # Pop  BR  79E11 [Standard]
  RoomSpriteInfo(1704801, 1085722, numbOfEnemies=[2, 3, 2, 99]),        # Pop  BR  7A0D2 [Standard]
  RoomSpriteInfo(1705303, 1088045, numbOfEnemies=[1, 99, 99, 99]),        # Pop  BR  79B5B [Standard]
  RoomSpriteInfo(1704737, 1085486, numbOfEnemies=[3, 2, 99, 99]),        # Pop  BR  7A0A4 [Standard]
],                                                                                  
"Green Hill Zone Top Right": [                                                      
  RoomSpriteInfo(1705383, 1088697, numbOfEnemies=[5, 5, 99, 99]),        # Pop  BR  79E52 [Standard]
],                                                                                  
"Noob Bridge Right": [                                                              
  RoomSpriteInfo(1704867, 1086115, numbOfEnemies=[4, 4, 99, 99]),        # Pop  BR  79FBA [Standard]
],                                                                                  
"West Ocean Left": [                                                                
  RoomSpriteInfo(1704289, 1083012, numbOfEnemies=[2, 1, 1, 3]),        # Pop  CR  793FE [Standard]
],                                                                                  
"Wrecked Ship Main": [                                                              
  RoomSpriteInfo(1704289, 1083012, numbOfEnemies=[5, 1, 1, 99]),        # Pop  CR  793FE [Standard]
  RoomSpriteInfo(1706861, 1096864, numbOfEnemies=[1, 20, 4, 2]),       # Pop  WS  7CAF6 [Standard]
  RoomSpriteInfo(1707307, 1101079, numbOfEnemies=[9, 4, 4, 99]),        # Pop  WS  7CAF6 [Bosses]
  RoomSpriteInfo(1706905, 1097702, numbOfEnemies=[4, 4, 9, 99]),        # Pop  WS  7CA52 [Bosses]
  RoomSpriteInfo(1707177, 1099506, numbOfEnemies=[1, 19, 9, 99]),       # Pop  WS  7CA52 [Standard]
  RoomSpriteInfo(1706829, 1096762, numbOfEnemies=[1, 99, 99, 99]),        # Pop  WS  7CD5C [Bosses]
  RoomSpriteInfo(1706979, 1098149, numbOfEnemies=[0, 99, 99, 99]),        # Pop  WS  7CD5C [Standard]
  RoomSpriteInfo(1707199, 1099973, numbOfEnemies=[1, 20, 2, 4]),       # Pop  WS  7CDF1 [Standard]
  RoomSpriteInfo(1707271, 1100881, numbOfEnemies=[2, 2, 4, 99]),        # Pop  WS  7CDF1 [Bosses]
  RoomSpriteInfo(1707027, 1098209, numbOfEnemies=[0, 99, 99, 99]),        # Pop  WS  7CAAE [Standard]
  RoomSpriteInfo(1707131, 1099241, numbOfEnemies=[8, 3, 99, 99]),        # Pop  WS  7CAAE [Bosses]
  RoomSpriteInfo(1707257, 1100718, numbOfEnemies=[5, 99, 99, 99]),        # Pop  WS  7CB8B [Bosses]
  RoomSpriteInfo(1706969, 1098146, numbOfEnemies=[0, 99, 99, 99]),        # Pop  WS  7CB8B [Standard]
  RoomSpriteInfo(1707117, 1098726, numbOfEnemies=[32, 99, 99, 99]),       # Pop  WS  7CA08 [Standard]
],                                                                                  
"Wrecked Ship Back": [                                                              
  RoomSpriteInfo(1706843, 1096781, numbOfEnemies=[2, 3, 99, 99]),        # Pop  WS  7CC27 [Bosses]
],                                                                                  
"PhantoonRoomOut": [                                                                
  RoomSpriteInfo(1707099, 1098371, numbOfEnemies=[20, 2, 99, 99]),       # Pop  WS  7CC6F [Standard]
  RoomSpriteInfo(1706927, 1098041, numbOfEnemies=[2, 3, 1, 99]),        # Pop  WS  7CC6F [Bosses]
],                                                                                  
"Bowling": [                                                                        
  RoomSpriteInfo(1704417, 1083772, numbOfEnemies=[3, 3, 99, 99]),        # Pop  CR  79461 [Standard]
  RoomSpriteInfo(1707009, 1098158, numbOfEnemies=[1, 2, 99, 99]),        # Pop  WS  7C98E [Bosses]
  RoomSpriteInfo(1704385, 1083574, numbOfEnemies=[1, 99, 99, 99]),        # Pop  CR  7968F [Standard])
],                                                                                  
"Crab Maze Left": [                                                                 
  RoomSpriteInfo(0x1A0221, 0x108AB8),                                  # Pop  CR  7957D [Standard]
  RoomSpriteInfo(0x1A023D, 0x108B3E),                                  # Pop  CR  79552 [Standard]
  RoomSpriteInfo(0x1A0009, 0x108002),                                  # Pop  CR  794FD [Standard]
],                                                                                  
"Lava Dive Right": [                                                                
  RoomSpriteInfo(1706147, 1092873, numbOfEnemies=[6, 99, 99, 99]),        # Pop  NO  7AF14 [Standard]
],                                                                                  
"LN Entrance": [                                                                    
  RoomSpriteInfo(1705649, 1090108, numbOfEnemies=[1, 3, 6, 99]),        # Pop  NO  7B1E5 [Standard]
  RoomSpriteInfo(1706301, 1093610, numbOfEnemies=[10, 8, 99, 99]),       # Pop  NO  7B236 [Standard]
  RoomSpriteInfo(1705767, 1090801, numbOfEnemies=[2, 1, 2, 99]),        # Pop  NO  7B3A5 [Standard]
  RoomSpriteInfo(1706161, 1092972, numbOfEnemies=[2, 99, 99, 99]),        # Pop  NO  7B457 [Standard]
  RoomSpriteInfo(1705829, 1090912, numbOfEnemies=[5, 7, 99, 99]),        # Pop  NO  7B40A [Standard]
  RoomSpriteInfo(1705973, 1091630, numbOfEnemies=[5, 3, 3, 99]),        # Pop  NO  7B4AD [Standard]
  RoomSpriteInfo(1706269, 1093364, numbOfEnemies=[9, 99, 99, 99]),        # Pop  NO  7B4E5 [Standard]
  RoomSpriteInfo(1705725, 1090600, numbOfEnemies=[3, 99, 99, 99]),        # Pop  NO  7B585 [Standard]
],                                                                                  
"LN Above GT": [                                                                    
],                                                                                  
"Firefleas": [                                                                      
  RoomSpriteInfo(1706097, 1092480, numbOfEnemies=[5, 3, 5, 99]),        # Pop  NO  7B6EE [Standard]
  RoomSpriteInfo(1706747, 1096267, numbOfEnemies=[4, 3, 99, 99]),        # Pop  NO  7B656 [Standard]
  RoomSpriteInfo(1706193, 1093202, numbOfEnemies=[5, 99, 99, 99]),        # Pop  NO  7B510 [Standard]
],                                                                                  
"Crocomire Room Top": [                                                             
  RoomSpriteInfo(1706323, 1093917, numbOfEnemies=[5, 4, 4, 99]),        # Pop  NO  7AB8F [Standard]
  RoomSpriteInfo(1705951, 1091515, numbOfEnemies=[5, 1, 1, 99]),        # Pop  NO  7AA82 [Standard]
  RoomSpriteInfo(1705621, 1090006, numbOfEnemies=[4, 99, 99, 99]),        # Pop  NO  7AB07 [Standard]
  RoomSpriteInfo(1706515, 1094865, numbOfEnemies=[2, 5, 99, 99]),        # Pop  NO  7AB3B [Standard]
  RoomSpriteInfo(1706423, 1094591, numbOfEnemies=[0, 99, 99, 99]),        # Pop  NO  7AC00 [Standard]
  RoomSpriteInfo(1706569, 1095290, numbOfEnemies=[3, 99, 99, 99]),        # Pop  NO  7ABD2 [Standard]
  RoomSpriteInfo(1705603, 1089843, numbOfEnemies=[5, 5, 99, 99]),        # Pop  NO  7AB64 [Standard]
],                                                                                  
"Three Muskateers Room Left": [                                                     
  RoomSpriteInfo(1706747, 1096267, numbOfEnemies=[4, 3, 99, 99]),        # Pop  NO  7B656 [Standard]
  RoomSpriteInfo(1706193, 1093202, numbOfEnemies=[5, 99, 99, 99]),        # Pop  NO  7B510 [Standard]
],                                                                                  
"Wasteland": [                                                                      
  RoomSpriteInfo(1705725, 1090600, numbOfEnemies=[3, 99, 99, 99]),        # Pop  NO  7B585 [Standard]
  RoomSpriteInfo(1706379, 1094233, numbOfEnemies=[4, 4, 2, 99]),        # Pop  NO  7B5D5 [Standard]
],                                                                                  
"Ridley Zone": [                                                                    
  RoomSpriteInfo(1706379, 1094233, numbOfEnemies=[4, 4, 2, 99]),        # Pop  NO  7B5D5 [Standard]
  RoomSpriteInfo(1705635, 1090073, numbOfEnemies=[2, 99, 99, 99]),        # Pop  NO  7B62B [Standard]
  RoomSpriteInfo(1706079, 1092237, numbOfEnemies=[12, 3, 99, 99]),       # Pop  NO  7B482 [Standard]
],                                                                                  
"RidleyRoomOut": [                                                                  
  RoomSpriteInfo(1706647, 1095529, numbOfEnemies=[5, 6, 99, 99]),        # Pop  NO  7B37A [Standard]
],                                                                                  
"Crocomire Speedway Bottom": [                                                      
  RoomSpriteInfo(1706053, 1092058, numbOfEnemies=[5, 4, 2, 99]),        # Pop  NO  7A923 [Standard]
  RoomSpriteInfo(1706405, 1094444, numbOfEnemies=[5, 4, 99, 99]),        # Pop  NO  7AFCE [Standard]
  RoomSpriteInfo(1706035, 1091943, numbOfEnemies=[3, 4, 99, 99]),        # Pop  NO  7B139 [Standard]
  RoomSpriteInfo(1706811, 1096663, numbOfEnemies=[1, 5, 99, 99]),        # Pop  NO  7AF72 [Standard]
],                                                                                  
"Bubble Mountain Bottom": [                                                         
  RoomSpriteInfo(1706457, 1094616, numbOfEnemies=[1, 3, 3, 1]),        # Pop  NO  7ACB3 [Standard]
],                                                                                  
"Bubble Mountain": [                                                                
  RoomSpriteInfo(1706457, 1094616, numbOfEnemies=[1, 3, 3, 1]),        # Pop  NO  7ACB3 [Standard]
  RoomSpriteInfo(1705929, 1091240, numbOfEnemies=[4, 5, 8, 99]),        # Pop  NO  7AFA3 [Standard]
  RoomSpriteInfo(1706533, 1094980, numbOfEnemies=[6, 4, 99, 99]),        # Pop  NO  7A788 [Standard]
  RoomSpriteInfo(1706283, 1093511, numbOfEnemies=[4, 2, 99, 99]),        # Pop  NO  7A7B3 [Standard]
  RoomSpriteInfo(1706551, 1095143, numbOfEnemies=[6, 3, 99, 99]),        # Pop  NO  7AC5A [Standard]
  RoomSpriteInfo(1706247, 1093297, numbOfEnemies=[2, 99, 99, 99]),        # Pop  NO  7AC83 [Standard]
],                                                                                  
"Bubble Mountain Top": [                                                            
  RoomSpriteInfo(1706457, 1094616, numbOfEnemies=[1, 3, 3, 1]),        # Pop  NO  7ACB3 [Standard]
  RoomSpriteInfo(1706683, 1095823, numbOfEnemies=[6, 2, 99, 99]),        # Pop  NO  7ACF0 [Standard]
  RoomSpriteInfo(1706701, 1095954, numbOfEnemies=[5, 3, 99, 99]),        # Pop  NO  7B07A [Standard]
  RoomSpriteInfo(1706551, 1095143, numbOfEnemies=[6, 3, 99, 99]),        # Pop  NO  7AC5A [Standard]
  RoomSpriteInfo(1706247, 1093297, numbOfEnemies=[2, 99, 99, 99]),        # Pop  NO  7AC83 [Standard]
  RoomSpriteInfo(1705995, 1091809, numbOfEnemies=[2, 4, 1, 1]),        # Pop  NO  7ADAD [Standard]
  RoomSpriteInfo(1706619, 1095475, numbOfEnemies=[2, 99, 99, 99]),        # Pop  NO  7AE07 [Standard]
  RoomSpriteInfo(1706793, 1096500, numbOfEnemies=[6, 4, 99, 99]),        # Pop  NO  7AE32 [Standard]
],                                                                                  
"Single Chamber Top Right": [                                                       
  RoomSpriteInfo(1706665, 1095708, numbOfEnemies=[3, 4, 99, 99]),        # Pop  NO  7AD5E [Standard]
],                                                                                  
"Warehouse Zeela Room Left": [                                                      
  RoomSpriteInfo(1704931, 1086495, numbOfEnemies=[3, 99, 99, 99]),        # Pop  BR  7A471 [Standard]
  RoomSpriteInfo(1705229, 1087630, numbOfEnemies=[4, 99, 99, 99]),        # Pop  BR  7A4B1 [Standard]
  RoomSpriteInfo(1705267, 1087735, numbOfEnemies=[4, 99, 99, 99]),        # Pop  BR  7A4DA [Standard]
],                                                                                  
"KraidRoomOut": [                                                                   
  RoomSpriteInfo(1705553, 1089722, numbOfEnemies=[3, 1, 99, 99]),        # Pop  BR  7A521 [Standard]
  RoomSpriteInfo(1705517, 1089444, numbOfEnemies=[1, 10, 99, 99]),       # Pop  BR  7A56B [Standard]
],                                                                                  
"Etecoons Bottom": [                                                                
  RoomSpriteInfo(1705189, 1087352, numbOfEnemies=[3, 5, 99, 99]),        # Pop  BR  7A011 [Standard]
],                                                                                  
"Grapple Escape": [                                                                 
  RoomSpriteInfo(1706175, 1093007, numbOfEnemies=[10, 2, 99, 99]),       # Pop  NO  7AA0E [Standard]
],                                                                                  
"Business Center": [                                                                
  RoomSpriteInfo(1706733, 1096152, numbOfEnemies=[6, 99, 99, 99]),        # Pop  NO  7A7DE [Standard]
  RoomSpriteInfo(1706443, 1094597, numbOfEnemies=[1, 99, 99, 99]),        # Pop  NO  7AA41 [Standard]
  RoomSpriteInfo(1706587, 1095341, numbOfEnemies=[3, 4, 99, 99]),        # Pop  NO  7A8B9 [Standard]
  RoomSpriteInfo(1706497, 1094798, numbOfEnemies=[3, 1, 99, 99]),        # Pop  NO  7A865 [Standard]
  RoomSpriteInfo(1706483, 1094747, numbOfEnemies=[3, 99, 99, 99]),        # Pop  NO  7A75D [Standard]
  RoomSpriteInfo(1705685, 1090354, numbOfEnemies=[3, 6, 1, 99]),        # Pop  NO  7A815 [Standard]
  RoomSpriteInfo(1706365, 1094134, numbOfEnemies=[6, 99, 99, 99]),        # Pop  NO  7A8F8 [Standard]
],                                                                                  
"Caterpillar Room Top Right": [                                                     
  RoomSpriteInfo(0x1A063F, 0x10A057),  # Pop  BR  7A322 [Standard]     # Pop  BR  7A322 [Standard]
],                                                                                  
"Red Tower Top Left": [                                                             
  RoomSpriteInfo(1705427, 1089071, numbOfEnemies=[4, 4, 99, 99]),        # Pop  BR  7A3AE [Standard]
  RoomSpriteInfo(1704945, 1086546, numbOfEnemies=[8, 1, 2, 99]),        # Pop  BR  7A322 [Standard]
],                                                                     # Pop  BR  7A37C [Standard]
"East Tunnel Right": [                                                              
  RoomSpriteInfo(1705585, 1089808, numbOfEnemies=[2, 99, 99, 99]),                     
  RoomSpriteInfo(1705033, 1086948, numbOfEnemies=[2, 1, 99, 99]),        # Pop  BR  7A2F7 [Standard]
],                                                                     # Pop  BR  7A253 [Standard]
"Red Brinstar Elevator": [                                                          
  RoomSpriteInfo(1705503, 1089377, numbOfEnemies=[4, 99, 99, 99]),                     
  RoomSpriteInfo(1705535, 1089623, numbOfEnemies=[3, 2, 99, 99]),        # Pop  BR  7A3DD [Standard]
  RoomSpriteInfo(1704783, 1085639, numbOfEnemies=[2, 3, 99, 99]),        # Pop  BR  7A408 [Standard]
],                                                                                  
"Main Street Bottom": [                                                             
  RoomSpriteInfo(1707329, 1101418, numbOfEnemies=[6, 6, 99, 99]),        # Pop  MA  7CF80 [Standard]
  RoomSpriteInfo(1708190, 1106047, numbOfEnemies=[4, 4, 99, 99]),                     
  RoomSpriteInfo(1708090, 1105517, numbOfEnemies=[5, 7, 99, 99]),                     
],                                                                     # Pop  MA  7D1A3 [Standard]
"Crab Shaft Left": [                                                                
  RoomSpriteInfo(1707383, 1101763, numbOfEnemies=[4, 99, 99, 99]),                     
],                                                                     # Pop  MA  7D1A3 [Standard]
"Crab Shaft Right": [                                                               
  RoomSpriteInfo(1707383, 1101763, numbOfEnemies=[4, 99, 99, 99]),                     
],                                                                     # Pop  MA  7D5A7 [Standard]
"Aqueduct Top Left": [                                                              
  RoomSpriteInfo(1707550, 1102679, numbOfEnemies=[5, 99, 99, 99]),                     
],                                                                     # Pop  MA  7D5A7 [Standard]
"Aqueduct Bottom": [                                                   # Pop  MA  7D617 [Standard]
  RoomSpriteInfo(1707550, 1102679, numbOfEnemies=[5, 99, 99, 99]),        # Pop  MA  7D6FD [Standard]
  RoomSpriteInfo(1707938, 1105007, numbOfEnemies=[5, 2, 99, 99]),                     
  RoomSpriteInfo(1707988, 1105208, numbOfEnemies=[5, 1, 99, 99]),                     
],                                                                     # Pop  MA  7D5A7 [Standard]
"Aqueduct": [                                                                       
  RoomSpriteInfo(1707550, 1102679, numbOfEnemies=[5, 99, 99, 99]),                     
],                                                                     # Pop  MA  7D51E [Standard]
"Left Sandpit": [                                                                   
  RoomSpriteInfo(1708140, 1105814, numbOfEnemies=[4, 99, 99, 99]),                     
],                                                                     # Pop  MA  7D4C2 [Standard]
"West Sand Hall Left": [                                               # Pop  MA  7D461 [Standard]
  RoomSpriteInfo(1707858, 1104445, numbOfEnemies=[6, 99, 99, 99]),        # Pop  MA  7D69A [Standard]
  RoomSpriteInfo(1707756, 1103854, numbOfEnemies=[1, 99, 99, 99]),        # Pop  MA  7D646 [Standard]
],                                                                                  
"Crab Hole Bottom Left": [                                                          
  RoomSpriteInfo(1708058, 1105431, numbOfEnemies=[4, 99, 99, 99]),        # Pop  MA  7D461 [Standard]
],                                                                     # Pop  MA  7D252 [Standard]
"East Tunnel Top Right": [                                                          
  RoomSpriteInfo(1707670, 1103167, numbOfEnemies=[7, 3, 99, 99]),                     
],                                                                     # Pop  NO  7A7B3 [Standard]
"Post Botwoon": [                                                      # Pop  NO  7A788 [Standard]
  RoomSpriteInfo(1707449, 1102098, numbOfEnemies=[5, 5, 99, 99]),                     
  RoomSpriteInfo(1707347, 1101613, numbOfEnemies=[3, 3, 99, 99]),                     
  RoomSpriteInfo(1708172, 1105948, numbOfEnemies=[6, 99, 99, 99]),        # Pop  MA  7D30B [Standard]
  RoomSpriteInfo(1708154, 1105881, numbOfEnemies=[4, 99, 99, 99]),        # Pop  MA  7D2D9 [Standard]
  RoomSpriteInfo(1707505, 1102318, numbOfEnemies=[9, 99, 99, 99]),        # Pop  MA  7D433 [Standard]
],                                                                     # Pop  MA  7D340 [Standard]
"Colosseum Top Right": [                                               # Pop  MA  7D387 [Standard]
  RoomSpriteInfo(1707415, 1101961, numbOfEnemies=[8, 99, 99, 99]),        # Pop  MA  7D2AA [Standard]
],                                                                     # Pop  MA  7D27E [Standard]
"Kronic Boost Room Bottom Left": [                                     # Pop  MA  7D5EC [Standard]
  RoomSpriteInfo(1706217, 1093288, numbOfEnemies=[0, 99, 99, 99]),        # Pop  MA  7D86E [Standard]
  RoomSpriteInfo(1705671, 1090271, numbOfEnemies=[5, 99, 99, 99]),                     
  RoomSpriteInfo(1706119, 1092691, numbOfEnemies=[9, 2, 99, 99]),                     
  RoomSpriteInfo(1706719, 1096085, numbOfEnemies=[4, 99, 99, 99]),        # Pop  MA  7D7E4 [Standard]
  RoomSpriteInfo(1706619, 1095475, numbOfEnemies=[2, 99, 99, 99]),        # Pop  MA  7D913 [Standard]
  RoomSpriteInfo(1706793, 1096500, numbOfEnemies=[6, 4, 99, 99]),        # Pop  MA  7DA2B [Standard]
],                                                                     # Pop  MA  7D9FE [Standard]
"Right Sandpit": [                                                     # Pop  MA  7D898 [Standard]
  RoomSpriteInfo(1708126, 1105763, numbOfEnemies=[3, 99, 99, 99]),                     
],                                                                                  
"Oasis Bottom": [                                                      # Pop  MA  7D1DD [Standard]
  RoomSpriteInfo(1707882, 1104595, numbOfEnemies=[6, 99, 99, 99]),        # Pop  MA  7D16D [Standard]
  RoomSpriteInfo(1707858, 1104445, numbOfEnemies=[6, 99, 99, 99]),                     
  RoomSpriteInfo(1707960, 1105122, numbOfEnemies=[5, 99, 99, 99]),                     
  RoomSpriteInfo(1707614, 1102931, numbOfEnemies=[6, 7, 99, 99]),        # Pop  MA  7D13B [Standard]
],                                                                                  
"Golden Four": [                                                                    
  RoomSpriteInfo(1708208, 1106178, numbOfEnemies=[6, 7, 99, 99]),        # Pop  MA  7D0B9 [Standard]
  RoomSpriteInfo(1708236, 1106392, numbOfEnemies=[4, 4, 99, 99]),        # Pop  MA  7D017 [Standard]
  RoomSpriteInfo(1708396, 1107222, numbOfEnemies=[4, 99, 99, 99]),        # Pop  MA  7CFC9 [Standard]
  RoomSpriteInfo(1708254, 1106523, numbOfEnemies=[1, 99, 99, 99]),                     
  RoomSpriteInfo(1708322, 1106823, numbOfEnemies=[2, 99, 99, 99]),                     
  RoomSpriteInfo(1708360, 1107008, numbOfEnemies=[2, 4, 99, 99]),        # Pop  MA  7D72A [Standard]
  RoomSpriteInfo(1708410, 1107289, numbOfEnemies=[4, 99, 99, 99]),                     
  RoomSpriteInfo(1708378, 1107107, numbOfEnemies=[3, 4, 99, 99]),                     
  RoomSpriteInfo(1708452, 1107538, numbOfEnemies=[4, 99, 99, 99]),        # Pop  NO  7AEDF [Standard]
  RoomSpriteInfo(1708424, 1107356, numbOfEnemies=[2, 99, 99, 99]),        # Pop  NO  7B051 [Standard]
  RoomSpriteInfo(1708438, 1107391, numbOfEnemies=[9, 99, 99, 99]),        # Pop  NO  7AEB4 [Standard]
  RoomSpriteInfo(1708536, 1107860, numbOfEnemies=[3, 9, 99, 99]),        # Pop  NO  7AE74 [Standard]
  RoomSpriteInfo(1708466, 1107605, numbOfEnemies=[7, 99, 99, 99]),        # Pop  NO  7AE07 [Standard]
  RoomSpriteInfo(1708554, 1108055, numbOfEnemies=[3, 99, 99, 99]),        # Pop  NO  7AE32 [Standard]
],                                                                                  
"Cathedral": [                                                                      
  RoomSpriteInfo(1706283, 1093511, numbOfEnemies=[4, 2, 99, 99]),        # Pop  MA  7D4EF [Standard]
  RoomSpriteInfo(1706533, 1094980, numbOfEnemies=[6, 4, 99, 99]),                     
],                                                                                  
"Beach": [                                                             # Pop  MA  7D21C [Standard]
  RoomSpriteInfo(1707734, 1103707, numbOfEnemies=[1, 6, 2, 99]),                     
  RoomSpriteInfo(1707716, 1103512, numbOfEnemies=[7, 5, 99, 99]),                     
],                                                                     # Pop  TO  7DEDE [Standard]
"Watering Hole": [                                                     # Pop  TO  7DAE1 [Standard]
  RoomSpriteInfo(1707365, 1101712, numbOfEnemies=[1, 2, 99, 99]),      # Pop  TO  7DAE1 [Events 1]
],                                                                     # Pop  TO  7DC65 [Standard/Events 1]
"Toilet Top": [                                                        # Pop  TO  7DC19 [Standard/Events 1]
  RoomSpriteInfo(1707397, 1101830, numbOfEnemies=[6, 1, 99, 99]),      # Pop  TO  7DB31 [Standard]
  RoomSpriteInfo(1707788, 1103972, numbOfEnemies=[7, 8, 99, 99]),      # Pop  TO  7DB31 [Events 1]
  RoomSpriteInfo(1708108, 1105712, numbOfEnemies=[2, 1, 99, 99]),      # Pop  TO  7DBCD [Standard]
  RoomSpriteInfo(1707810, 1104215, numbOfEnemies=[4, 5, 2, 99]),       # Pop  TO  7DBCD [Events 1]
  RoomSpriteInfo(1708006, 1105307, numbOfEnemies=[3, 4, 99, 99]),      # Pop  TO  7DE7A [Standard]
  RoomSpriteInfo(1707586, 1102829, numbOfEnemies=[4, 2, 99, 99]),      # Pop  TO  7DB7D [Events 1]
  RoomSpriteInfo(1707770, 1103873, numbOfEnemies=[6, 99, 99, 99]),     # Pop  TO  7DB7D [Standard]
  RoomSpriteInfo(1707924, 1104956, numbOfEnemies=[3, 99, 99, 99]),     # Pop  TO  7DEA7 [Standard]
  RoomSpriteInfo(1707491, 1102267, numbOfEnemies=[3, 99, 99, 99]),     # Pop  TO  7DDF3 [Standard]
],
}
