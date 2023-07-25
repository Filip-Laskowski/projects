import React from 'react';
import plus from './plus.png';
import minus from './minus.png';
import './ImageDisplay.css';

// In ImageDisplay.js
const ImageDisplay = ({ image, searchTerm, onDownload, onReject }) => {

  const downloadImage = (imgUrl, fileName, callback) => {
      fetch(imgUrl)
      .then(response => response.blob())
      .then(blob => {
          const url = window.URL.createObjectURL(blob);
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', fileName);
          document.body.appendChild(link);
          link.click();
          link.parentNode.removeChild(link);
          callback();
      });
  }

  return (
      <div className="work">
          <img src={image.url} alt={searchTerm} className="overlay" />
          <div className="layer">
              <div className="layerHalf redLayer">
                  <img 
                      src={minus} 
                      className="sign minus" 
                      alt="Minus Sign" 
                      onClick={onReject}
                  />
              </div>
              <div className="layerHalf greenLayer">
                  <img 
                      src={plus} 
                      className="sign plus" 
                      alt="Plus Sign" 
                      onClick={() => downloadImage(image.url, `${searchTerm}.jpg`, onDownload)}
                  />
              </div>
          </div>
      </div>
  );
}


export default ImageDisplay;
