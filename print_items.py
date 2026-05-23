class ListPrinter:

    def __init__(self, items):
        self.items = items

    def print_items(self):
        for item in self.items:
            print(item)


# Example usage:
my_list = ["apple", "banana", "cherry"]
printer = ListPrinter(my_list)
printer.print_items()
