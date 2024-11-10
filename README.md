# Junction2024-Hackaconda

# Setup
The Survall application consists of three components, the client which which the users interact, the authetication server which sets up secure sessions, and the backend server which serves questions to the clients which they can answer.

The chapters below detail the setup process, split between the frontend client and the backend servers.

## Frontend setup
The frontend is using Vue and Vite give the user their UI.
All of the files for the frontend are in the `survall_frontend` directory.

### Frontend preparations
Install the dependencies for the frontend using `npm`.
```sh
#in the ./servall_frontend directory
npm install
```

Furthermore, you need to set up your `.env` file.
The `.env.example` has the same layout as a typical .env file.
The `VITE_AUTH_DOMAIN` should be the address to access the authorization service.
The `VITE_API_DOMAIN` should ebt the address to access the voting service.

If these are set you should be prepared to run the front end.

### Compile and Hot-Reload for Development
The hot-reload mode allows you to access the frontend with hot reload.
Any change you make to the application will be directly updated in your browser.
To run the frontend in development mode, run the following command.

```sh
#in the ./servall_frontend directory
npm run dev
```

The output will then show on which port the frontend is running.
Access the address in your browser and the frontend will be displayed.

### Compile and Minify for Production

```sh
#in the ./servall_frontend directory
npm run build
```
The files will then be placed inside the `./servall_frontend/dist` directory. 
The files in the directory can then be served by a HTTP engine (such as NGINX or Apache)

## Backend Setup
The backend is using Flask and the OpenAI API with python. The files for the authentication server can be found in `survall_auth` and the file for the question server can be found in `survall_backend`.

### Backend preparations
Optionally for both the authentication and question server a conda environment can be created. This is not nessesary for the functionality of the application.

```sh
#in the ./ root directory
conda create --name survall_backend python=3.10.0

conda activate survall_backend
```

Non-optionally install the dependencies for the backend using `pip`.

```sh
#in the ./ root directory
pip install -r requirements.txt
```

Furthermore, you need to set up your .env files. The .env.example has the same layout as a typical .env file. In the `./survall_auth` directory, the SURVALL_SECRET_KEY should be the a random string used as a private key to encrypt the login sessions. Additionally, in the `./survall_backend` directory, the OPENAI_API_KEY should be set to allow the application generate new questions dynamically.

### Running the backend
To run both backend servers, navigate to their respective sub-directories in seperate CLIs and run the following commands:

```sh
#in the ./survall_auth directory
python main.py
```

```sh
#in the ./survall_backend directory
python main.py
```
After starting both servers, no additional actions are required and the application is ready to be interacted with via the frontend client.

### Database
As an additional note, the current demo is setup to create a mock-database and inject it with mock-data in `./survall_backed/survall.db`. After initializaiton this database persists any voting responses and newly generated questions, which will be loaded when restarting the backend. The backend is setup such that the database layer can easily be swapped with a techstack fitting the requirements of the host.





