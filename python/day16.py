import collections, functools

LITERAL_CONT_WIDTH = 1
LITERAL_NUM_WIDTH = 4

VERSION_WIDTH = 3
TYPE_ID_WIDTH = 3

OPERATOR_TYPE_WIDTH = 1
OPERATOR_TYPE_FIXED = 0
OPERATOR_TYPE_VARIABLE = 1

OPERATOR_FIXED_WIDTH = 15
OPERATOR_VARIABLE_WIDTH = 11

LiteralPacket = collections.namedtuple('LiteralPacket', ['V', 'T', 'num'])
OperatorPacket = collections.namedtuple('OperatorPacket', ['V', 'T', 'contents'])

def prod(ls):
    return functools.reduce(lambda x, y: x * y, ls)

OPS_MAP = {
    0: sum, 1: prod, 2: min, 3: max,
    5: lambda iterable: next(iterable) > next(iterable),
    6: lambda iterable: next(iterable) < next(iterable),
    7: lambda iterable: next(iterable) == next(iterable),
}

def consume(n, s):
    return int(s[:n], 2), s[n:]

def raw_consume(n, s):
    return s[:n], s[n:]

def parse_literal_num(bits):
    result, shouldContinue = 0, 1
    while shouldContinue:
        shouldContinue, bits = consume(1, bits)
        num, bits = consume(4, bits)
        result = result * 16 + num
    return result, bits

def parse_operator_contents(bits):
    operator_type, bits = consume(OPERATOR_TYPE_WIDTH, bits)

    contents = []
    if operator_type == OPERATOR_TYPE_FIXED:
        content_width, bits = consume(OPERATOR_FIXED_WIDTH, bits)
        INNER, bits= raw_consume(content_width, bits)

        while INNER:
            packet, INNER = parse(INNER)
            contents.append(packet)

    elif operator_type == OPERATOR_TYPE_VARIABLE:
        content_num, bits = consume(OPERATOR_VARIABLE_WIDTH, bits)

        for _ in range(content_num):
            packet, bits = parse(bits)
            contents.append(packet)
    else:
        raise ValueError("Operator content type could not be parsed")

    return contents, bits

def parse(bits):
    version, bits = consume(VERSION_WIDTH, bits)
    type_id, bits = consume(TYPE_ID_WIDTH, bits)

    if (type_id == 4):
        num, bits = parse_literal_num(bits)
        return LiteralPacket(version, type_id, num), bits
    else:
        contents, bits = parse_operator_contents(bits)
        return OperatorPacket(version, type_id, contents), bits

def version_sum(packet):
    if isinstance(packet, LiteralPacket):
        return packet.V
    elif isinstance(packet, OperatorPacket):
        return packet.V + sum(version_sum(p) for p in packet.contents)
    else:
        raise ValueError("Hey, this is not a packet!")

def packet_eval(packet):
    if isinstance(packet, LiteralPacket):
        return packet.num
    elif isinstance(packet, OperatorPacket):
        return OPS_MAP[packet.T](map(packet_eval, packet.contents))
    else:
        raise ValueError("Hey, this is not a packet!")

def read_input(file):
    file_content = file.read().strip()
    return bin(int(file_content, 16))[2:].zfill(4 * len(file_content))

def part1(packet):
    return version_sum(packet)

def part2(packet):
    return packet_eval(packet)

with open('../data/16.in') as file:
    bits = read_input(file)

    packet, rest = parse(bits)
    if rest:
        print(f'Note: Parsing left trailing bits: {rest}')

    print(part1(packet))
    print(part2(packet))
