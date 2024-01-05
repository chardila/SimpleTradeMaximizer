def read_item_lists_from_file(file_path):
    """
    Read item lists from a file and return a dictionary.

    Parameters:
    - file_path (str): The path to the file.

    Returns:
    - dict: A dictionary representing the item lists for each participant.
    """
    item_lists = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                # Split the line into parts
                parts = line.split(' ')
                # Extract participant and offered item
                participant = parts[0][1:-1]  # Remove parentheses
                offered_item = parts[1].split(' : ')[0]
                # Extract wanted items
                wanted_items = parts[2:]
                # Update item_lists dictionary
                if participant not in item_lists:
                    item_lists[participant] = {'offered': [], 'wanted': []}
                item_lists[participant]['offered'].append(offered_item)
                item_lists[participant]['wanted'].extend(wanted_items)
    return item_lists
