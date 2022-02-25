
class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    order_type = None
    tax = None
    

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        
    
    def get_total(self):
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price   
        
        return total
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
    

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08
    def __init__(self, species, qty):

        super().__init__(species,qty)

    def get_total(self):
        if self.species == "Christmas":
            base_price = 1.5*5
        else:
            base_price = 5

        total = (1 + self.tax) * self.qty * base_price   
        return total


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):

        super().__init__(species, qty)
        self.country_code = country_code
        
        


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
    

    def get_total(self):
            
        if self.species == "Christmas":
            base_price = 1.5*5
        else:
            base_price = 5

        total = (1 + self.tax) * self.qty * base_price

        if self.qty < 10:
            return total + 3   
        return total


