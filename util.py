# from matplotlib.table import table


def ascii_table():

    ascii_dict = {
        0: "NUL",
        1: "SOH",
        2: "STX",
        3: "ETX",
        4: "EOT",
        5: "ENQ",
        6: "ACK",
        7: "BEL",
        8: "BS",
        9: "TAB",
        10: "LF",
        11: "VT",
        12: "FF",
        13: "CR",
        14: "SO",
        15: "SI",
        16: "DLE",
        17: "DC1",
        18: "DC2",
        19: "DC3",
        20: "DC4",
        21: "NAK",
        22: "SYN",
        23: "ETB",
        24: "CAN",
        25: "EM",
        26: "SUB",
        27: "ESC",
        28: "FS",
        29: "GS",
        30: "RS",
        31: "US",
        32: " ",
        33: "!",
        34: '"',
        35: "#",
        36: "$",
        37: "%",
        38: "&",
        39: "'",
        40: "(",
        41: ")",
        42: "*",
        43: "+",
        44: ",",
        45: "-",
        46: ".",
        47: "/",
        48: "0",
        49: "1",
        50: "2",
        51: "3",
        52: "4",
        53: "5",
        54: "6",
        55: "7",
        56: "8",
        57: "9",
        65: "A",
        66: "B",
        67: "C",
        68: "D",
        69: "E",
        70: "F",
        71: "G",
        72: "H",
        73: "I",
        74: "J",
        75: "K",
        76: "L",
        77: "M",
        78: "N",
        79: "O",
        80: "P",
        81: "Q",
        82: "R",
        83: "S",
        84: "T",
        85: "U",
        86: "V",
        87: "W",
        88: "X",
        89: "Y",
        90: "Z",
        97: "a",
        98: "b",
        99: "c",
        100: "d",
        101: "e",
        102: "f",
        103: "g",
        104: "h",
        105: "i",
        106: "j",
        107: "k",
        108: "l",
        109: "m",
        110: "n",
        111: "o",
        112: "p",
        113: "q",
        114: "r",
        115: "s",
        116: "t",
        117: "u",
        118: "v",
        119: "w",
        120: "x",
        121: "y",
        122: "z",
        123: "{",
        124: "|",
        125: "}",
        126: "~",
        127: "DEL",
    }

    return ascii_dict


def getByChar(char):
    values = ascii_table()

    for key, value in values.items():
        if value == char:
            return key


def getByKey(key):
    values = ascii_table()
    return values[key]


def get_base64_table():

    base64_dict = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G",
        7: "H",
        8: "I",
        9: "J",
        10: "K",
        11: "L",
        12: "M",
        13: "N",
        14: "O",
        15: "P",
        16: "Q",
        17: "R",
        18: "S",
        19: "T",
        20: "U",
        21: "V",
        22: "W",
        23: "X",
        24: "Y",
        25: "Z",
        26: "a",
        27: "b",
        28: "c",
        29: "d",
        30: "e",
        31: "f",
        32: "g",
        33: "h",
        34: "i",
        35: "j",
        36: "k",
        37: "l",
        38: "m",
        39: "n",
        40: "o",
        41: "p",
        42: "q",
        43: "r",
        44: "s",
        45: "t",
        46: "u",
        47: "v",
        48: "w",
        49: "x",
        50: "y",
        51: "z",
        52: "0",
        53: "1",
        54: "2",
        55: "3",
        56: "4",
        57: "5",
        58: "6",
        59: "7",
        60: "8",
        61: "9",
        62: "+",
        63: "/",
    }

    return base64_dict


def getByChar64(char):
    values = get_base64_table()

    for key, value in values.items():
        if value == char:
            return key


def getByKey64(key):
    values = get_base64_table()
    return values[key]



def inverse_val_tab(table):
    result = []
    for i in range(1, len(table)):
        result.append(table[-i])
    result.append(table[0])
    return result


def tTos(table):
    strbase = ""
    for i in range(0, len(table)):
        strbase += str(table[i])
    return strbase


# Binaire en nombre
def binGX(data, bits=8):
    val = []

    while data > 0:
        val.append(data % 2)
        data //= 2

    val.reverse()

    # ajouter les 0 manquants
    while len(val) < bits:
        val.insert(0, 0)

    return val


# print( binGX(2))


# nombre en binaire
def nombreToGX(data, n):
    result = 0
    val = inverse_val_tab(data)
    for i in range(0, len(data)):
        result = result + (val[i] * (n**i))
    # print("Utilisation de Base"+str(n)+" en decimal de GeneratX -> " + tTos(data) + " = " + str(result))
    return result


def nombreToGXString(data, n):
    result = 0
    val = inverse_val_tab(data)
    for i in range(0, len(data)):
        result = result + (int(val[i]) * (n**i))
    # print("Utilisation de Base"+str(n)+" en decimal de GeneratX -> " + tTos(data) + " = " + str(result))
    return result



def nbtTotable(nombre):
    valString = str(nombre)
    tableResult = []
    for i in range(0, len(valString)):
        tableResult.append(int(valString[i]))
    return tableResult


# nombre en binaire
def nombreToGX1(data, n):
    val = inverse_val_tab(nbtTotable(data))
    # print(val)
    return nombreToGX(val, n)


def assembleBinary2D(table):
    # print("tableee ------"  )
    # print( table )
    stringResult = ""
    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            stringResult += str(table[i][j])
            # print(table[i][j])
    return stringResult


def get6bitAssembled(stringResult):
    tableResult = []
    tableResult6bit = []
    tableResult6bit.append(stringResult[0])
    # print("Hello  - > " +  len(stringResult))
    for i in range(1, len(stringResult)):
        if i % 6 == 0:
            # print("Hello  - > " + str(i))
            tableResult.append(tableResult6bit)
            tableResult6bit = []
            tableResult6bit.append(stringResult[i])
        else:
            tableResult6bit.append(stringResult[i])
    
    tableResult.append(tableResult6bit)
    return tableResult 


def get6bitBase64(tableValues):
    tableResult = []
    for i in range(0, len(tableValues)):
        tableResult.append(nombreToGXString(tableValues[i], 2))
    return tableResult


def convertTo64( tableValues ):
    finalStr  = ""
    for i in range(0, len(tableValues)) : 
        finalStr+=  getByKey64(tableValues[i])
    return finalStr


def encoderBase64(text):
    tableResult = []
    tableResult1 = []
    tableBinary = []
    for i in range(0, len(text)):
        val = getByChar(text[i])
        bins = binGX(val)
        tableResult1.append(val)
        tableBinary.append(bins)

    tableResult = assembleBinary2D(tableBinary)
    # print(tableResult1)
    # print(tableResult)
    tableVal  = get6bitAssembled(tableResult) 
    table6bit = get6bitBase64(tableVal) 
    table64bit = convertTo64(table6bit ) 
    
    print(text + " => base64 :| " + table64bit)
    return tableResult




def decoderBase64(text):
    tableResult = []
    
    
# encoderBase64("HelloLuckas!")
decoderBase64("SGVsbG9MdWNrYXMh") 
# nombreToGX1( 11  , 2 )
# print(getByChar('a'))
