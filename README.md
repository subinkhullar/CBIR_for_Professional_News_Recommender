# CBIR_for_Professional_News_Recommender
CBIR WebApp System for News Recommendation Based on Professional Profile of a user

1. The CBIR WebApp System is built using FastAPI and GoogleNews API. 

2. A user is presented with a form to receive professional profile details, such as, educational details, professional experience, and skills. The entered professional details are converted in a search query by application of TFIDF on the three types of data in the professional profile details. The GoogleNews API is called using the search query to retrieve news-based search results, which may be relevant to the professional profile details of the user. The retrieved search results along with the entered professional details are displayed in another webpage. Each search results includes a title of a related news item, a brief description of the news item, and a URL of the news item.

3. The folder structure of the CBIR system is as follows:

Root___
	|___
	|    templates___
	|		     |___
	|			    hello.html
	|			    index.html
      |
      |___ app.py (Python file)
	|
	|___ readme.txt (Readme text file) 
	|
	|___ requirements.txt (Package requirements text file) 
	|
	|___ screenshot1.jpg
	|
	|___ screenshot2.jpg
	|
	|___ screenshot3.jpg
	|
	|___ screenshot4.jpg	

4. How to deploy/run the WebApp:
	a. On opening and running the app.py Python file on any IDE or console, a Uvicorn server starts running on http://127.0.0.1:5049
	b. To run the Webapp, open http://127.0.0.1:5049 on any browser.
	c. "index.html" webpage is rendered. Here, enter the professional profile details and press submit.
	d. The WebApp navigates to "hello.html" and displays the professional profile details and the retrieved search results including news items related to the professional profile details.
	e. Press "Back" or "Home" to go back to "index.html" and update professional profile details.

  
Screenshots:
![Screenshot1](https://user-images.githubusercontent.com/89964333/201000392-7c30ab37-30ab-47ff-b477-4685d7df1cc4.jpg)
 
![Screenshot2](https://user-images.githubusercontent.com/89964333/201000442-ec76a680-6beb-42e8-913a-2ce303607324.jpg)

![Screenshot3](https://user-images.githubusercontent.com/89964333/201000468-1a3ab061-d991-4770-8695-26be0c9e92ec.jpg)

![Screenshot4](https://user-images.githubusercontent.com/89964333/201000490-67d1005a-cc21-4bcf-a0a4-80c2bca2724e.jpg)
