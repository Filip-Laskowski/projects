import axios from 'axios';

const API_KEY = '074de3becc0a62bdd20ed197dee1fbaf';  
const API_URL = 'https://api.flickr.com/services/rest/';


const calculateImagesNeeded = () => {
  const windowWidth = window.innerWidth;
  const windowHeight = window.innerHeight;

  const imageWidth = 200; 
  const imageHeight = 200;  

  const imagesPerRow = Math.floor(windowWidth / imageWidth);
  const imagesPerColumn = Math.floor(windowHeight / imageHeight);

  return imagesPerRow * imagesPerColumn;
};

export const searchImages = async (searchTerm, imageCount) => {
    try {
        if (!searchTerm || isNaN(imageCount)) {
            throw new Error('Invalid searchTerm or imageCount');
        }

        const response = await axios.get(API_URL, {
            params: {
              method: 'flickr.photos.search',
              api_key: API_KEY,
              text: searchTerm,
              format: 'json',
              nojsoncallback: 1,
              per_page: imageCount,
              sort: 'relevance', 
              content_type: 1,
            },
          });
          

        console.log(response.data);

        if (response.data && response.data.photos && response.data.photos.photo) {
            // Parsing the URL of images
            const images = response.data.photos.photo.map((photo) => {
                return {
                    id: photo.id,
                    url: `https://farm${photo.farm}.staticflickr.com/${photo.server}/${photo.id}_${photo.secret}.jpg`,
                    title: photo.title
                };
            });

            return images;
        } else {
            throw new Error("Invalid API response");
        }
    } catch (error) {
        console.error('Error in Flickr API', error);
        throw error;
    }
};


