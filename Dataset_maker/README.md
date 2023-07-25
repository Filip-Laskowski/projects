## Getting Started
Follow these instructions to run this project on your local machine for development and testing purposes.

### Prerequisites
What things you need to install:
- Git - [Download & Install Git](https://git-scm.com/downloads). MacOS and Linux machines typically have this already installed.
- Node.js - [Download & Install Node.js](https://nodejs.org/en/download/) and the npm package manager.

### Installing

**Step 1**: Clone the Repo
On the command line, in any directory you'd like to have the project, type:
```
git clone 
```

**Step 2**: Navigate to the directory
```
cd 
```

**Step 3**: Install dependencies
```
npm install
```

**Step 4**: Start the project
```
npm start
```

Now the development server has started and the project will be running at localhost:3000 (or a different port if 3000 is busy).

---
# Image Fetch and Curation Tool

## Project Description

This project aims to become a powerful tool for curating image datasets, catering particularly to the needs of AI practitioners and researchers. It is designed to fetch and organize images based on user input, presenting an intuitive way to create datasets for image processing and machine learning tasks.

By inputting a search term, the application fetches relevant images from an API and displays them in a dynamic, responsive grid layout that adapts to the size of the user's screen. Users can interact with the displayed images by choosing to download or remove them. Removed images get replaced by new ones, ensuring a continuously refreshing pool of images. 

In its final form, this application will not only allow users to gather images but will also organize these images into correctly labeled folders. This eliminates the need for users to manually sort and label images, significantly speeding up the process of preparing datasets for machine learning model training.

### Current State & Functionality

Currently, the application offers the following functionalities:

- **Search for images:** Users can input keywords to fetch related images.
- **Responsive grid layout:** The images are displayed in a grid that adapts to the user's screen size, providing a comfortable browsing experience.
- **Interactive image curation:** Users can download or remove[not yet fully functional] images. When an image is removed, it gets replaced by a new one without repetition, allowing for a dynamic and engaging user experience.

### Future Work

The project is in progress, and future developments aim to enhance its functionality and convenience:

- **Dataset Generation:** The end goal is to allow users to create an organized, labeled dataset directly from the application. Users will be able to select multiple images, which will then be downloaded into a single folder and labeled appropriately. This feature is instrumental for practitioners preparing datasets for image processing networks, making the tool a one-stop solution for dataset curation.
- **Robust Error Handling:** Improved handling for scenarios like API failures or no images returned needs to be implemented.
- **User Account Management:** Future improvements may include creating user accounts, saving preferences, and tracking history for personalized user experience.
- **Expansion to Other Resources:** The current implementation works with a specific image API. Plans include expanding it to fetch images from various sources or APIs.
- **Implementing loading new images in place of old or removed ones:** This functionality has yet to be implemented into the design, but the frontend infrastructure is already there.
This project stands at the intersection of image fetching and dataset curation, aiming to streamline and automate the often time-consuming process of gathering and organizing images for machine learning tasks. Though in a functional state, the tool will continue to evolve, incorporating features to enhance usability and efficiency.
