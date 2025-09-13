"""Functions to manage a users shopping cart items."""
from typing import Dict, List, Any


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart.setdefault(item, 0)
        current_cart[item] += 1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    result = {}
    for note in notes:
        result.setdefault(note, 0)
        result[note] += 1

    return result


def update_recipes(ideas: dict, recipe_updates: tuple[str, dict]) -> dict:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    print(ideas)

    for name, updates in recipe_updates:
        ideas[name] = updates

    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    result = {}

    for item, quantity in sorted(cart.items(), reverse=True):
        result[item] = [quantity, aisle_mapping[item][0], aisle_mapping[item][1]]

    return result


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for item, status in fulfillment_cart.items():
        if store_inventory[item][0] - fulfillment_cart[item][0] == 0:
            store_inventory[item][0] = 'Out of Stock'
        else:
            store_inventory[item][0] = store_inventory[item][0] - fulfillment_cart[item][0]

    return store_inventory
