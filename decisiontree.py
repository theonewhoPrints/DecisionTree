"""
This will be the decision tree we are making

"""
import math

import pandas as pd
from pandas.core.arrays.categorical import contains


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
    store_remainder = []
    length, width = dataframe.shape


    for i in range(width - 1):

        j = 0
        i = 0
        attribute = str(i)
        true_rows = dataframe[dataframe[attribute] == True].index.tolist()


# A VALUES OF TRUE
#     true_col_true_A_values = dataframe.loc[
#     (dataframe.index.isin(true_rows)) & (dataframe['label'] == "A"), 'label'].tolist()
#     print(len(true_col_true_A_values))

    # Filter to get only rows with True values in the attribute column and label equal to "A"
    true_rows_with_A = dataframe.loc[(dataframe.index.isin(true_rows)) & (dataframe['label'] == "A")]

    # Create a dictionary with row indices as keys and 'A' as the value
    true_col_true_A_dict = {index: 'A' for index in true_rows_with_A.index}

    # only by col & row







# B VALUES OF TRUE
    true_rows_with_B = dataframe.loc[(dataframe.index.isin(true_rows)) & (dataframe['label'] == "B")]
    true_col_true_B_dict = {index: 'B' for index in true_rows_with_B.index}



    # should be 88
##################################################################

# ################## FALSE LISTS ################################################

    false_rows = dataframe[dataframe[attribute] == False].index.tolist()

# A VALUES OF FALSE
#     false_col_true_A_values = dataframe.loc[
#     (dataframe.index.isin(false_rows)) & (dataframe['label'] == "A"), 'label'].tolist()

    false_rows_with_A = dataframe.loc[(dataframe.index.isin(false_rows)) & (dataframe['label'] == "A")]
    false_col_true_A_dict = {index: 'A' for index in false_rows_with_A.index}

# B VALUES OF FALSE
#     false_col_true_B_values = dataframe.loc[
#     (dataframe.index.isin(false_rows)) & (dataframe['label'] == "B"), 'label'].tolist()

    false_rows_with_B = dataframe.loc[(dataframe.index.isin(false_rows)) & (dataframe['label'] == "B")]
    false_col_true_B_dict = {index: 'B' for index in false_rows_with_B.index}


    ##################################################################

    #lue_rows = dataframe[dataframe['label'] == "A"].index.tolist().  -- the og ones
    #blue_rows = dataframe[dataframe['label'] == "B"].index.tolist()
    #print(lue_rows)


    P = (len(true_rows)/length) * ( (len(true_col_true_A_dict) * math.log2(1/len(true_col_true_A_dict)))
    + (len(true_col_true_B_dict) * math.log2(1/len(true_col_true_B_dict)))  )

    H = (len(false_rows) / length) * ((len(false_col_true_A_dict) * math.log2(1 / len(false_col_true_A_dict)))
                                 + (len(false_col_true_B_dict) * math.log2(1 / len(false_col_true_B_dict))))


    r = P + H
    store_remainder.append(r)
    ls = store_remainder.index(r)


    # store dataframes and cal it the same as the other one,
    # if not in explored and attributes less than etc

    true_rows_data = dataframe.loc[true_rows]
    false_rows_data = dataframe.loc[false_rows]

    if  len(store_remainder) >= 2 and store_remainder[ls] <= store_remainder[ls - 1]:
        #new_data_left = tru
        depth = attribute
        store_remainder.clear()
    #store  dataframes
    # do left and then right printing afterwards
    # else:
    #
    #     continue


    #outside of for range, call print function
    # recursive call on both left and right side



    # remainder.clear
    # with new remainder and it's new true and false rows, rec call on each true and fall

    #too_string()

    #from here we can make a dict, for the too string method(to hashmap)

    # attribute,
    # if it's in explored


    # if not new_data_left:



    """
     " the depth is : [
     
     
     values at depth:    
        A;                    ]
    
        B; 
    
    """







    # then if lower store those rows in that level(do the math rn)

    # MATH
    # math.log2()







def too_string():

    pass




def main():

    dataframe = read_input()
    Decision_tree(dataframe)

    # x = [1,3,2,4,5]
    # for i in range(len(x)):
    #     print(x[i])




main()



