from collections import defaultdict

START = 'start'
END = 'end'

def parse(file):
    p = [tuple(line.split("-")) for line in file.read().strip().splitlines()]
    graph = defaultdict(list)
    for a, b in p:
        graph[a].append(b)
        graph[b].append(a)
    return graph

def search(g, u, path, allowDouble):
    count = 0
    for v in g[u]:
        if v == END:
            count += 1
        elif v.isupper():
            count += search(g, v, path, allowDouble)
        elif v not in path:
            count += search(g, v, path | {v}, allowDouble)
        elif allowDouble and v != START:
            count += search(g, v, path, False)
    return count

def part1(graph):
    return search(graph, START, {START}, False)

def part2(graph):
    return search(graph, START, {START}, True)

def main():
    with open("../data/12.in", "r") as f:
        inp = parse(f)
        print(part1(inp))
        print(part2(inp))

if __name__ == "__main__":
    main()

