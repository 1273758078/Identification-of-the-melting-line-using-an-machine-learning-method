from astropy.modeling import models, fitting
import numpy as np
import matplotlib.pyplot as plt

# Set font for displaying Chinese characters and handle minus signs in plots
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Input data for x (cut positions) and y (accuracy)
x = np.array([210, 220, 230, 240, 250, 260, 270, 280, 290])
y = np.array([
    0.952394009,
    0.951573193,
    0.955129981,
    0.961422682,
    0.96497947,
    0.976744175,
    0.986867309,
    0.984404922,
    0.970451415
])

# Initialize the Gaussian model with an amplitude of 1, mean of 250, and standard deviation of 10000
g_init = models.Gaussian1D(amplitude=1., mean=250, stddev=10000.)

# Fit the Gaussian model to the data using Levenberg-Marquardt least squares fitting
fit_g = fitting.LevMarLSQFitter()
g = fit_g(g_init, x, y)

# Output the fitted mean and standard deviation values
print(g.mean.value, g.stddev.value)

# Generate new x-values for plotting the fitted curve
a = np.array([210, 220, 230, 240, 250, 260, 270, 280, 290])
b = g(a)  # Calculate the fitted y-values based on the model

# Plot settings
plt.title('Gaussian Fitting', fontsize=20)  # Set plot title
plt.xlabel('Cut Position', fontsize=20)  # X-axis label
plt.ylabel('Accuracy', fontsize=20)  # Y-axis label

# Plot the fitted curve and the original data
plt.plot(a, b, '-', label='Fitted Curve')
plt.plot(x, y, '.', label='Original Data')

# Display the legend
plt.legend(fontsize=20)

# Show the plot
plt.show()
