# class to hanlde the shipping cost calculation
class ShippingCostCalculator:
    # base rate for different weight ranges
    Base_rate={
        [0,2]:1.5,
        [2,5]:2.5,
        [5,10]:3.5,
        [10,float('inf')]:5
    }
    # constant for extra cost calculation
    EXTRA_COST=50
    EXTRA_COST_DISTANCE_THRESHOLD=500

def __init__(self,weight,distance):
    self.weight=weight
    self.distance=distance

    def calculate_shipping_cost(self):
        # Calculate cost based on weight and distance
        for weight_range,rate in ShippingCostCalculator.Base_rate.items():
            if weight_range[0]<=self.weight<weight_range[1]:
                cost=self.distance*rate
                break
        else:
            print('Invalid weight')
            return

        if self.distance>ShippingCostCalculator.EXTRA_COST_DISTANCE_THRESHOLD:
            cost+=ShippingCostCalculator.EXTRA_COST

        print(f'The shipping cost is: {cost}')

    def get_rate_for_weight(self,weight):
        for weight_range,rate in ShippingCostCalculator.Base_rate.items():
            if weight_range[0]<=weight<weight_range[1]:
                return rate
        return None   



def calculate_shipping_cost():
    # Get input for package weight and distance
    weight=float(input('Enter the weight of the package: '))
    distance=float(input('Enter the distance to be shipped: '))
    # Calculate shipping cost
    shipping_cost_calculator=ShippingCostCalculator(weight,distance)
    cost= shipping_cost_calculator.calculate_shipping_cost()
    return cost

if __name__ == '__main__':
    calculate_shipping_cost()
