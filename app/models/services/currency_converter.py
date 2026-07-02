class CurrencyConverter:
    def __init__(self):
        self.rate = 10  # example

    def mad_to_eur(self, amount):
        return amount / self.rate

    def eur_to_mad(self, amount):
        return amount * self.rate