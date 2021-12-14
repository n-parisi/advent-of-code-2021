paths = {}
full_paths = []
with open("input.txt", "r") as f:
    for line in f:
        src, dst = line.strip().split('-')
        if src in paths:
            paths[src].append(dst)
        else:
            paths[src] = [dst]
        if dst in paths:
            paths[dst].append(src)
        else:
            paths[dst] = [src]


def visited_two_small(visited):
    for visited_node in visited:
        if (visited_node == visited_node.lower()) and (len([x for x in visited if x == visited_node]) > 1):
            return True
    return False


def visit(node, visited):
    visited.append(node)
    for dst in paths[node]:
        if dst == 'end':
            final_path = visited.copy()
            full_paths.append(final_path.append(dst))
        elif (dst == dst.upper()) or (dst not in visited) or ((not visited_two_small(visited)) and (dst != 'start')):
            visit(dst, visited.copy())


visit('start', [])
print(len(full_paths))
