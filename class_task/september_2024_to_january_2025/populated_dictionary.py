def get_populate_dictionary(list1, list2):
    cohort_details = {}
    for key,value in zip(list1,list2):
        cohort_details[key] = value
    return cohort_details