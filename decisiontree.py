"""
This will be the decision tree we are making

"""

import pandas as pd
def read_input():

    input_vectors = []
    labels = []

    with open("../dtree-data.dat", 'r') as file:
        for data in file:
            vals = data.strip().split()
            attributes = vals[:-1]
            label = vals[-1]
            r = []
            for attribute in attributes:
                if attribute == "True":
                    r.append(True)
                else:
                    r.append(False)
            input_vectors.append(r)
            labels.append(label)
    df = pd.DataFrame(input_vectors, columns=[str(i) for i in range(len(input_vectors[0]))])
    #
    df["label"] = labels
    return df


def Decision_tree(dataframe):




    length, width = dataframe.shape

    # for i in range(width - 1):
    i = 0
    attribute = str(i)

    true_false_counts = dataframe[attribute].value_counts()
    true_count = true_false_counts[True]
    false_count = true_false_counts[False]


    true_rows = dataframe[dataframe[attribute] == True].index.tolist()
    false_rows = dataframe[dataframe[attribute] == False].index.tolist()


    # right now I can use length of list, but later I can use amount only instead of making
    # 2 new lists. Length(divisor should equal amount of thos trues or those falses.

    last_col_true_values = dataframe.loc[true_rows, 'label'].tolist() #on'es with label = A or B
    #  THIS ONE FOR NEXT.



    last_col_false_values = dataframe.loc[false_rows, 'label'].tolist()



    #Print the lists to verify
    print("Last column values for rows with True values:", last_col_true_values)
    print("Last column values for rows with False values:", last_col_false_values)
    # print(true_rows_A)









def main():

    dataframe = read_input()
    Decision_tree(dataframe)

    # x = [1,3,2,4,5]
    # for i in range(len(x)):
    #     print(x[i])




main()



