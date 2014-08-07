def calculate_discount(item_cost, relative_discount, absolute_discount):
    """
    Given the cost of an item, deduct the absolute discount.
    Then, deduct the percentage discount ("relative")
    """
    final_cost = item_cost
    final_cost -= item_cost * (relative_discount / 100)
    final_cost -= absolute_discount

    if item_cost <= 0 :
        raise ValueError("Item has no original cost. Give it away.")

    if final_cost < 0:
        raise ValueError("Too big a discount! Just give it away.")

    return final_cost

def main():
    original = 100.00
    relative = 10.0
    absolute = 90.00
    final_cost = calculate_discount(original, relative, absolute)
    print "The original cost of ${:.2f} has been discounted.".format(original)
    print "{:.1f}% has been taken off the original price.".format(relative)
    print "Plus, an additional ${:.2f} discount has been made.".format(absolute)
    print "The final, discounted price is ${:.2f}.".format(final_cost)

if __name__ == "__main__":
    main()