#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt # these lines of code are calling the pandas and matplot libraries and nicknaming them

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None) # these are setting display options

movieData = pd.read_csv('rotten_tomatoes_movies.csv') # in replit be sure to change it to './rotten_tomatoes_movies.csv'
favMovie = "The LEGO Movie"

print("My favorite movie is " + favMovie)



#Part 3 Investigate the data
# print(movieData.head()) # looks at the heading
# print(movieData["movie_title"]) # looks at the specific row called movie_title


#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information
favMovieBooleanList = movieData["movie_title"] == favMovie
# print(favMovieBooleanList)
favMovieData = movieData.loc[favMovieBooleanList] # locates where my fav movie is
print(favMovieData)



print("\n\n")

#Create a new variable to store a new data set with a certain genre
actionAdventureMovieBooleanList = movieData["genres"].str.contains("Action & Adventure") # makes sure the data set includes options that have Action & Adventure and other genres
actionAdventureMovieData = movieData.loc[actionAdventureMovieBooleanList]


numOfMovies = actionAdventureMovieData.shape[0] # gets the number of rows

print("We will be comparing " + favMovie +
      " to other movies under the genre Action and Adventure in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Action and Adventure.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
min = actionAdventureMovieData["audience_rating"].min() # checks within the column audience_rating and calculates the min using .min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated 87 points higher than the lowest rated movie.")
print()

#find max
max = actionAdventureMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated 11 points lower than the highest rated movie.")
print()

#find mean
mean = actionAdventureMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is higher than the mean movie rating.")

#find median
median = actionAdventureMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is higher than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(actionAdventureMovieData["audience_rating"], range=(0, 100), bins=20) # displays the histogram that displays the data of audience_rating; range is meant to show how our diagram is going from 0 to 100 bc it's a percentage; the bin is representing the spread of the histogram

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Action & Adventure Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Action & Adventure Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, the audience ratings between 60-65 are applicable to 280 Action & Adventure movies"
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = actionAdventureMovieData, x = "audience_rating", y = "critic_rating") # the reason we don't do the brackets n stuff like that is bc the plt library is pulling data directly rather than u having to call for it

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating vs. Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, there is a positive correlation between the audience rating and critic rating. One specific thing to note was the fact that we were dealing with a LARGE dataset so it made the data a lot more saturated-something to keep in mind for future investigations."
)
print()

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
