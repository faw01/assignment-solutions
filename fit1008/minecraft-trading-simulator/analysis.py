from hash_table import *

def get_combinations(table: list):
    """
    Run through all combinations in the list and generate a hash table for each combination

    Time Complexity Analysis:
        Best Case: O(n^2)
        Worst Case: O(n^2)
    """
    hash_base = []
    table_size = []
    keys_data = []
    # keys = ['india_cities.txt', 'aust_cities.txt', 'us_cities.txt']
    keys = ['India Cities', 'Australia Cities', 'US Cities']

    # Assign the hash base, table size and keys data for each combination
    for datasets in range(len(table)):
        hash_base.append(table[datasets][0])
        table_size.append(table[datasets][1])
        keys_data.append(table[datasets][2])

    # Go through all combinations of hash functions, table sizes and keys and print the statistics
    for i in hash_base:
        for j in table_size:
            hash_table = LinearProbeTableAnalysis(j)
            hash_table.set_hash_value(i)
            for l in keys_data:
                for m in l:
                    hash_table[m] = m
                print(f"Hash Base: {i}, Table Size: {j}, Dataset: {keys[keys_data.index(l)]}, Statistics: {hash_table.statistics()}")
                # print a new line when there is a new hash base
                if l == keys_data[-1]:
                    print()
    return 

if __name__ == "__main__":
    indian_cities = open("fake_data_indian_cities.txt").read().splitlines()
    aust_cities = open("fake_data_aust_cities.txt").read().splitlines()
    us_cities = open("fake_data_us_cities.txt").read().splitlines()

    indian_cities_table = [1, 20021, indian_cities]
    aust_cities_table = [9929, 402221, aust_cities]
    us_cities_table = [250726, 1000081, us_cities]

    city_table_data = [indian_cities_table, aust_cities_table, us_cities_table]

    get_combinations(city_table_data)