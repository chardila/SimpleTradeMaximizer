def trade_maximizer_with_cycle_canceling_algorthm(item_lists):
    """
    Find and print the cycle or cycles with the maximum number of trades.

    Parameters:
    - item_lists (dict): A dictionary representing the item lists for each participant.
    """
    # Create a directed graph
    import networkx as nx
    G = nx.DiGraph()

    # Add source and sink nodes
    G.add_node('source')
    G.add_node('sink')

    # Add nodes for participants and edges from source to participants
    for participant, trade_info in item_lists.items():
        G.add_node(participant)
        G.add_edge('source', participant, capacity=1)

        # Add edges representing offered items and wanted items
        G.add_edges_from([(participant, offered_item) for offered_item in trade_info['offered']])
        G.add_edges_from([(wanted_item, participant) for wanted_item in trade_info['wanted']])

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

        # Calculate the number of trades in the cycle
        num_trades = len(cycle) // 2

        # Check if the current cycle has more trades than the maximum
        if num_trades > max_trades:
            max_trades = num_trades
            max_trade_cycles = [cycle]
        elif num_trades == max_trades:
            max_trade_cycles.append(cycle)

    # Print the cycle or cycles with the maximum number of trades
    if max_trades > 0:
        print(f"Cycles with the maximum number of trades ({max_trades}):")
        for cycle in max_trade_cycles:
            print("Trade Cycle:", cycle)
            for i in range(len(cycle)):
                sender = cycle[i]
                receiver = cycle[(i + 1) % len(cycle)]
                print(f"{sender} sends to {receiver}")
    else:
        print("No cycles found.")
