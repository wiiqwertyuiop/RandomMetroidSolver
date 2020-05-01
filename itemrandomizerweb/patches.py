patches = {
    "Removes_Gravity_Suit_heat_protection": {
        0x06e37d: [0x01],
        0x0869dd: [0x01]},
    "Mother_Brain_Cutscene_Edits": {
        0x148824: [0x01,0x00],
        0x148848: [0x01,0x00],
        0x148867: [0x01,0x00],
        0x14887f: [0x01,0x00],
        0x148bdb: [0x04,0x00],
        0x14897d: [0x10,0x00],
        0x1489af: [0x10,0x00],
        0x1489e1: [0x10,0x00],
        0x148a09: [0x10,0x00],
        0x148a31: [0x10,0x00],
        0x148a63: [0x10,0x00],
        0x148a95: [0x10,0x00],
        0x148b33: [0x10,0x00],
        0x148dc6: [0xb0],
        0x148b8d: [0x12,0x00],
        0x148d74: [0x00,0x00],
        0x148d86: [0x00,0x00],
        0x148daf: [0x00,0x01],
        0x148e51: [0x01,0x00],
        0x14b93a: [0x00,0x01],
        0x148eef: [0x0a,0x00],
        0x148f0f: [0x60,0x00],
        0x14af4e: [0x0a,0x00],
        0x14af0d: [0x0a,0x00],
        0x14b00d: [0x00,0x00],
        0x14b132: [0x40,0x00],
        0x14b16d: [0x00,0x00],
        0x14b19f: [0x20,0x00],
        0x14b1b2: [0x30,0x00],
        0x14b20c: [0x03,0x00]},
    "Suit_acquisition_animation_skip":{
        0x020717: [0xea,0xea,0xea,0xea]},
    "Fix_heat_damage_speed_echoes_bug":{
        0x08b629: [0x01]},
    "Disable_GT_Code":{
        0x15491c: [0x80]},
    "Disable_Space_Time_select_in_menu":{
        0x013175: [0x01]},
    "Fix_Morph_Ball_Hidden_Chozo_PLMs":{
        0x0268ce: [0x04],
        0x026e02: [0x04]},
    "Fix_Screw_Attack_selection_in_menu":{
        0x0134c5: [0x0c]},
    "No_Music":{
        0x278413: [0x6f]},
    "Tourian_Refill": {
        0x1922C: [0x47, 0xF6]},
    "Escape_Rando_Enable_Enemies":{
        0x10F000: [0x0, 0x0]},
    "Escape_Rando_Disable_Enemies":{
        0x10F000: [0x1]},
    "Escape_Animals_Open_Brinstar": {
        0x784BD: [0x10]
    },
    "Escape_Animals_Open_Norfair": {
        0x78B0B: [0x10]
    },
    "Escape_Animals_Open_Maridia": {
        0x7C54C: [0x10]
    },
    # vanilla data to restore setup asm for plandos
    "Escape_Animals_Disable": {
        0x79867: [0xb2, 0x91],
        0x798dc: [0xbb, 0x91]
    },
    "LN_Chozo_SpaceJump_Check_Disable": {
        0x2518f: [0xea, 0xea, 0xea, 0xea, 0xea, 0xea, 0xea, 0xea]
    },
    "LN_PB_Heat_Disable": {
        0x18878: [0x80, 0x00]
    },
    "LN_Firefleas_Remove_Fune": {
        0x10ABC2: [0xff, 0x7f, 0xff, 0x7f],
    },
    "WS_Main_Open_Grey": {
        0x10BE92: [0x0]
    },
    "WS_Save_Active": {
        0x7ceb0: [0xC9]
    },
    "WS_Etank": {
        0x7cc4d: [0x37, 0xc3]
    },
    "Phantoon_Eye_Door":{
        0x7CCAF: [0x91, 0xC2]
    },
    # has to be applied along with WS_Main_Open_Grey
    "Sponge_Bath_Blinking_Door": {
        0x7C276: [0x0C],
        0x10CE69: [0x00]
    },
    # custom load points for non standard start APs
    "Save_G4": {
        # load point entry
        0x4527: [0xED, 0xA5, 0x16, 0x92, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0xA8, 0x00, 0x60, 0x00],
        # map icon X/Y
        0x1486f: [0x78, 0x00, 0x48, 0x00]
    },
    "Save_Gauntlet": {
        # load point entry
        0x4519: [0xBD, 0x99, 0x1A, 0x8B, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x88, 0x00, 0x50, 0x00],
        # music in room state header
        0x799ce: [0x09],
        # map icon X/Y
        0x1486b: [0x58, 0x00, 0x18, 0x00]
    },
    "Save_Watering_Hole": {
        # load point entry
        0x4979: [0x3B, 0xD1, 0x98, 0xA4, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x88, 0x00, 0xD0, 0xFF],
        # music in room state header
        0x7d14c: [0x1b, 0x06],
        # map icon X/Y
        0x14a0f: [0x68, 0x00, 0x28, 0x00]
    },
    "Save_Mama": {
        # load point entry
        0x496B: [0x55, 0xD0, 0xE4, 0xA3, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x98, 0x00, 0xF0, 0xFF],
        # music in room state header
        0x7d066: [0x1b, 0x06],
        # map icon X/Y
        0x14a0b: [0x97, 0x00, 0x67, 0x00]
    },
    "Save_Aqueduct": {
        # load point entry
        0x495D: [0xA7, 0xD5, 0xC8, 0xA4, 0x00, 0x00, 0x00, 0x05, 0x00, 0x00, 0x78, 0x00, 0x20, 0x00],
        # map icon X/Y
        0x14a07: [0xc4, 0x00, 0x50, 0x00]
    },
    "Save_Etecoons": {
        # load point entry
        0x4631: [0x51, 0xA0, 0x3A, 0x8F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x98, 0x00, 0xD0, 0xFF],
        # music in room state header
        0x7a062: [0x0f, 0x05],
        # map icon X/Y
        0x148d9: [0x28, 0x00, 0x58, 0x00]
    },
    "Save_Firefleas": {
        # load point entry
        0x473b: [0x5A, 0xB5, 0x9E, 0x9A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00],
        # music in room state header
        0x7b56b: [0x18, 0x05],
        # map icon X/Y
        0x1493f: [0x38, 0x01, 0x28, 0x00]
    },
    # blinking doors for area APs
    'Blinking[Keyhunter Room Bottom]': {
        0x78228: [0x4e, 0xc8, 0x16, 0x2d, 0x0e, 0x8c],
        0x108F7B: [0x0]
    },
    'Blinking[Moat Right]': {
        0x1085E0: [0x0]
    },
    'Blinking[Morph Ball Room Left]': {
        0x78746: [0x48, 0xc8, 0x01, 0x26, 0x31, 0x8c],
        0x1093A8: [0x0]
    },
    'Blinking[Green Pirates Shaft Bottom Right]': {
        0x78470: [0x42, 0xc8, 0x0e, 0x66, 0x63, 0x8c],
        0x108572: [0x0]
    },
    'Blinking[Lower Mushrooms Left]': {
        0x108C0C: [0x0]
    },
    'Blinking[Golden Four]': {
        0x109F60: [0x0]
    },
    'Blinking[Green Brinstar Elevator]': {
        0x108585: [0x0]
    },
    'Blinking[Green Hill Zone Top Right]': {
        0x78670: [0x42, 0xc8, 0x1e, 0x06, 0x63, 0x8c],
        0x109D5B: [0x0]
    },
    'Blinking[Noob Bridge Right]': {
        0x787A6: [0x42, 0xc8, 0x5e, 0x06, 0x63, 0x8c],
        0x109325: [0x0]
    },
    'Blinking[Warehouse Zeela Room Left]': {
        0x109451: [0x0]
    },
    'Blinking[KraidRoomOut]': {
        0x10A056: [0x0]
    },
    'Blinking[Warehouse Entrance Right]': {
        0x1098F6: [0x0]
    },
    'Blinking[Warehouse Entrance Left]': {
        0x1098F6: [0x0]
    },
    'Blinking[Single Chamber Top Right]': {
        0x10B88E: [0x0]
    },
    'Blinking[Kronic Boost Room Bottom Left]': {
        0x78D4E: [0x48, 0xc8, 0x11, 0x26, 0x58, 0x8c],
        0x10B9D7: [0x0]
    },
    'Blinking[Three Muskateers Room Left]': {
        0x10BB0D: [0x0]
    },
    'Blinking[Lava Dive Right]': {
        0x10AD6B: [0x0]
    },
    'Blinking[RidleyRoomOut]': {
        0x10B81B: [0x0]
    },
    'Blinking[West Ocean Left]': {
        0x1086F6: [0x0]
    },
    'Blinking[PhantoonRoomOut]': {
        0x10C3E5: [0x0]
    },
    'Blinking[Crab Maze Left]': {
        0x108B3A: [0x0]
    },
    'Blinking[Crab Hole Bottom Left]': {
        0x10DE59: [0x0]
    },
    'Blinking[Main Street Bottom]': {
        0x10DF2F: [0x0]
    },
    'Blinking[Red Fish Room Left]': {
        0x10D3EC: [0x0]
    },
    'Blinking[Le Coude Right]': {
        0x7823E: [0x42, 0xc8, 0x0e, 0x06, 0x63, 0x8c],
        0x1085DD: [0x0]
    },
    'Blinking[DraygonRoomOut]': {
        0x10D111: [0x0]
    },
    'Blinking[East Tunnel Top Right]': {
        0x10D5E1: [0x0]
    },
    'Blinking[East Tunnel Right]': {
        0x10D5E1: [0x0]
    },
    'Blinking[Glass Tunnel Top]': {
        0x10D53B: [0x0]
    },
    'Blinking[Red Tower Top Left]': {
        0x109504: [0x0]
    },
    'Blinking[Caterpillar Room Top Right]': {
        0x10A0B9: [0x0]
    },
    'Blinking[Red Brinstar Elevator]': {
        0x78256: [0x54, 0xc8, 0x06, 0x02, 0x10, 0x8c],
        0x1089F1: [0x0]
    },
}

additional_PLMs = {
    # for escape rando seeds
    "WS_Map_Grey_Door": {
        'room': 0Xcc6f,
        'plm_bytes_list': [
            [0x48, 0xc8, 0x1, 0x6, 0x61, 0x90]
        ]
    },
    "WS_Map_Grey_Door_Openable": {
        'room': 0Xcc6f,
        'plm_bytes_list': [
            [0x48, 0xc8, 0x1, 0x6, 0x61, 0x10]
        ]
    },
    # area/boss seeds
    # has to be applied along with WS_Main_Open_Grey
    "WS_Save_Blinking_Door": {
        'room': 0xcaf6,
        'state': 0xcb08,
        'plm_bytes_list': [
            [0x42, 0xC8, 0x4E, 0x36, 0x62, 0x0C]
        ]
    },
    # non standard start AP seeds (morph item is not in vanilla PLM list w/ zebes awake)
    "Morph_Zebes_Awake": {
        'room': 0x9e9f,
        'state': 0x9ecb,
        'plm_bytes_list': [
            [0xff, 0xff, 0x45, 0x29, 0x1A, 0x00]
        ],
        'locations': [("Morphing Ball", 0)]
    },
    # custom save points for non standard start APs
    "Save_G4": {
        "room": 0xa5ed,
        'plm_bytes_list': [
            [0x6F, 0xB7, 0x3D, 0x0C, 0x07, 0x00]
        ]
    },
    "Save_Gauntlet": {
        "room": 0x99bd,
        'plm_bytes_list': [
            [0x6F, 0xB7, 0x0C, 0x0A, 0x06, 0x00]
        ]
    },
    "Save_Watering_Hole": {
        "room": 0xd13b,
        'plm_bytes_list': [
            [0x6F, 0xB7, 0x14, 0x0A, 0x07, 0x00]
        ]
    },
    "Save_Mama": {
        "room": 0xd055,
        'plm_bytes_list': [
            [0x6F, 0xB7, 0x26, 0x0B, 0x06, 0x00]
        ]
    },
    "Save_Aqueduct": {
        "room": 0xd5a7,
        'plm_bytes_list': [
            [0x6F, 0xB7, 0x59, 0x09, 0x05, 0x00]
        ]
    },
    "Save_Etecoons": {
        "room": 0xa051,
        'plm_bytes_list': [
            [0x6F, 0xB7, 0x04, 0x0B, 0x07, 0x00]
        ]
    },
    "Save_Firefleas": {
        "room": 0xb55a,
        'plm_bytes_list': [
            [0x6F, 0xB7, 0x07, 0x09, 0x07, 0x00]
        ]
    },
    # blinking doors for area APs
    'Blinking[Moat Right]': {
        'room': 0x95ff,
        'plm_bytes_list': [
            [0x42, 0xc8, 0x1e, 0x06, 0x63, 0x8c]
        ]
    },
    'Blinking[Lower Mushrooms Left]': {
        'room': 0x9969,
        'plm_bytes_list': [
            [0x48, 0xc8, 0x01, 0x06, 0x63, 0x8c]
        ]
    },
    'Blinking[Golden Four]': {
        'room': 0xa5ed,
        'plm_bytes_list': [
            [0x48, 0xc8, 0x01, 0x06, 0x63, 0x8c]
        ]
    },
    'Blinking[Green Brinstar Elevator]': {
        'room': 0x9938,
        'plm_bytes_list': [
            [0x42, 0xc8, 0x0e, 0x06, 0x63, 0x8c]
        ]
    },
    'Blinking[Warehouse Zeela Room Left]': {
        'room': 0xa471,
        'plm_bytes_list': [
            [0x48, 0xc8, 0x01, 0x06, 0x63, 0x8c]
        ]
    },
    'Blinking[KraidRoomOut]': {
        'room': 0xa56b,
        'plm_bytes_list': [
            [0x42, 0xc8, 0x1e, 0x16, 0x63, 0x8c]
        ]
    },
    'Blinking[Warehouse Entrance Right]': {
        'room': 0xa6a1,
        'plm_bytes_list': [
            [0x48, 0xc8, 0x01, 0x06, 0x63, 0x8c]
        ]
    },
    'Blinking[Warehouse Entrance Left]': {
        'room': 0xa6a1,
        'plm_bytes_list': [
            [0x42, 0xc8, 0x2e, 0x06, 0x63, 0x8c]
        ]
    },
    'Blinking[Single Chamber Top Right]': {
        'room': 0xad5e,
        'plm_bytes_list': [
            [0x42, 0xc8, 0x5e, 0x06, 0x63, 0x8c]
        ]
    },
    'Blinking[Three Muskateers Room Left]': {
        'room': 0xb656,
        'plm_bytes_list': [
            [0x48, 0xc8, 0x11, 0x06, 0x63, 0x8c]
        ]
    },
    'Blinking[Lava Dive Right]': {
        'room': 0xaf14,
        'plm_bytes_list': [
            [0x42, 0xc8, 0x3e, 0x06, 0x63, 0x8c]
        ]
    },
    'Blinking[RidleyRoomOut]': {
        'room': 0xb37a,
        'plm_bytes_list': [
            [0x48, 0xc8, 0x01, 0x06, 0x63, 0x8c]
        ]
    },
    'Blinking[West Ocean Left]': {
        'room': 0x93fe,
        'plm_bytes_list': [
            [0x48, 0xc8, 0x01, 0x46, 0x63, 0x8c]
        ]
    },
    'Blinking[PhantoonRoomOut]': {
        'room': 0xcc6f,
        'plm_bytes_list': [
            [0x42, 0xc8, 0x4e, 0x06, 0x63, 0x8c]
        ]
    },
    'Blinking[Crab Maze Left]': {
        'room': 0x957d,
        'plm_bytes_list': [
            [0x48, 0xc8, 0x01, 0x16, 0x63, 0x8c]
        ]
    },
    'Blinking[Crab Hole Bottom Left]': {
        'room': 0xd21c,
        'plm_bytes_list': [
            [0x48, 0xc8, 0x01, 0x16, 0x63, 0x8c]
        ]
    },
    'Blinking[Main Street Bottom]': {
        'room': 0xcfc9,
        'plm_bytes_list': [
            [0x4e, 0xc8, 0x16, 0x7d, 0x63, 0x8c]
        ]
    },
    'Blinking[Red Fish Room Left]': {
        'room': 0xd104,
        'plm_bytes_list': [
            [0x48, 0xc8, 0x01, 0x06, 0x63, 0x8c]
        ]
    },
    'Blinking[DraygonRoomOut]': {
        'room': 0xd78f,
        'plm_bytes_list': [
            [0x48, 0xc8, 0x01, 0x26, 0x63, 0x8c]
        ]
    },
    'Blinking[East Tunnel Top Right]': {
        'room': 0xcf80,
        'plm_bytes_list': [
            [0x42, 0xc8, 0x3e, 0x06, 0x63, 0x8c]
        ]
    },
    'Blinking[East Tunnel Right]': {
        'room': 0xcf80,
        'plm_bytes_list': [
            [0x42, 0xc8, 0x0e, 0x16, 0x63, 0x8c]
        ]
    },
    'Blinking[Glass Tunnel Top]': {
        'room': 0xcefb,
        'plm_bytes_list': [
            [0x54, 0xc8, 0x06, 0x02, 0x63, 0x8c]
        ]
    },
    'Blinking[Red Tower Top Left]': {
        'room': 0xa253,
        'plm_bytes_list': [
            [0x48, 0xc8, 0x01, 0x46, 0x63, 0x8c]
        ]
    },
    'Blinking[Caterpillar Room Top Right]': {
        'room': 0xa322,
        'plm_bytes_list': [
            [0x42, 0xc8, 0x2e, 0x36, 0x63, 0x8c]
        ]
    },
}
