# CPTN265 Final Presentation: Ground Breaking
* [Github Repository](https://github.com/ashlyn-knox/final-project)

## Overview
This site is a space to develop integration between node and python servers. The long term goal is to be able to explore how AI and machine learning can be optimized on a python server to interact with users on a vuejs frontend framework. I want to be able to explore integrating python with javascript's asynchronous functionality and Express's scalability.

### Core Values
* Modularity
* Scalability
* Curiosity
* Flexibility

## Basic Setup
While this site could easily have been made using a templating engine like ejs or jinja, Later stages of development will benefit from VueJs' virtual dom. Likewise regarding the backend setup. This stage would easily work well by just running everything on either flask or express, However the goal at this stage was to gain early working knowledge on how to integrate these two setups so that I can focus on building them vertically.

### Frontend
* VueJs frontend framework
* bootstrap-vue

### Backend Setup
* Node Express web server
* Mongo Atlas Database
* Flask server
* Python API

## Immediate Next Steps
1. Set up the frontend hosted form to communicate with the flask server.
  - TODO: Test routing through express using async/await
  - TODO: Test routing post request directly to flask.
  - TODO: Also test python's asyncio library for asyc functions against those in express
2. Manage get requests for google searches to output onto the table
  - TODO: Like the post requests, test pros and cons of routing directly and through express
  - TODO: Also test directly from flask. -- NOTE: I forsee trouble with this approach in the long run.
3. Set up email feature to send results to user via email.
  - TODO: test formats - plain text, pdf, docx, odt, spreadsheet
  - TODO: look for security vulnerabilities (Do this regarding form in general)
4. Basic Vuejs site ready for production
  - TODO: SASS styling
  - TODO: Finish setting up components (particularly moving large form data into a separate file to make it more maintainable)
  - TODO: Improve Typography and body text content. -- Rethink target audience

## Attributions
* 
