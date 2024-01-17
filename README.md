
 
# HOTELS

## Goal:
The purpose of this project is to create user login and registration, to display the hotels I have saved according 
to the city searched, and to provide the opportunity to review the hotel for each hotel.

## Technologies and Programming Languages Used:
Python,django,JavaScript,bootstrap.

## Requirements:
 - Search capability by City, Dates and Guest count
 - Show a list of at least 3 hotels on home page that are AVAILABLE as of the coming WEEKEND, ordered by points
   DESCENDING in the COUNTRY of the user making the search
 - Each hotel’s (at least) rating, number of comments, name, price will be displayed
 - If not logged in, login will be visible at the header. For flagged hotes, show ‘Uye fiyati icin giris yapin’ for users
   not logged in. Users logged in will get 10% discount
 -Hotels can specify special discounts and they will be displayed in hotel card i.e %42 indirim
LOGIN PAGE:
 - Login with email/password or Google will be supported. 
 - User can register with just email, password (at least 8 characters, 1 number and 1 none alphanumeric character) and
    country, city 
 - If google authenticated or after register, user will be directed to HOME PAGE.
   o Header will have ‘Merhaba, <user name’ 
   o Hotel cards will have Member price, if defined
SEARCH RESULTS:
 Search results will be show 
 - name, price, rating and number of comments for hotels along with a picture. 
 - Comments are not needed 
 - At least 5 amenities of the hotel
 - Map of the hotel. You can use Google Maps or other APIs for this purpose. You can make up on coordinates
   
## Video:
https://github.com/gultenguzel/hotels/assets/140374859/d413143f-e893-4b49-917d-502a18e23e20


https://github.com/gultenguzel/hotels/assets/140374859/ac731107-6f98-4435-ba13-6c17832e7940





## Data Model:
![hotels diagram](https://github.com/gultenguzel/hotels/assets/140374859/e390ae63-3a21-4b8e-8283-8256d7b5c75f)

## Carry Through:
The web application called "Hotels.com" is a platform I developed mostly using Django. Users can create their
accounts by registering, then log in. They can choose where they want to go from 81 cities in Turkey, set the 
check-in and check-out dates, enter the number of rooms, and look at the hotels listed. There are only 12 hotels in 
the application I developed, so it is possible that there are no hotels available according to the selected city.
In such a case, a warning appears that there are no hotels to be shown, which I created using HTML. If the cities of
Antalya, Izmir, Muğla, Istanbul and Adana are selected, 1-3 hotels will be listed. Hotels can be examined and users who 
register on the website can benefit from a 10% discount. You can also use Google Maps. Using the API, the locations of 
selected hotels on the map can be viewed.




