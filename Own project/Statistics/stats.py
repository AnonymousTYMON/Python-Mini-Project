#Need data: range, Min, max, average, mode, median,
#Inter-quartile range, standard deviation, standard score
import statistics
class Stats():

    def __init__(self):
        """
        Constructor method.
        """
        pass

    def range(lst):
       return __class__.max(lst) - __class__.min(lst)

    def min(lst):
        return min(lst)

    def max(lst):
        return max(lst)

    def average(lst):
        return __class__.sum(lst) / __class__.length(lst) #or return sum(lst)/len(lst)

    def median(lst):
        length = __class__.length(lst)
        if length%2 == 1:
            return lst[round(length/2)]
        if length%2 == 0:
            return (lst[round((length/2))-1] + lst[round(length/2)])/2

    def mode(lst):
        return statistics.mode(lst)

    def ir(lst):
        return statistics.quantiles(lst, n=4)[2] - statistics.quantiles(lst, n=4)[0]

    def SD(lst):
        return round(statistics.variance(lst) ** 0.5)



#Other functions
    def sum(lst):
        """
        Returns summation of all values in a list.
        """
        return sum(lst)

    @staticmethod
    def length(lst):
        """
        Returns the length of list.
        """
        return len(lst)

    @staticmethod
    def sort(lst):
        """
        Sorts the list.
        """
        return sorted(lst)
