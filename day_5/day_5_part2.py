input_file = 'input.txt'


def get_input_data():
    with open(input_file) as file:
        input_data = file.readlines()
    return input_data


def parse_input(input_data):
    page_orders = []
    print_pages = []
    pages = True
    for line in input_data:
        line = line.strip()
        if line == "":
            pages = False
            continue
        if pages:
            l, r = line.split("|")
            page_orders.append((int(l.strip()), int(r.strip())))
        else:
            [int(x.strip()) for x in line.split(",")]
            print_pages.append([int(x.strip()) for x in line.split(",")])

    return page_orders, print_pages


class Graph:
    def __init__(self):
        self.graph = {}
        self.normalized = False

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = set()
        if neighbour not in (self.graph[node]) and neighbour:
            self.graph[node].add(neighbour)
            # self.graph[node] = sorted(self.graph[node])
    # 97 > 75 > 47 > 61 > 53 > 29 > 13

    def normalize(self):
        if self.normalized:
            return
        for key in self.graph:
            # print(key)
            for reference in [k for k, v in self.graph.items() if key in v]:
                # print(self.graph[reference], self.graph[key])
                self.graph[reference] = self.graph[reference] - self.graph[key]
        for key in self.graph:
            assert len(self.graph[key]) == 1, self.graph[key]
            self.graph[key] = list(self.graph[key])[0]
        self.normalized = True

    def node_order(self, start_point=None):
        # start = ([v for k, v in self.graph.items() if v not in ] + [None])[0]
        self.normalize()
        start = start_point or ([k for k, v in self.graph.items() if k not in self.graph.values()] + [None])[0]
        start = start or list(self.graph.keys())[0]
        nodes = [start]
        while True:
            next_node = self.graph.get(nodes[-1], None)
            if next_node is None or next_node in nodes:
                break
            nodes.append(next_node)
        return nodes


def ultimate_page_order(pages):
    overall_order = Graph()
    temp_order = sorted(pages, key=lambda x: f"{x[0]}-{x[1]}")
    for l, r in temp_order:
        overall_order.add_edge(l, r)
    return overall_order


def valid_page(page, ultimate_order):
    expected_order = ultimate_order.node_order(page[0])
    try:
        idx_order = [expected_order.index(x) for x in page]
        return idx_order == sorted(idx_order)
    except:
        return False


def fix_page(page, ultimate_order):
    expected_order = ultimate_order.node_order(page[0])
    print(expected_order)
    idx_order = [expected_order.index(x) for x in page]
    return [expected_order[i] for i in sorted(idx_order)]


def main():
    orders, pages = parse_input(get_input_data())
    ultimate_order = ultimate_page_order(orders)

    results = []
    for page in pages:
        if not valid_page(page, ultimate_order):
            if page == [27, 26, 19, 69, 94, 34, 99, 87, 25]:
                print("  ", page)
                fixed = fix_page(page, ultimate_order)
                mid = int(len(fixed) / 2)
                results.append(fixed[mid])
                print(fixed[mid], fixed)

                break

    print(f"Final Result: {sum(results)}")

defaultdict(None, {27: 6, 26: 2, 19: 4, 69: 0, 94: 1, 34: 3, 99: 8, 87: 5, 25: 7})


if __name__ == "__main__":
    main()
