Django Game Store Project Plan
-----------------------

### 1. Team

* 543693 Kenneth Forsman
* k84823 Olli Mustakallio
* 999997 Otso Teperi


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

** Authentication
** Basic player functionalities
** Basic developer functionalities
** Game/service interaction
** Quality of Work
** Non-functional requirements
** Save/load and resolution feature
** 3rd party login (OpenID, Google)
** RESTful API (NodeJS)
** Own game (optional)
** Mobile Friendly (optional)
** Social media sharing (optional)

#### 3.2. Responsibilities & Tasks

* Olli Mustakallio - Project manager 
* Kenneth Forsman - Secretary of defence
* Otso Teperi - Office sweetheart <3

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

