'''
This program plots the data for visual analysis and gives the suer a way to compare the stats
'''


import matplotlib.pyplot as plt
import numpy as np

import task2_30046572 # importing task 2 file

class Visualiser(): # class definition

    def __init__(self, list_of_stats):

        self.list_of_stats = list_of_stats # initializing list of stats for each group

    def compute_averages(self):

        list_of_categories = self.list_of_stats
        average_category_list = [] # empty string

        for each in list_of_categories: # looping over list_of_caegories
            average_category_list.append(each/10)  # appending average stats into average_category_list
        return average_category_list # returning average_category_list

    def visualise_statistics(self, stat_group, title): # stat group is the group for which the statistics are visualized e.g. SLI or TD

        average_category_list = stat_group
        labels = ['Retracing [//]', 'Repeating [/]', 'Statements [.?!]', 'Grammatical Errors [* m:ed]', 'Pauses (.)', 'Unique Words'] # plot labels

        plt.bar(range(len(average_category_list)), average_category_list) # setting bar plot with average stats for each group
        plt.xticks(range(len(average_category_list)), labels) # setting labels as defined above
        plt.title(title) # setting title
        plt.show() # plotting the final graph

    def convert_to_list(self): # for converting class object to list (only for comparison)

        list_of_categories = self.list_of_stats
        list_of_category_comparison = [] # empty list

        for each in list_of_categories: # looping over list_of_categories
            list_of_category_comparison.append(each/10) # computing average

        return list_of_category_comparison

def TD_SLI_comparison(): # to display the comparison stats

    print("\nTD-SLI Difference Comparison")
    print("-- --- ---------- ----------")
    print("Retracing words '[//]' difference : " + str(int(V_TD_SLI_compare[0] * 10)))
    print("Repeating words '[/]' difference : " + str(int(V_TD_SLI_compare[1] * 10)))
    print("Difference in Total statements '[.!?]' : " + str(int(V_TD_SLI_compare[2] * 10)))
    print("Grammatical Errors '[* m:+ed]' difference : " + str(int(V_TD_SLI_compare[3] * 10)))
    print("Pauses difference : " + str(int(V_TD_SLI_compare[4] * 10)))
    print("Unique words difference : " + str(int(V_TD_SLI_compare[5] * 10)))


SLI_path = 'ENNI_Cleaned/SLI_Cleaned/SLI_Cleaned.txt' # SLI cleaned file path

TD_path = 'ENNI_Cleaned/TD_Cleaned/TD_Cleaned.txt' # TD cleaned file path


V_SLI = Visualiser(task2_30046572.Analyser().analyse_script(SLI_path)).compute_averages() # initializing class object for SLI and calling compute_average()

V_SLI_stats_viz = Visualiser(task2_30046572.Analyser().analyse_script(SLI_path)).visualise_statistics(stat_group = V_SLI, title = "SLI Group (Average)") # calling visualise_statistics() and passing SLI object and title


V_TD = Visualiser(task2_30046572.Analyser().analyse_script(TD_path)).compute_averages() # initializing class object for TD and calling compute_average()

V_TD_stats_viz = Visualiser(task2_30046572.Analyser().analyse_script(TD_path)).visualise_statistics(stat_group = V_TD, title = "TD Group (Average)") # calling visualise_statistics() and passing TD object and title



V_SLI_compare = Visualiser(task2_30046572.Analyser().analyse_script(SLI_path)).convert_to_list() # calling convert_to_list make the SLI class object as a list

V_TD_compare = Visualiser(task2_30046572.Analyser().analyse_script(TD_path)).convert_to_list() # calling convert_to_list make the TD class object as a list



V_TD_SLI_compare = [TD - SLI for (TD,SLI) in zip(V_TD_compare, V_SLI_compare)] # using zip to subtract two lists

V_TD_SLI_compare_stats = Visualiser('').visualise_statistics(stat_group = V_TD_SLI_compare, title = "TD vs SLI Comparison (Average)") # calling visualise_statistics() and passing TD_SLI_compare object and title

TD_SLI_comparison() # calling TD_SLI_comparison() to print the average stats for the difference






















