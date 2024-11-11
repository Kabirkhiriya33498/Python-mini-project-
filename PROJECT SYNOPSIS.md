#Project Title: Basic Online Auction Site

Objective:
The goal of this project is to create a simple online auction site where users can view auction listings, place bids, and track the highest bid for each product. The site will allow basic functionality like creating an auction listing and bidding, with minimal complexity.

#Technologies Used:

Backend: Python (Flask or Django)

Frontend: HTML, CSS (basic styling), and JavaScript for interactivity (optional)

Database: SQLite (for simplicity)

Version Control: Git (for project management)

#Project Description:
This basic online auction site will have the following features:

1. User Registration & Login:
Users will be able to sign up with a username and password, log in, and manage their sessions.
Basic authentication (no need for complex email verification or password reset features).

2. Auction Listings:
Users can create auction listings with simple details: product name, description, and starting bid.
A list of all active auctions will be displayed on the homepage, where users can see the auction title and current highest bid.

3. Bidding Functionality:
Registered users can place bids on auctions. The system will track the highest bid and display it in real time (refreshing the page).
If a user places a higher bid than the current one, the auction page will show their bid as the new highest bid.

4. Auction Timer (Optional):
Each auction will have a countdown timer indicating how long the auction will run. After the timer expires, the auction will end, and the highest bidder wins.

5. Admin View (Optional):
A simple admin page where the admin can view all auctions and end any active auction manually if needed.

#Development Phases:

Phase 1 – Setup and Basic Web Framework:
Set up a Python environment and install Flask (or Django if you prefer).
Create a basic project structure with folders for templates (HTML files) and static files (CSS, JavaScript).

Phase 2 – User Authentication:
Implement basic user registration and login forms. You can use Flask’s built-in tools like Flask-Login or Django’s authentication system for managing user sessions.
Users should be able to sign up with a username and password and log in to place bids.

Phase 3 – Auction Creation & Display:
Create a form for users to create new auction listings, where they can provide:
Auction Title
Description
Starting Bid Amount
Store auction data in a simple SQLite database.
Display all active auctions on the homepage, showing the product name and the current highest bid.

Phase 4 – Bidding System:
Implement a system where users can place bids on any auction listed on the homepage.
Each auction should have a "Bid Now" button, and users will only be able to bid if they place a higher amount than the current highest bid.
Once a bid is placed, update the auction listing with the new highest bid.

Phase 5 – Simple Styling & Interaction:
Use basic CSS to style the auction listings and forms.
Optionally, use JavaScript to handle dynamic elements like refreshing the auction page without reloading (e.g., using setInterval to periodically refresh the page to show the updated bids).

Phase 6 – Final Testing and Deployment:
Test all functionalities (user registration, bidding, displaying auctions) to ensure they work as expected.
Optionally deploy the project on a platform like Heroku or PythonAnywhere.

#Features Breakdown:

1. User Authentication:
Basic forms for signing up and logging in.
Session management for logged-in users.

2. Auction Listings:
Simple auction creation form (product name, description, starting bid).
Display auctions with title, description, and current highest bid on the homepage.

3. Bidding:
Users can place a bid if it’s higher than the current bid.
The system updates the highest bid in the auction.

4. Timer (Optional):
A simple timer that counts down from a set amount of time for each auction.
The auction ends once the timer reaches zero, and no further bids can be placed.

5. Basic UI Design:
Minimal styling using basic CSS to make the site clean and usable.
Simple forms and interactive buttons for bidding.
