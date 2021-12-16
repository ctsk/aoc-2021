import collections, functools, itertools

LITERAL_CONT_WIDTH = 1
LITERAL_NUM_WIDTH = 4

VERSION_WIDTH = 3
TYPE_ID_WIDTH = 3

OPERATOR_TYPE_WIDTH = 1
OPERATOR_TYPE_FIXED = 0
OPERATOR_TYPE_VARIABLE = 1

OPERATOR_FIXED_WIDTH = 15
OPERATOR_VARIABLE_WIDTH = 11

LiteralPacket = collections.namedtuple('LiteralPacket', ['V', 'T', 'value'])
OperatorPacket = collections.namedtuple('OperatorPacket', ['V', 'T', 'contents'])


def prod(ls):
    return functools.reduce(lambda x, y: x * y, ls)

OPS_MAP = {
    0: sum, 1: prod, 2: min, 3: max,
    5: lambda iterable: next(iterable) > next(iterable),
    6: lambda iterable: next(iterable) < next(iterable),
    7: lambda iterable: next(iterable) == next(iterable),
}

class GenEmptyException(Exception):
    pass

def sub_gen(num_bits, bit_gen):
    sub_iter = itertools.islice(bit_gen, num_bits)
    return (item for item in sub_iter)

def consume(num_bits, bit_gen):
    numberString = ''.join(itertools.islice(bit_gen, num_bits))
    if len(numberString) < num_bits:
        raise GenEmptyException()

    return int(numberString, 2)

def parse_literal_num(bit_gen):
    result, shouldContinue = 0, 1
    while shouldContinue:
        shouldContinue = consume(LITERAL_CONT_WIDTH, bit_gen)
        number = consume(LITERAL_NUM_WIDTH, bit_gen)
        result = result * 16 + number
    return result

def parse_operator_contents(bit_gen):
    operator_type = consume(OPERATOR_TYPE_WIDTH, bit_gen)

    contents = []
    if operator_type == OPERATOR_TYPE_FIXED:
        content_width = consume(OPERATOR_FIXED_WIDTH, bit_gen)
        INNER = sub_gen(content_width, bit_gen)

        # *sigh*
        while True:
            try:
                packet = parse(INNER)
                contents.append(packet)
            except GenEmptyException:
                break

    elif operator_type == OPERATOR_TYPE_VARIABLE:
        content_num = consume(OPERATOR_VARIABLE_WIDTH, bit_gen)

        for _ in range(content_num):
            packet = parse(bit_gen)
            contents.append(packet)
    else:
        raise ValueError("Operator content type could not be parsed")

    return contents

def parse(bit_gen):
    version = consume(VERSION_WIDTH, bit_gen)
    type_id = consume(TYPE_ID_WIDTH, bit_gen)

    if (type_id == 4):
        value = parse_literal_num(bit_gen)
        return LiteralPacket(version, type_id, value)
    else:
        contents = parse_operator_contents(bit_gen)
        return OperatorPacket(version, type_id, contents)

def version_sum(packet):
    if isinstance(packet, LiteralPacket):
        return packet.V
    elif isinstance(packet, OperatorPacket):
        return packet.V + sum(version_sum(p) for p in packet.contents)
    else:
        raise ValueError("Hey, this is not a packet!")

def packet_eval(packet):
    if isinstance(packet, LiteralPacket):
        return packet.value
    elif isinstance(packet, OperatorPacket):
        return OPS_MAP[packet.T](map(packet_eval, packet.contents))
    else:
        raise ValueError("Hey, this is not a packet!")

def read_input(file):
    file_content = file.read().strip()
    return bin(int(file_content, 16))[2:].zfill(4 * len(file_content))

def get_bit_gen(hex_string):
    for ch in hex_string:
        digit = int(ch, 16)
        yield '01'[bool(digit & 8)]
        yield '01'[bool(digit & 4)]
        yield '01'[bool(digit & 2)]
        yield '01'[bool(digit & 1)]

def part1(packet):
    return version_sum(packet)

def part2(packet):
    return packet_eval(packet)

def main():
    with open('../data/16.in') as file:
        bit_gen = get_bit_gen(file.read().strip())
        packet = parse(bit_gen)
        print(part1(packet))
        print(part2(packet))

if __name__ == '__main__':
    main()
