#!/usr/bin/env python
# coding: utf-8

# ### Analyzing the Stroop Effect
# Perform the analysis in the space below. Remember to follow [the instructions](https://docs.google.com/document/d/1-OkpZLjG_kX9J6LIQ5IltsqMzVWjh36QpnP2RYpVdPU/pub?embedded=True) and review the [project rubric](https://review.udacity.com/#!/rubrics/71/view) before submitting. Once you've completed the analysis and write-up, download this file as a PDF or HTML file, upload that PDF/HTML into the workspace here (click on the orange Jupyter icon in the upper left then Upload), then use the Submit Project button at the bottom of this page. This will create a zip file containing both this .ipynb doc and the PDF/HTML doc that will be submitted for your project.
# 
# 
# (1) What is the independent variable? What is the dependent variable?

# independent variable: congruent or incongruent condition.
# dependent variable: Time to complete test.

# (2) What is an appropriate set of hypotheses for this task? Specify your null and alternative hypotheses, and clearly define any notation used. Justify your choices.

# Null Hypothsis, H0 - No change in time between two reading tasks (congruent or incongruent)
# Alternate Hypothesis, H1 - incongruent task take more time than congruent.
# H0: μi ≤ μc (μi - population mean of incongruent values, μc - population mean of congruent values)
# 
# H1: μi > μc (μi - population mean of incongruent values, μc - population mean of congruent values)

# (3) Report some descriptive statistics regarding this dataset. Include at least one measure of central tendency and at least one measure of variability. The name of the data file is 'stroopdata.csv'.

# In[2]:


# Perform the analysis here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import t
import math
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


data= pd.read_csv('stroopdata.csv')
data.head()


# In[8]:


data.shape


# In[6]:


data.describe()


# Mean for congrount = 14.05 & Mean for incongrount = 22.02 .....
# Standard Deviationfor congrount = 3.56 & Standard Deviation for incongrount = 4.80

# (4) Provide one or two visualizations that show the distribution of the sample data. Write one or two sentences noting what you observe about the plot or plots.

# In[4]:


data.hist()


# It is hard to compare the two ditribution seperatly, so we can plot one graph for congrount & incongrount regarding the Time, that can help us to make comparsion.

# In[5]:


# Build the visualizations here
sns.distplot(data['Congruent'],label="Congruent")
sns.distplot(data['Incongruent'],label="Incongruent")
plt.xlabel("Time")
plt.title("Time for congrount vs. incongrount")
plt.legend();


# We notice that for Congruent Group follows a normal distribution, and Incongruent Group follows a bi-modal normal distribution, the important notice is that the Congruent group has faster response time than Incongruent group.
# 

# (5)  Now, perform the statistical test and report your results. What is your confidence level or Type I error associated with your test? What is your conclusion regarding the hypotheses you set up? Did the results match up with your expectations? **Hint:**  Think about what is being measured on each individual, and what statistic best captures how an individual reacts in each environment.

# In[6]:


# Perform the statistical test here
#t-critical value for a 95% confidence level and 23 d.f ...{degrees of freedom is 24-1 = 23}....
t.ppf(.95, 23)


# T-critical is 1.7138

# For a confidence level of 95% and 23 degrees of freedom, our t-critical value ends up being 1.7138

# Our point estimate for the difference of the means is: 22.02 - 14.05 = 7.97

# In[7]:


#Identify the t-statistic
data['Difference'] = data['Congruent'] - data['Incongruent']
print("Std of Difference = {0:.4f}".format(data['Difference'].std(axis=0)))


# In[25]:


print("T-statistic = {0:.4f}".format(7.97/(4.8648 / math.sqrt(24))))


# T-statistic of 8.0260 is greater than the critical value of 1.7138 for 95% confidience level and 23 degrees of freedom,So we can reject the null hypothesis and can confirm that the time needed to analyize a congrouent set is statistically less than the time needed to analyize an incongrouent set, Which matches up with what we expected, That it takes much less time to do the congruent task than it does to do the incongruent task.

# ## Resources:

# http://www.statstutor.ac.uk/resources/uploaded/paired-t-test.pdf

# http://www.statisticshowto.com/when-to-use-a-t-score-vs-z-score/

# https://en.wikipedia.org/wiki/Stroop_effect

# http://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/t-score-vs-z-score/

# https://github.com/dpipkin/udacity-stroop

# (6) Optional: What do you think is responsible for the effects observed? Can you think of an alternative or similar task that would result in a similar effect? Some research about the problem will be helpful for thinking about these two questions!

# --write answer here--
