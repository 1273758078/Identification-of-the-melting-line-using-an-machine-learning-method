# Complex Plasma Phase Identification Project

## Project Overview

This project involves the development of a machine learning-based approach to identify phase transitions in complex plasma systems, particularly focusing on identifying the melting line in two-dimensional (2D) complex plasmas. Complex plasmas, consisting of micron-sized particles suspended in weakly ionized gases, exhibit unique phase behavior under varying temperature and interaction conditions. Leveraging unsupervised machine learning, specifically convolutional neural networks (CNNs), this project identifies phase changes by analyzing particle distributions in simulated environments.

## Motivation

Understanding phase transitions in complex plasmas is fundamental to advancements in fields like plasma physics, material science, and space sciences. Traditional approaches to phase identification rely on pre-defined parameters like the hexatic order parameter; however, this project demonstrates that unsupervised learning can effectively identify these transitions without manual labeling, opening avenues for more autonomous and scalable analysis.

## Project Structure

- **Data Processing and Simulation**: The `pretreatment.py` and `pretreatment_2.py` scripts process raw particle simulation data. Simulation data is generated based on the Langevin dynamics to capture particle behaviors across various temperatures.
- **Image Generation**: The `Scatter_plot.py` script visualizes particle distributions, converting position data into image formats for input into the CNN model.
- **Model Training**: The `gamma.py` script defines the architecture and training pipeline for the CNN model. A CNN is applied to grayscale images of particle positions, classifying phases without explicit feature engineering.
- **Phase Identification**: The CNN model is trained on image sequences representing different temperatures and tested to identify the melting line with high accuracy.
- **Utilities**: Additional scripts (`create_folder.py`, `delete_pictures.py`, etc.) handle data organization and cleanup.

## Key Results

The results indicate that unsupervised CNN models can robustly identify melting transitions in 2D complex plasmas, achieving results comparable to conventional supervised methods without requiring labeled training data. This approach also validates critical temperature thresholds identified in traditional analysis, demonstrating the model’s effectiveness in real-world scenarios.

## Requirements

- Python 3.8+
- TensorFlow for CNN modeling
- matplotlib and numpy for data processing and visualization
- Additional packages: `scipy`, `os`, `shutil`

## Getting Started

1. **Data Preparation**: Run `pretreatment.py` and `pretreatment_2.py` to preprocess raw data into image sequences.
2. **Model Training**: Execute `gamma.py` to train the CNN model on the generated images.
3. **Visualization**: Use `Scatter_plot.py` to visualize particle distributions across different temperatures.
4. **Cleanup**: Optional - Use `delete_pictures.py` to manage disk space post-training by deleting intermediate images.

## Future Directions

Further work may extend to 3D complex plasma systems and incorporate additional machine learning techniques, such as self-supervised learning, to explore higher-dimensional phase behavior.

## References

- "Identification of the melting line in the two-dimensional complex plasmas using an unsupervised machine learning method," *Fundamental Plasma Physics*, 2024.

## Acknowledgments

This project is supported by the National Natural Science Foundation of China and other foundational grants.

---

For more details, please refer to the source code in this repository or the associated publication for in-depth methodology and analysis.
