def to_float(value):
    try:
        return float(value)
    except ValueError:
        return None


def calcMissing(readings):
    # [{'index': 0, 'value': 289.71}, {'index': 1, 'value': 291.71}, {'index': 2, 'value': 292.46}, 
    #  {'index': 3, 'value': None}, {'index': 4, 'value': None}, {'index': 5, 'value': 305.11}, {'index': 6, 'value': None}]
    data = [{'index': i, 'value': to_float(r.split(' ')[1])} for i, r in enumerate(readings)]
    print(data)

    for row in data:
        if row['value'] is None:
            left_not_none = next((r for r in data[:row['index']][::-1] if r['value'] is not None), None)
            right_not_none = next((r for r in data[row['index'] + 1:] if r['value'] is not None), None)
            if left_not_none is None:
                print(right_not_none['value'])
            elif right_not_none is None:
                print(left_not_none['value'])
            else:
                diff_index = right_not_none['index'] - left_not_none['index']
                diff_value = right_not_none['value'] - left_not_none['value']
                print(left_not_none['value'] + diff_value / diff_index)



if __name__ == "__main__":
    res = calcMissing(["1/30/201216:00:00 289.71", "1/31/201216:00:00 291.71", "2/1/201216:00:00 292.46", "2/2/201216:00:00 Missing_1", "2/3/201216:00:00 Missing_2", "2/6/201216:00:00 Missing_3", "2/13/201216:00:00 Missing_2"])
            
    
