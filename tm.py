import networkx as nx


def read_item_lists_from_file(file_path):
    item_lists = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(' ')
                participant = parts[0][1:-1]  # Remove parentheses
                offered_item = parts[1].split(' : ')[0]
                wanted_items = line.split(" : ")[1].split()
                if participant not in item_lists:
                    item_lists[participant] = {'offered': [], 'wanted': []}
                item_lists[participant]['offered'].append(offered_item)
                item_lists[participant]['wanted'].extend(wanted_items)
    return item_lists


def trade_maximizer(item_lists):
    # Create a directed graph
    G = nx.DiGraph()

    # Add source and sink nodes
    G.add_node('source')
    G.add_node('sink')

    # Add nodes for participants and edges from source to participants
    for participant, trade_info in item_lists.items():
        G.add_node(participant)
        G.add_edge('source', participant, capacity=1)

        # Add edges representing offered items and wanted items
        for offered_item in trade_info['offered']:
            G.add_edge(participant, offered_item, capacity=1)
        for wanted_item in trade_info['wanted']:
            G.add_edge(wanted_item, participant, capacity=1)

        # Add edges from items to sink with capacity 1
        G.add_edge(participant, 'sink', capacity=1)

    # Use the cycle canceling algorithm to find maximum flow
    flow_dict = nx.max_flow_min_cost(G, 'source', 'sink')

    # Extract trade cycles from the residual graph
    cycles = nx.simple_cycles(G)

    # Track the maximum number of trades
    max_trades = 0

    # Track the cycle or cycles with the maximum number of trades
    max_trade_cycles = []

    # Process and print the trade cycles
    for cycle in cycles:
        if 'source' in cycle or 'sink' in cycle:
            continue  # Ignore cycles involving source or sink

        num_trades = len(cycle) / 2

        # Check if the current cycle has more trades than the maximum
        if num_trades > max_trades:
            max_trades = num_trades
            max_trade_cycles = [cycle]
        elif num_trades == max_trades:
            max_trade_cycles.append(cycle)

    for cycle in max_trade_cycles:

        print("Trade Cycle:", cycle)

        for i in range(len(cycle)):
            sender = cycle[i]
            receiver = cycle[(i + 1) % len(cycle)]
            print(f"{sender} sends to {receiver}")


def main():
    file_path = 'sample01.txt'  # Replace with the actual file path
    item_lists = read_item_lists_from_file(file_path)
    trade_maximizer(item_lists)


if __name__ == "__main__":
    main()
