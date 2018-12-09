Django Game Store Project Plan
-----------------------

### 1. Team

* 543693 Kenneth Forsman
* k84823 Olli Mustakallio
* 369181 Otso Teperi


### 2. Goal

The topic for the course project for CS-C3170 2018-2019 is an online game store for JavaScript games. The service has two types of users: players and developers. Developers can add their games to the service and set a price for it. Players can buy games on the platform and then play purchased games online.


### 3. Plans

We will use agile working method, kanban board (trello).
Meetings on demand, other communication is handled by slack.
We will use git repository and heroku.

For the frontend we plan to use Django framework , HTML5 and SCSS.
For the middleware we have planned to use Express framework with NodeJS to create a restful API.
Database will be Postgre SQL.

#### 3.1. Features to implement

1. Authentication
	* Authentication will be done with Django Authentication.
	* Validation will use emails, using the Django email validation.
	* For extra points we will try and create a Django Rest API using Django Rest Framework and JWT for added security.

2. Basic player functionalities
	* Players are able to purchase games, play games and play games.
	* Players can browse games via the search games page and see which games are discounted.
	* Players can see their purchase history and high score for each game.
	* Players can only play games they have purchased or if games are marked as free.
	
3. Basic developer functionalities
	* Developers can submit games to the site using a form to register their game.
	* Developers can edit , delete the game they have added to the site.
	* Developers cannot register the same game twice.
	* Developers can monitor the sales of games have have listed.
	
4. Game/service interaction
	* Games are played via iframes that communicate with the service via postMessages.
	
5. Quality of Work
	* We will try to follow Django best practices to create a good site.
	
6. Non-functional requirements
	* When plans have changed we will update the Kanban board with new tasksa nd update the project plan.
	
7. Save/load and resolution feature (extra)
	* TBD
8. 3rd party login (OpenID, Google) (extra)
	* We plan to add the OpenID service to Django Auth or add it to Django Rest Framework
9. RESTful API  (extra)
	* A restful API using nodeJS or Django Rest Framework will be added to the site to tasks of communicating with the game services and browsing games.
10. Own game  (extra)
	* We will create a simple javascript game for the site to test it.
11. Mobile Friendly (extra)
	* We will be using bootstrap for the UI
12. Social media sharing (extra)
	* TBD if we will add social sharing.

#### 3.2. Responsibilities & Tasks

* Olli Mustakallio - Project manager  Full stack
* Kenneth Forsman - Backend
* Otso Teperi - Frontend

Each member of the team will contribute to the project equally on all parts, however they have been assigned specialties that they will mostly focus on.

#### 3.3. Priorities

We will prioritize mandatory components first. After all mandatory components are created we will start creating additional features to the web application.
Functionality , User experience , User interface

Our project has to look good , feel good and work good.

#### 3.4. Security

We have planned to use OpenID as the authentication service, we will be using JWT for user sessions.
A new key is generated per login and destroyed on logout. Each HTTP request will be validated.

For the web frontend we will follow django security tips.
https://docs.djangoproject.com/en/2.1/topics/security/

HTTPS and SSL will not be included in this project, even tho we could use lets encrypt (but it is not mandatory part of this course).

#### 3.5 Django Model

| Users        		| Games         			| Score  		| Purchases			 |
| ------------------|:-----------------------:	| -------------:|-------------------:|
| Id (int32)      	| id (int32)	 			| id(Users:id)	| id (Games:id)		 |
| fname (string)    | title (string)      		| score(int32)  | purchasedate (date)|
| lname (string) 	| imageURL (string) 		| title(Game:title) | price (Games:price)|
| password (string) | price (int32)    			| date(date)	| user (Users:id)	 |
| class (int32) 	| developer (User:id)   	|    	 		| title:(Games:title)|
|  					| url (string)     			|    	 		| |
|				 	| genre (string)  			|    	 		| |



### 4. Process and Time Schedule

We communicate using smoke signals at 1 p.m. The finished
modules are taken to north pole using goverment post services.

* Week 49: Create project plan.
* Week 49: Setup git repository , Heroku , PostgreSQL , Restful API
* Week 50: Split work into small pieces, start working on them as a team or individually. Grab tickets from the trello board.
* Week 51: Prepare for Christmas and New year, hopefully a small prototype is ready at this phase.	Registration , Login , Developer basic functionality working
* Week 52: Money and Power
* Week 53: Is there a week 53?

#### 4.1 Project Milestones
During the first phase, the mandatory specifications are completed. This phase ends with a test Heroku deployment. During the second phase, the extra functionality is added as per our agile planning. After each additional functionality 'sprint', a Heroku deployment should be made to assure a working project is available for review. This is repeated until the time is out.

### 5. Testing & Working in GIT

Master branch is only for release build, it will only contain functioning code.
Each project member will fork the master branch into their own branch, and work in that branch until the code is working. Once the code is working it will be merged into the master branch.
Once enough working components are created, master branch will be deployed to Heroku.

Before merging components into master branch, components are tested and approved.



### 6. Risk Analysis

-Sickness
-Work & Other commitments
-Lazyness
-Lack of experience
-Fail to test properly

