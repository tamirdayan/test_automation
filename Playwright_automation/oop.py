class MobileDevice:

    def __init__(self, model, os, version, has_flash, price):
        self.model = model
        self.os = os
        self.version = version
        self.has_flash = has_flash
        self.price = price

    def print_parameters(self):
        print("\nmodel: " + self.model)
        print("os: " + self.os)
        print("version: " + str(self.version))
        print("has_flash: " + str(self.has_flash))
        print("price: " + str(self.price))