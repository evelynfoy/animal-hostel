## Local Deployment

- Steps for deployment:
    - There are several ways to get this application working locally
        - Using GITPOD 
            - Add Gitpod extension to Chrome (or firefox) - chrome://extensions/     
              search for gitpod and click add
            - Go to https://github.com/evelynfoy/animal-hostel 
            - Click the green Gitpod button on the right of the screen.
            - This will create a new local workspace for you to work in.

        - Clone the repository from the https url on GitHub 
            - Go to https://github.com/evelynfoy/animal-hostel
            - Click on the Code dropdown button on the right hand side of screen
            - Click the copy button to the right of the HTTPS url to get the url to use
            - Open Git Bash on you local machine and type git clone and the url e.g.    
              git clone https://github.com/evelynfoy/animal-hostel.git
            - This will create a repository on your machine.
            - cd animal-hostel and open with your choice of editor e.g. vscode
            - To run you need to have python3 installed.    
              Run python --version in the command line to find what version you are on. 

        - Download the code as a ZIP file, unpack and open with your favorite editor e.g. vscode 

         - Type pip3 install -r requirements.txt 
         - Type python3 manage.py migrate
         - Type python3 manage.py runserver
         - This will run the application for you - click Open Browser button

## Remote Deployment
This project was deployed using [Heroku](https://dashboard.heroku.com/apps "Heroku").

- Steps for deployment:
    - Fork or clone this repository 
    - Create a new Heroku app - https://dashboard.heroku.com/apps. You will need an account for this. 
    - On the resources tab add a Heroku Postgres database
    - Copy the DATABASE_URL value located in the Settings Tab, click reveal Config Vars and copy the value.
    - Create new env.py file on top level directory
    - Paste this database url into the env.py file     
      os.environ["DATABASE_URL"] = "postgres://" + DATABASE_URL VALUE
    - On the Settings tab
        - Add in a secret key value under Config vars called SECRET_KEY   
        - Copy this value into your env.py file
          os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"
        - Add another config var called CLOUDINARY_URL and set it to your cloudinary account url.
          You will need to set up an account In [Cloudinary](https://cloudinary.com/ "Cloudinary")
          Then paste this value into you env.py file     
          os.environ["CLOUDINARY_URL"] = "cloudinary://************************"
    - Add your new site into the 'ALLOWED_HOSTS' setting in the settings.py file.
    - Then Add, Commit and Push to heroku    
      git add .    
      git commit -am "Deployment commit"    
      git push heroku main    
    - You can see the progress of the build on the activity tab
    - Click Open app to run it

## To run the application
- The application has been deployed to https://animals-hostel.herokuapp.com/.    
  It can be accessed there or through the github repository - https://github.com/evelynfoy/animal-hostel/