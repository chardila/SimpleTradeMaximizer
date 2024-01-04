import networkx as nx

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

    # Process and print the trade cycles
    for cycle in cycles:
        if 'source' in cycle or 'sink' in cycle:
            continue  # Ignore cycles involving source or sink
        print("Trade Cycle:", cycle)
        for i in range(len(cycle)):
            sender = cycle[i]
            receiver = cycle[(i + 1) % len(cycle)]
            print(f"{sender} sends to {receiver}")

def main():
    item_lists = {
        'Alice': {'offered': ['item1', 'item2'], 'wanted': ['item3', 'item4']},
        'Bob': {'offered': ['item3'], 'wanted': ['item2']},
        'Charlie': {'offered': ['item2', 'item4'], 'wanted': ['item1']},
        'David': {'offered': ['item4'], 'wanted': ['item1', 'item3']}
    }

    trade_maximizer(item_lists)

if __name__ == "__main__":
    main()
