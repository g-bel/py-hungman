import random

words = ["ABLE","ABOUT","ACCOUNT","ACID","ACROSS","ACT","ADDITION","ADJUSTMENT","ADVERTISEMENT","AFTER","AGAIN","AGAINST","AGREEMENT","AIR","ALL","ALMOST","AMONG","AMOUNT","AMUSEMENT","AND","ANDROID","ANGLE","ANGRY","ANIMAL","ANSWER","ANT","ANY","APPARATUS","APPLE","APPROVAL","ARCH","ARGUMENT","ARM","ARMY","ART","AS","AT","ATTACK","ATTEMPT","ATTENTION","ATTRACTION","AUTHORITY","AUTOMATIC","AWAKE","BABY","BACK","BAD","BAG","BALANCE","BALL","BAND","BASE","BASIN","BASKET","BATH","BE","BEAUTIFUL","BECAUSE","BED","BEE","BEFORE","BEHAVIOUR","BELIEF","BELL","BENT","BEER","BERRY","BETWEEN","BICYCLE","BIRD","BIRTH","BIT","BITE","BITTER","BLACK","BLADE","BLOOD","BLOW","BLUE","BOARD","BOAT","BODY","BOILING","BONE","BOOK","BOOT","BOTTLE","BOX","BOY","BRAIN","BRAKE","BRANCH","BRASS","BREAD","BREATH","BRICK","BRIDGE","BRIGHT","BROKEN","BROTHER","BROWN","BRUSH","BUCKET","BUILDING","BULB","BURN","BURST","BUSINESS","BUT","BUTTER","BUTTON","BY","CAKE","CAMERA","CANVAS","CARD","CARE","CARRIAGE","CART","CAT","CAUSE","CERTAIN","CHAIN","CHALK","CHANCE","CHANGE","CHEAP","CHEESE","CHEMICAL","CHEST","CHIEF","CHIN","CHURCH","CIRCLE","CLEAN","CLEAR","CLOCK","CLOTH","CLOUD","COAL","COAT","COLD","COLLAR","COLOUR","COMB","COME","COMFORT","COMMITTEE","COMMON","COMPANY","COMPARISON","COMPETITION","COMPLETE","COMPLEX","CONDITION","CONNECTION","CONSCIOUS","CONTROL","COOK","COPPER","COPY","CORD","CORK","COTTON","COUGH","COUNTRY","COVER","COW","CRACK","CREDIT","CRIME","CRUEL","CRUSH","CRY","CUP","CUP","CURRENT","CURTAIN","CURVE","CUSHION","DAMAGE","DANGER","DARK","DAUGHTER","DAY","DEAD","DEAR","DEATH","DEBT","DECISION","DEEP","DEGREE","DELICATE","DEPENDENT","DESIGN","DESIRE","DESTRUCTION","DETAIL","DEVELOPMENT","DIFFERENT","DIGESTION","DIRECTION","DIRTY","DISCOVERY","DISCUSSION","DISEASE","DISGUST","DISTANCE","DISTRIBUTION","DIVISION","DO","DOG","DOOR","DOUBT","DOWN","DRAIN","DRAWER","DRESS","DRINK","DRIVING","DROP","DRY","DUST","EAR","EARLY","EARTH","EAST","EDGE","EDUCATION","EFFECT","EGG","ELASTIC","ELECTRIC","END","ENGINE","ENOUGH","EQUAL","ERROR","EVEN","EVENT","EVER","EVERY","EXAMPLE","EXCHANGE","EXISTENCE","EXPANSION","EXPERIENCE","EXPERT","EYE","FACE","FACT","FALL","FALSE","FAMILY","FAR","FARM","FAT","FATHER","FEAR","FEATHER","FEEBLE","FEELING","FEMALE","FERTILE","FICTION","FIELD","FIGHT","FINGER","FIRE","FIRST","FISH","FIXED","FLAG","FLAME","FLAT","FLIGHT","FLOOR","FLOWER","FLY","FOLD","FOOD","FOOLISH","FOOT","FOR","FORCE","FORK","FORM","FORWARD","FOWL","FRAME","FREE","FREQUENT","FRIEND","FROM","FRONT","FRUIT","FULL","FUTURE","GARDEN","GENERAL","GET","GIRL","GIVE","GLASS","GLOVE","GO","GOAT","GOLD","GOOD","GOVERNMENT","GRAIN","GRASS","GREAT","GREEN","GREY","GRIP","GROUP","GROWTH","GUIDE","GUN","HAIR","HAMMER","HAND","HANGING","HAPPY","HARBOUR","HARD","HARMONY","HAT","HATE","HAVE","HE","HEAD","HEALTHY","HEAR","HEARING","HEART","HEAT","HELP","HIGH","HISTORY","HOLE","HOLLOW","HOOK","HOPE","HORN","HORSE","HOSPITAL","HOUR","HOUSE","HOW","HUMOUR","HUMAN","ICE","IDEA","IF","ILL","IMPORTANT","IMPULSE","IN","INCREASE","INDUSTRY","INK","INSECT","INSTRUMENT","INSURANCE","INTEREST","INVENTION","IRON","ISLAND","JELLY","JEWEL","JOIN","JOURNEY","JUDGE","JUMP","KEEP","KETTLE","KEY","KICK","KIND","KISS","KNEE","KNIFE","KNOT","KNOWLEDGE","LAND","LANGUAGE","LAST","LATE","LAUGH","LAW","LEAD","LEAF","LEARNING","LEATHER","LEFT","LEG","LET","LETTER","LEVEL","LIBRARY","LIFT","LIGHT","LIKE","LIMIT","LINE","LINEN","LIP","LIQUID","LIST","LITTLE","LIVING","LOCK","LONG","LOOK","LOOSE","LOSS","LOUD","LOVE","LOW","MACHINE","MAKE","MALE","MAN","MANAGER","MAP","MARK","MARKET","MARRIED","MASS","MATCH","MATERIAL","MAY","MEAL","MEASURE","MEAT","MEDICAL","MEETING","MEMORY","METAL","MIDDLE","MILITARY","MILK","MIND","MINE","MINUTE","MIST","MIXED","MONEY","MONKEY","MONTH","MOON","MORNING","MOTHER","MOTION","MOUNTAIN","MOUTH","MOVE","MUCH","MUSCLE","MUSIC","NAIL","NAME","NARROW","NATION","NATURAL","NEAR","NECESSARY","NECK","NEED","NEEDLE","NERVE","NET","NEW","NEWS","NIGHT","NO","NOISE","NORMAL","NORTH","NOSE","NOT","NOTE","NOW","NUMBER","NUT","OBSERVATION","OF","OFF","OFFER","OFFICE","OIL","OLD","ON","ONLY","OPEN","OPERATION","OPINION","OPPOSITE","OR","ORANGE","ORDER","ORGANIZATION","ORNAMENT","OTHER","OUT","OVEN","OVER","OWNER","PAGE","PAIN","PAINT","PAPER","PARALLEL","PARCEL","PART","PAST","PASTE","PAYMENT","PEACE","PEN","PENCIL","PERSON","PHYSICAL","PICTURE","PIG","PIN","PIPE","PLACE","PLANE","PLANT","PLATE","PLAY","PLEASE","PLEASURE","PLOUGH","POCKET","POINT","POISON","POLISH","POLITICAL","POOR","PORTER","POSITION","POSSIBLE","POT","POTATO","POWDER","POWER","PRESENT","PRICE","PRINT","PRISON","PRIVATE","PROBABLE","PROCESS","PRODUCE","PROFIT","PROPERTY","PROSE","PROTEST","PUBLIC","PULL","PUMP","PUNISHMENT","PURPOSE","PUSH","PUT","QUALITY","QUESTION","QUICK","QUIET","QUITE","RAIL","RAIN","RANGE","RAT","RATE","RAY","REACTION","READING","READY","REASON","RECEIPT","RECORD","RED","REGRET","REGULAR","RELATION","RELIGION","REPRESENTATIVE","REQUEST","RESPECT","RESPONSIBLE","REST","REWARD","RHYTHM","RICE","RIGHT","RING","RIVER","ROAD","ROD","ROLL","ROOF","ROOM","ROOT","ROUGH","ROUND","RUB","RULE","RUN","SAD","SAFE","SAIL","SALT","SAME","SAND","SAY","SCALE","SCHOOL","SCIENCE","SCISSORS","SCREW","SEA","SEAT","SECOND","SECRET","SECRETARY","SEE","SEED","SEEM","SELECTION","SELF","SEND","SENSE","SEPARATE","SERIOUS","SERVANT","SEX","SHADE","SHAKE","SHAME","SHARP","SHEEP","SHELF","SHIP","SHIRT","SHOCK","SHOE","SHORT","SHUT","SIDE","SIGN","SILK","SILVER","SIMPLE","SISTER","SIZE","SKIN","","SKIRT","SKY","SLEEP","SLIP","SLOPE","SLOW","SMALL","SMASH","SMELL","SMILE","SMOKE","SMOOTH","SNAKE","SNEEZE","SNOW","SO","SOAP","SOCIETY","SOCK","SOFT","SOLID","SOME","","SON","SONG","SORT","SOUND","SOUP","SOUTH","SPACE","SPADE","SPECIAL","SPONGE","SPOON","SPRING","SQUARE","STAGE","STAMP","STAR","START","STATEMENT","STATION","STEAM","STEEL","STEM","STEP","STICK","STICKY","STIFF","STILL","STITCH","STOCKING","STOMACH","STONE","STOP","STORE","STORY","STRAIGHT","STRANGE","STREET","STRETCH","STRONG","STRUCTURE","SUBSTANCE","SUCH","SUDDEN","SUGAR","SUGGESTION","SUMMER","SUN","SUPPORT","SURPRISE","SWEET","SWIM","SYSTEM","TABLE","TAIL","TAKE","TALK","TALL","TASTE","TAX","TEACHING","TENDENCY","TEST","THAN","THAT","THE","THEN","THEORY","THERE","THICK","THIN","THING","THIS","THOUGHT","THREAD","THROAT","THROUGH","THROUGH","THUMB","THUNDER","TICKET","TIGHT","TILL","TIME","TIN","TIRED","TO","TOE","TOGETHER","TOMORROW","TONGUE","TOOTH","TOP","TOUCH","TOWN","TRADE","TRAIN","TRANSPORT","TRAY","TREE","TRICK","TROUBLE","TROUSERS","TRUE","TURN","TWIST","UMBRELLA","UNDER","UNIT","UP","USE","VALUE","VERSE","VERY","VESSEL","VIEW","VIOLENT","VOICE","WAITING","WALK","WALL","WAR","WARM","WASH","WASTE","WATCH","WATER","WAVE","WAX","WAY","WEATHER","WEEK","WEIGHT","WELL","WEST","WET","WHEEL","WHEN","WHERE","WHILE","WHIP","WHISTLE","WHITE","WHO","WHY","WIDE","WILL","WIND","WINDOW","WINE","WING","WINTER","WIRE","WISE","WITH","WOMAN","WOOD","WOOL","WORD","WORK","WORM","WOUND","WRITING","WRONG","YEAR","YELLOW","YES","YESTERDAY","YOU","YOUNG"]
player_name = input("Please provide your name: ")

game = {
    "word": "",
    "wrong_letters": [],
    "discovered": [],
    "max_attempts": 5
}

def print_discovered():
    print(" ".join(game["discovered"]))
    print("")
    print("Failed Attempts: {}/{} | Wrong letters: {}".format(len(game["wrong_letters"]), game["max_attempts"], " ".join(game["wrong_letters"])))
    print("")

def validate_input(text):
    if(len(text) == 1 and ord(text) >= 65 and ord(text)<= 90):
        return True
    print("Letter provided is not valid. I expected 1 character between 'A' and 'Z'")
    return False

def check_char(letter):
    if(letter in game["discovered"] or letter in game["wrong_letters"]):
        print("Letter already provided")
    else:
        if(letter in game["word"]):
            for i in range(len(game["word"])):
                if(game["word"][i] == letter):
                    game["discovered"][i] = letter
        else:
            game["wrong_letters"].append(letter)

def lose_game():
    if(len(game["wrong_letters"]) == game["max_attempts"]):
        print("OOPS!! You've reached the maximum attempts possible.\nYou've LOST!\nThe word was: {}".format(game["word"]))
        return True
    return False

def win_game():
    if("_" not in game["discovered"]):
        print("YEEEY!!! That was the missing letter!!\nCongratulations, you've WON!!")
        return True
    return False


def play_game():
    print("hello " + player_name)
    print("")
    game["word"] = random.choice(words)
    game["discovered"] = ["_" for c in range(len(game["word"]))]
    game["wrong_letters"] = []
    print_discovered()
    exit = False
    while not exit:
        theChar = str(input(">> Please provide a letter: ")).upper()
        if(validate_input(theChar)):
            check_char(theChar)
            print_discovered()
            if(win_game() or lose_game()):
                exit = True
    replay = str(input("\n>> Want to play again?\nType Y or YES and press Enter (anything else will finish): ")).upper()
    if(replay == "Y" or replay == "YES"):
        play_game()

play_game()
