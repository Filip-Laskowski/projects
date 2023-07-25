import React, { useState, useEffect } from 'react';
import SearchBar from './components/SearchBar/SearchBar';
import ImageDisplay from './components/ImageDisplay/ImageDisplay';
import './App.css';
import { searchImages } from './api/flickr';
import ImagesLoaded from 'react-images-loaded';

function App() {
  const [searchTerm, setSearchTerm] = useState("");
  const [images, setImages] = useState([]);
  const [displayedImages, setDisplayedImages] = useState(new Set()); 
  const IMAGE_WIDTH = 300;
  const IMAGE_HEIGHT = 200;
  const GRID_GAP = 4;

  const handleSearch = async (term, totalImages) => {
    setSearchTerm(term);
    if (term) {
      try {
        const images = await searchImages(term, totalImages);
        setImages(images);
        setDisplayedImages(new Set(images.map(image => image.url)));
      } catch (error) {
        console.error('Error in image fetching:', error);
      }
    }
  }

  useEffect(() => {
    function handleResize() {
      let imagesPerRow = Math.floor((window.innerWidth - GRID_GAP) / (IMAGE_WIDTH + GRID_GAP));
      let numRows = Math.floor((window.innerHeight - GRID_GAP) / (IMAGE_HEIGHT + GRID_GAP));
      let totalImages = imagesPerRow * numRows;
      handleSearch(searchTerm, totalImages);
    }

    window.addEventListener('resize', handleResize)
    
    handleResize(); // Initial load

    return () => {
      window.removeEventListener('resize', handleResize)
    }
  }, [searchTerm]);

  // This function will replace the current image with a new unique one
  const replaceImage = async (index, displayedImagesSet, imagesArray) => {
    let newImage;
    
    // Fetch a new image until it's not in displayedImages
    do {
      try {
        [newImage] = await searchImages(searchTerm, 1);
      } catch (error) {
        console.error('Error in image fetching:', error);
        return;
      }
    } while (displayedImagesSet.has(newImage.url))
    
    // Add the new image's URL to the displayed images set
    displayedImagesSet.add(newImage.url);
    
    // Insert the new image at the same index
    imagesArray.splice(index, 0, newImage);
    
    // Update the states
    setDisplayedImages(displayedImagesSet);
    setImages(imagesArray);
  };

  const handleDownload = async (index) => {
    let newImages = [...images];
    
    // Remove the selected image from the displayed images set
    let newDisplayedImages = new Set(displayedImages);
    newDisplayedImages.delete(images[index].url);
    
    // Remove the selected image
    newImages.splice(index, 1);

    // Call replaceImage to handle fetching new images and updating state
    replaceImage(index, newDisplayedImages, newImages);
  };

  const handleReject = async (index) => {
    let newImages = [...images];

    // Remove the selected image from the displayed images set
    let newDisplayedImages = new Set(displayedImages);
    newDisplayedImages.delete(images[index].url);

    // Remove the selected image
    newImages.splice(index, 1);

    // Call replaceImage to handle fetching new images and updating state
    replaceImage(index, newDisplayedImages, newImages);
  };

  return (
    <div className="App">
      <SearchBar onSearch={(term) => handleSearch(term, images.length)}/>
      <div className="worklist">
        {images.map((image, index) => 
          <ImageDisplay 
            key={index} 
            image={image} 
            searchTerm={searchTerm}
            onDownload={() => handleDownload(index)}
            onReject={() => handleReject(index)}
          />
        )}
      </div>
    </div>
  );
}

export default App;
