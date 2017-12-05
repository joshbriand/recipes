#Josh Briand's Linux Server Configuration v 1.0 12/05/2017

##Introduction

The purpose of this project was to prepare a Linux server to host my Recipe
Catalog web application from earlier this year.


##Usage

Users can go to http://34.223.226.189/ in their web browser to use the
application.
The reviewer can access the server by SSHing in to 34.223.226.189 on port 2200
using the username grader.


##Software Installed on Server

apache2, libapache2-mod-wsgi, virtualenv, git, python-pip, python-dev,
postgreSQL and build-essential were all installed onto the server.

Using pip I installed the following Python modules: sys, logging, sqlalchemy,
sqlalchemy.orm, datetime, psycopg2, sqlalchemy.ext.declarative, flask, random,
string, oauth2client.client, httplib2, simplejson, json and requests.

As of December 5 @ 3:00pm PT all packages have been updated and all security
updates have been installed.


##Configuration Changes

The following configuration changes were made to the server:
-changed the SSH port from 22 to 2200
-updated and upgraded all packages
-configured UFW to only allow incoming connections from ports 2200, 80 and 123
-created a grader user with sudo privileges


##Third Party Resources

I did a lot of reading in the Udacity Forum, Stackoverflow and Digital Ocean.  
Most of my research was done trying to figure out how to change my web app from
an SQLite database to a PostgreSQL database and on how to deploy a Flask
application on a Ubuntu server.


##Contact Info
E-mail: joshbriand@gmail.com
