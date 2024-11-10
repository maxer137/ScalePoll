# Junction2024-Hackaconda

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