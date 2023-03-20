import random


class Enemy:
    __slots__ = ('Name', 'Code', 'Speed', 'Speed2', 'SpecialGFX',
                 'Special', 'Orientation', 'Difficulty')

    def __init__(self, Name, Code, Speed=0, Speed2=0, SpecialGFX=0, Special=0x2000, Orientation=0, Difficulty=0):
        self.Name = Name
        self.Code = Code
        self.Speed = Speed
        self.Speed2 = Speed2
        self.SpecialGFX = SpecialGFX
        self.Special = Special
        self.Orientation = Orientation
        self.Difficulty = Difficulty


class EnemyManager:
    Enemies = {
        'BOYON': Enemy(
            Name='Boyon',
            Code=0xCEBF,
            Speed=0x0003,
            Speed2=0x0020,
        ),
        'STOKE': Enemy(
            Name='Mini-Crocomire',
            Code=0xCEFF,
        ),
        'KAME': Enemy(
            Name='Tatori',
            Code=0xCF3F,
        ),
        'YTatori': Enemy(
            Name='Young Tatori',
            Code=0xCF7F,
            Speed=0x0001,
            Speed2=0x0000,
        ),
        'PUYO': Enemy(
            Name='Puyo',
            Code=0xCFBF,
            Speed=0x0002,
            Speed2=0x0001,
        ),
        'SABOTEN': Enemy(
            Name='Cacatac',
            Code=0xCFFF,
            Speed=0x0000,
            Speed2=0x0301,
        ),
        'TOGE': Enemy(
            Name='Owtch',
            Code=0xD03F,
            Speed=0x0100,
            Speed2=0x0108,
        ),
        'MERO': Enemy(
            Name='Mellow',
            Code=0xD0FF,
        ),
        'MELLA': Enemy(
            Name='Mella',
            Code=0xD13F,
        ),
        'MEMU': Enemy(
            Name='Memu',
            Code=0xD17F,
        ),
        'MULTI': Enemy(
            Name='Multiviola',
            Code=0xD1BF,
            Speed=0x00F0,
            Speed2=0x0003,
        ),
        'POLYP': Enemy(
            Name='Polyp',
            Code=0xD1FF,
        ),
        'RINKA': Enemy(
            Name='Rinka',
            Code=0xD23F,
        ),
        'RIO': Enemy(
            Name='Rio',
            Code=0xD27F,
        ),
        'SQUEEWPT': Enemy(
            Name='Squeept',
            Code=0xD2BF,
        ),
        'GERUDA': Enemy(
            Name='Geruta',
            Code=0xD2FF,
        ),
        'HOLTZ': Enemy(
            Name='Holtz',
            Code=0xD33F,
        ),
        'OUM': Enemy(
            Name='Oum',
            Code=0xD37F,
            Speed=0x0000,
            Speed2=0x0000,
            SpecialGFX=0x0004,
            Special=0xA800,
        ),
        'HIRU': Enemy(
            Name='Chute',
            Code=0xD3BF,
            Speed=0x0204,
            Speed2=0x0000,
        ),
        'GRIPPER': Enemy(
            Name='Gripper',
            Code=0xD3FF,
            Speed=0x0560,
            Speed2=0x05C0,
        ),
        'RIPPER2': Enemy(
            Name='Ripper II',
            Code=0xD43F,
            Speed=0x0040,
            Speed2=0x0000,
        ),
        'RIPPER': Enemy(
            Name='Ripper',
            Code=0xD47F,
            Speed=0x0010,
            Speed2=0x0001,
        ),
        'DRAGON': Enemy(
            Name='Dragon',
            Code=0xD4BF,
        ),
        'SHUTTER2': Enemy(
            Name='Kamer',
            Code=0xD5FF,
        ),
        'WAVER': Enemy(
            Name='Waver',
            Code=0xD63F,
        ),
        'METALEE': Enemy(
            Name='Metaree',
            Code=0xD67F,
        ),
        'HOTARY': Enemy(
            Name='Fireflea',
            Code=0xD6BF,
            Speed=0x0003,
            Speed2=0x0210,
        ),
        'FISH': Enemy(
            Name='Skultera',
            Code=0xD6FF,
            Speed=0x0110,
            Speed2=0x0210,
        ),
        'KANI': Enemy(
            Name='Sciser',
            Code=0xD77F,
        ),
        'OUMU': Enemy(
            Name='Zero',
            Code=0xD7BF,
        ),
        'KAMER': Enemy(
            Name='Tripper',
            Code=0xD7FF,
            Speed=0x0000,
            Speed2=0x1010,
        ),
        'KAMER': Enemy(
            Name='Kamer',
            Code=0xD83F,
            Speed=0x0000,
            Speed2=0x2800,
        ),
        'SBUG': Enemy(
            Name='Bug',
            Code=0xD87F,
        ),
        'METMOD': Enemy(
            Name='Mochtroid',
            Code=0xD8FF,
        ),
        'SSIDE': Enemy(
            Name='Sidehopper',
            Code=0xD93F,
        ),
        'SDEATH': Enemy(
            Name='Desgeega',
            Code=0xD97F,
        ),
        'BSIDE1': Enemy(
            Name='Big Sidehopper',
            Code=0xD9BF,
        ),
        'BSIDE2': Enemy(
            Name='Big Sidehopper',
            Code=0xD9FF,
        ),
        'DESSGEEGA': Enemy(
            Name='Big Desgeega',
            Code=0xDA3F,
        ),
        'ZOA': Enemy(
            Name='Zoa',
            Code=0xDA7F,
        ),
        'VIOLA': Enemy(
            Name='Viola',
            Code=0xDABF,
            Speed=0x0002,
            Speed2=0x0006,
        ),
        'BANG': Enemy(
            Name='Bang',
            Code=0xDB3F,
            Speed=0xBB4A,
            Speed2=0x0010,
            SpecialGFX=0x0000,
            Special=0x2000,
            Orientation=0x0001,
        ),
        'SKREE': Enemy(
            Name='Skree',
            Code=0xDB7F,
        ),
        'YARD': Enemy(
            Name='Yard',
            Code=0xDBBF,
            Speed=0x0007,
            Speed2=0x0000,
        ),
        'REFLEC': Enemy(
            Name='Reflec',
            Code=0xDBFF,
        ),
        'HZOOMER': Enemy(
            Name='Geemer',
            Code=0xDC3F,
        ),
        'ZEELA': Enemy(
            Name='Zeela',
            Code=0xDC7F,
        ),
        'NOVA': Enemy(
            Name='Norfair Geemer',
            Code=0xDCBF,
            Speed2=0x0000,
            SpecialGFX=0x0004,
        ),
        'ZOOMER': Enemy(
            Name='Geemer',
            Code=0xDCFF,
        ),
        'MZOOMER': Enemy(
            Name='Grey Geemer',
            Code=0xDD3F,
        ),
        'METROID': Enemy(
            Name='Metroid',
            Code=0xDD7F,
        ),
        'RSTONE': Enemy(
            Name='Boulder',
            Code=0xDFBF,
            Speed=0x0200,
            Speed2=0xA050,
        ),
        'KZAN': Enemy(
            Name='Kzan',
            Code=0xDFFF,
            Speed=0x0040,
            Speed2=0x8070,
            SpecialGFX=0x0000,
            Special=0xA000,
        ),
        'HIBASHI': Enemy(
            Name='Hibashi',
            Code=0xE07F,
        ),
        'PUROMI': Enemy(
            Name='Puromi',
            Code=0xE0BF,
            Speed=0x4010,
            Speed2=0x2001,
        ),
        'SCLAYD': Enemy(
            Name='Mini-Kraid',
            Code=0xE0FF,
        ),
        'EBI': Enemy(
            Name='Evir',
            Code=0xE63F,
            Speed=0x0000,
            Speed2=0xF808,
        ),
        'EYE': Enemy(
            Name='Eye',
            Code=0xE6BF,
        ),
        'FUNE': Enemy(
            Name='Fune',
            Code=0xE6FF,
            Speed=0x0000,
            Speed2=0x5007,
            SpecialGFX=0x0000,
            Special=0xA000,
        ),
        'NAMI': Enemy(
            Name='Namihe',
            Code=0xE73F,
            Speed=0x1001,
            Speed2=0x5005,
            SpecialGFX=0x0000,
            Special=0xA000,
        ),
        'GAI': Enemy(
            Name='Coven',
            Code=0xE77F,
        ),
        'HAND': Enemy(
            Name='Yapping Maw',
            Code=0xE7BF,
            Speed=0x0070,
            Speed2=0x0001,
        ),
        'KAGO': Enemy(
            Name='Kago',
            Code=0xE7FF,
            Speed=0x000A,
            Speed2=0x0000,
            SpecialGFX=0x0000,
            Special=0xA000,
        ),
        'LAVAMAN': Enemy(
            Name='Magdollite',
            Code=0xE83F,
            Speed=0x0000,
            Speed2=0x3A60,
        ),
        'NOMI': Enemy(
            Name='Beetom',
            Code=0xE87F,
        ),
        # 'PUU': Enemy(
        # Name = 'Powamp',
        # Code = 0xE8BF,
        # Speed = 0x0001,
        # 0x0070,
        # ),
        'ROBO': Enemy(
            Name='Work Robot',
            Code=0xE8FF,
        ),
        # 'ROBO2	Work': Enemy(
        # Name = 'Robot',
        # Code = 0xE93F,
        # ),
        'PIPE': Enemy(
            Name='Bull',
            Code=0xE97F,
            Speed=0x000A,
            Speed2=0x0000,
        ),
        'NDRA': Enemy(
            Name='Alcoon',
            Code=0xE9BF,
        ),
        'ATOMIC': Enemy(
            Name='Atomic',
            Code=0xE9FF,
            Speed=0x0000,
            Speed2=0x0008,
        ),
        'SPA': Enemy(
            Name='Sparks',
            Code=0xEA3F,
        ),
        'KOMA': Enemy(
            Name='Koma',
            Code=0xEA7F,
        ),
        'HACHI1': Enemy(
            Name='Green Kihunter',
            Code=0xEABF,
        ),
        'HACHI2': Enemy(
            Name='Greenish Kihunter',
            Code=0xEB3F,
        ),
        'HACHI3': Enemy(
            Name='Red Kihunter',
            Code=0xEBBF,
        ),
        # 'DORI': Enemy(
        # Name='Shaktool',
        # Code=0xF07F,
        # ),
        'ZEB': Enemy(
            Name='Zeb',
            Code=0xF193,
        ),
        'ZEBBO': Enemy(
            Name='Zebbo',
            Code=0xF1D3,
            Speed=0x0002,
            Speed2=0x0000,
        ),
        # 'GAMET': Enemy(
        # Name='Gamet',
        # Code=0xF213,
        # ),
        'GEEGA': Enemy(
            Name='Geega',
            Code=0xF253,
        ),
        'BATTA1': Enemy(
            Name='Grey Zebesian',
            Code=0xF353,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA1Br': Enemy(
            Name='Green Zebesian',
            Code=0xF393,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA1No': Enemy(
            Name='Red Zebesian',
            Code=0xF3D3,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA1Na': Enemy(
            Name='Gold Zebesian',
            Code=0xF413,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA1Ma': Enemy(
            Name='Pink Zebesian',
            Code=0xF453,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA1Tu': Enemy(
            Name='Black Zebesian',
            Code=0xF493,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA2': Enemy(
            Name='Grey Zebesian',
            Code=0xF4D3,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA2Br': Enemy(
            Name='Green Zebesian',
            Code=0xF513,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA2No': Enemy(
            Name='Red Zebesian',
            Code=0xF553,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA2Na': Enemy(
            Name='Gold Zebesian',
            Code=0xF593,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA2Ma': Enemy(
            Name='Pink Zebesian',
            Code=0xF5D3,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA2Tu': Enemy(
            Name='Black Zebesian',
            Code=0xF613,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA3': Enemy(
            Name='Grey Zebesian',
            Code=0xF653,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA3Br': Enemy(
            Name='Green Zebesian',
            Code=0xF693,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA3No': Enemy(
            Name='Red Zebesian',
            Code=0xF6D3,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA3Na': Enemy(
            Name='Gold Zebesian',
            Code=0xF713,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA3Ma': Enemy(
            Name='Pink Zebesian',
            Code=0xF753,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        ),
        'BATTA3Tu': Enemy(
            Name='Black Zebesian',
            Code=0xF793,
            Speed=0x8000,
            Speed2=0x0018,
            SpecialGFX=0x0004,
        )
    }
    EnemyLvl = 0

    @staticmethod
    def setEnemyLvl() -> None:
        EnemyManager.EnemyLvl += 5 # TODO: Add more logic here

    @staticmethod
    def getEnemyLvl() -> int:
        return EnemyManager.EnemyLvl

    @staticmethod
    def getRandomSprite() -> Enemy:
        filteredByDifficulty = {
            _k: enmy for _k, enmy in EnemyManager.Enemies.items() 
            if EnemyManager.enemyFilter(enmy)
        }
        return random.choice(list(filteredByDifficulty.items()))[1]
    
    @staticmethod
    def enemyFilter(enmy) -> bool:
        # TODO
        return (EnemyManager.EnemyLvl >= enmy.Difficulty)
