
#### inspired by [Modern JavaScript for Django Developers](https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/)

#### deploy
```
# set up your virtualenv 
pip install -r requirements.txt
python manage.py runserver
```
#### visit
`http://127.0.0.1:8000/demo/` for django template page  
`http://127.0.0.1:8000/demo/react` for react home page  


#### custom dev
```
# install npm
cd {project_dir}
npm init -y
npm install webpack webpack-cli --save-dev
npm install --save-dev babel-loader @babel/core @babel/preset-env @babel/preset-react
npm install --save react react-dom
# config webpack.config.js(for entry and babel-loader) and package.json(for dev subcommand)
npm run dev # to update static/index-bundle.js
```