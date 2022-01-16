# kural_analysis_py
Basic analysis of the ancient Tamil work Thirukkural using Python.

NOTE:

AFTER YOU READ THROUGH THE INTRODUCTION USE THE JUPITER NBVIEWER LINK BELOW TO VIEW ALL PLOTLY GRAPHS USED IN THE ANALYSIS.
THIS IS BECAUSE OPENING THE .ipynb FILE FROM GITHUB DOESNT RENDER THE PLOTLY GRAPHS
http://nbviewer.jupyter.org/github/krisrs/kural_analysis_py/blob/7bb3db7f2568c63cbfba7ef272b13cdd6f5c4089/kural_analysis.ipynb

INTRODUCTION:

This analysis is on the ancient Tamil work - Thirukkural
Thirukkural, is a set of 1330 couplets written by the saint poet Valluvar - known as Thiruvalluvar, using the writing devices of the time (palm leaves and writing needle)
The work has beautiful structure and deep meaning. 
Each couplet is an aphorism, a crisp statement on many aspects of life - organized around 3 main themes with a few sections under each theme
first theme is around right conduct & principles, the second major theme is about right way of learning & earning a living (from emperors to regular householders), and
the third theme is on love - in all its dimensions, from the subtle to the lusty
There are 133 subsections - of 10 each, under the major themes and their sections. 

Credits:

1) http://www.projectmadurai.org/ for having put out a pdf in unicode friendly tamil font which I have copied into a txt file for my analysis (http://www.projectmadurai.org/pm_etexts/pdf/pm0001.pdf)
2) Plotly for all the beautiful charts and editable code snippets which I could use to render visually some of what I saw in the data

**Brief note on the analyses itself
**

Analysis imports a unicode text file containing thirukkural 

Python codes in the iPython notebook, created using Jupyter notebook has various python codes that were used to analyze and plot this data

Analysis focuses on the frequency of usage of the Tamil language characters in this work - Vowel letters (called the uyir meaning life) and consonants (called mey or the body) and uyir-mey, which is a combination of the uyir & mey are analyzed using the python codes.

Plots using the plotly library for python then give a visual representation of the distribution of these group of letters.
