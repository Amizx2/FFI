#1 Write a function called proportion_of_education which returns the proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.  This function should return a dictionary in the form of (use the correct numbers, do not round numbers): {"less than high school":0.2, "high school":0.4, "more than high school but not college":0.2, "college":0.2} def proportion_of_education(): # your code goes here # YOUR CODE HERE raise NotImplementedError()

import pandas as pd

data = {
    'education': ['high school', 'college', 'less than high school', 'college',
                  'more than high school but not college'],
}

df = pd.DataFrame(data)


def proportion_of_education():
    education_counts = df['education'].value_counts(normalize=True)

    result = {
        "less than high school": education_counts.get("less than high school", 0),
        "high school": education_counts.get("high school", 0),
        "more than high school but not college": education_counts.get("more than high school but not college", 0),
        "college": education_counts.get("college", 0),
    }

    return result


result = proportion_of_education()
print(result)

#2Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider. Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not. This function should return a tuple in the form (use the correct numbers: (2.5, 0.1)def average_influenza_doses(): # YOUR CODE HERE raise NotImplementedError() assert len(average_influenza_doses())==2, "Return two values in a tuple, the first for yes and the second for no."

import pandas as pd

data = {
    'breastfed': [1, 0, 1, 1, 0, 0, 1, 0],
    'influenza_doses': [3, 1, 2, 4, 0, 0, 2, 0]
}

df = pd.DataFrame(data)


def average_influenza_doses():
    breastfed_group = df[df['breastfed'] == 1]
    no_breastfed_group = df[df['breastfed'] == 0]

    avg_breastfed = breastfed_group['influenza_doses'].mean()
    avg_no_breastfed = no_breastfed_group['influenza_doses'].mean()

    return avg_breastfed, avg_no_breastfed


result = average_influenza_doses()
print(result)

#3 It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child. Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.xThis function should return a dictionary in the form of (use the correct numbers): {"male":0.2,"female":0.4} Note: To aid in verification, the chickenpox_by_sex()['female'] value the autograder is looking for starts with the digits 0.0077.
import pandas as pd

data = {
    'sex': ['male', 'male', 'female', 'female', 'male', 'female', 'male', 'female'],
    'had_chickenpox': [1, 0, 1, 1, 1, 0, 0, 1],
    'vaccinated': [1, 1, 1, 1, 0, 1, 1, 1]
}

df = pd.DataFrame(data)


def chickenpox_by_sex():
    # Фильтр
    vaccinated = df[(df['vaccinated'] == 1) & (df['had_chickenpox'] == 1)]
    vaccinated_no = df[(df['vaccinated'] == 1) & (df['had_chickenpox'] == 0)]

    ratio_male = vaccinated[vaccinated['sex'] == 'male'].shape[0] / \
                 vaccinated_no[vaccinated_no['sex'] == 'male'].shape[0]
    ratio_female = vaccinated[vaccinated['sex'] == 'female'].shape[0] / \
                   vaccinated_no[vaccinated_no['sex'] == 'female'].shape[0]

    return {"male": ratio_male, "female": ratio_female}


result = chickenpox_by_sex()
print(result)

#4

import scipy.stats as stats
import numpy as np
import pandas as pd


def corr_chickenpox():
    df = pd.read_csv("D:/data.csv")

    corr, pval = stats.pearsonr(df["had_chickenpox_column"], df["num_chickenpox_vaccine_column"])

    return corr

result = corr_chickenpox()
print(result)

