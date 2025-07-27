# === here will be some non-library csv parsing modules === 

# === IMPORTS === 
from io import TextIOWrapper


def get_list(csv_file: TextIOWrapper) -> list[dict]:
    """
    returns list of dictionaries from given csv file(open('file'))
    """
    columns = []
    # try to get columns from the top of csv 
    try:
        columns = csv_file.readline().strip().split(",")
    except Exception as e:
        print(f"error getting lines error: {e}")
        return [{}]

    try:
        data = csv_file.readlines()[1:]
    except Exception as e:
        print(f"error getting lines error: {e}")
        return [{}]

    array = []

    for i in range(len(data)):
        one_row = {}
        data[i] = data[i].strip()
        for j in range(len(columns)):
            try:
                one_row[columns[j]] = data[i].split(",")[j]
            except IndexError as e:
                print(f"warning getting column id:{j} in row id: {i}")
                continue
            except Exception as e:
                print(f"unexcpected error: {e}")
        array.append(one_row)

    return array

