import matplotlib.pyplot as plt
import numpy as np

def Hydropathy_End(AA_1,AA_2,ReferenceParameters, window_range):
    length1 = len(AA_1[1])
    length2 = len(AA_2[1])
    x_values_for_hydroplot_1 = []
    y_values_for_hydroplot_1= []
    x_values_for_hydroplot_2 =[]
    y_values_for_hydroplot_2 = []


    numarated1=enumerate(AA_1[1])
    numarated2=enumerate(AA_2[1])

    for idx, aa in numarated1:
        s = 0.0
        if idx < length1-window_range:
            x_values_for_hydroplot_1.append(idx)
            for i in AA_1[1][idx:idx+20]:
                s += ReferenceParameters[i]
            y_values_for_hydroplot_1.append(s)

        elif idx == length1-window_range:
            x_values_for_hydroplot_1.append(idx)
            for i in AA_1[1][idx:idx+20]:
                s += ReferenceParameters[i]
            y_values_for_hydroplot_1.append(s)
            break

    for idx, aa in numarated2:
        s2 = 0.0
        if idx < length2-window_range:
            x_values_for_hydroplot_2.append(idx)
            for i in AA_2[1][idx:idx+20]:
                s2 += ReferenceParameters[i]
            y_values_for_hydroplot_2.append(s2)

        elif idx == length2-window_range:
            x_values_for_hydroplot_2.append(idx)
            for i in AA_2[1][idx:idx+20]:
                s2 += ReferenceParameters[i]
            y_values_for_hydroplot_2.append(s2)
            break

    plt.figure('HydroPathyIndexPlotFig')
    ax = plt.axes()
    #plt.plot(x_values_for_hydroplot_1,y_values_for_hydroplot_1, color='yellow')
    plt.plot(x_values_for_hydroplot_2,y_values_for_hydroplot_2, color='orange')
    x_lins=np.linspace(0,len(x_values_for_hydroplot_1))
    #x_lins2=np.linspace(0,len(x_values_for_hydroplot_2))

    plt.plot(x_lins,(x_lins*0))
    #plt.plot([0,length],[1.6, 1.6], "r")

    ## AdjustHereToDetermineMonitorRange
    ax.set(xlim=(0, length1-window_range))
    ##

    plt.ylabel('Hydropathy Of AA Sequence')
    plt.xlabel('Amino Acids')
    plt.fill_between(x_values_for_hydroplot_1, y_values_for_hydroplot_1, color='yellow',alpha=0.2)
    plt.fill_between(x_values_for_hydroplot_2, y_values_for_hydroplot_2, color='orange',alpha=0.2)

    first_labels = [AA_1[0], "Reference Line ",AA_2[0]]
    plt.legend(labels=first_labels, loc="upper right")
    plt.grid()
    plt.show()