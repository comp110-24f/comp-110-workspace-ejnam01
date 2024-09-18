"""EXERCISE 01 TEA PARTY"""

__author__: str = "730654179"


def main_planner(guests: int) -> None:
    """conventional function for main_planner by calling each function with no math"""
    """using + to add two elements together without having a space between them"""
    """utilizing two functions to compute for another function"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print("Cost:", "$" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """defining the tea bag function to see how many tea bags are needed"""
    """multiplying the number of people by two to find the count"""
    return people * 2


def treats(people: int) -> int:
    """defining treats function to see how many treats are needed"""
    """using tea_bags to find treats instead of using people"""
    """getting an int instead of a float for the return"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """defining cost function to combine both costs for both tea and treats"""
    """using arithmetic computation to find the cost with two variables"""
    return tea_count * 0.5 + treat_count * 0.75


"""allows us to RUN the code in trailhead"""
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
