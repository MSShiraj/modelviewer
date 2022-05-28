# modelviewer

Steps to load and run this project on the local system and run:
1. Download the code and save it in your project directory
2. Create a virtual environment to isolate our package dependencies locally:
       'python3 -m venv env'
       source env/bin/activate  # On Windows use `env\Scripts\activate`
3. With an active virual environment, run dollowing command to install all the reqired libraries and packages needed for the project:
      pip install -r requirements.txt
      
4. Change 'DEBUG=True' in settings.py on line 27
5. Put your Postgres DB details in 'DATABASES' variable of Settings.py where you want to upload the models.
6. Now the project is ready to run. 
7. To run the project enter following command:
      python manage.py runserver

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Steps to use all the functions in the project:
1. When you run the project, you'll see the page containing list view of the 3D models in the server.
2. Click the 'Upload 3D Model' in the sidebar to upload 'GLB' files to the server.
3. After adding the files, click on '<--Back' to move to the list page.
4. Now you can see your uploaded models in the list.
5. Click on any item in the list to see that model in a 3D space

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tech Stacks Used:
1. HTML
2. CSS
3. Bootstrap
4. JavaScript
5. Postgres Database
6. Django Framework
7. Three.js
