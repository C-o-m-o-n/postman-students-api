
## Postman Student Leader Program (LeadersHub) API

This API provides a comprehensive interface for managing events and speakers associated with the Postman Student Leader program. It allows authorized users to create, retrieve, update, and delete events and speaker information.

### Features

* Manage events: Create, retrieve, update, and delete events associated with the program.
* Manage speakers: Create, retrieve, update, and delete speaker profiles.
* Associate speakers with events: Connect speakers to relevant events they'll be participating in.
* Manage speaker social media links: Include social media profiles (e.g., Twitter, LinkedIn) for speakers.

### Benefits

* **Streamlined Event Organization:** Efficiently manage event details and speaker participation.
* **Informative Event Listings:** Create clear and informative event descriptions with associated speakers.
* **Engaging Speaker Profiles:** Showcase speaker expertise and social media presence for program participants.

### Technologies

* Django REST framework (Web framework)
* Django (Python web framework)
* your preferred database (figure out how to set it up)

### Installation

**Prerequisites:**

* Python (version 3.x recommended)
* pip (package manager)
<!--* PostgreSQL (or your chosen database)-->

**Steps:**

1. Clone the repository:

```
git clone https://github.com/C-o-m-o-n/postman-students-api
```

2. Navigate to the project directory:

```
cd postman-students-api
```

3. Create a virtual environment (recommended):

   ```
   python -m venv env
   source env/bin/activate
   ```

4. Install dependencies:

```
pip install -r requirements.txt
```

5. Migrate database schema:

```
python manage.py migrate
```

6. Create a Django secret key:

```
python manage.py secretkey generate
```

7. Update the `.env` file with your database credentials and any other environment variables.

8. Run Django development server:

```
python manage.py runserver
```
*** Kindly check out all the branches for different features ***

### Usage

1. Access the API documentation using a tool like Swagger or your preferred API client. The documentation endpoint is typically located at `http://127.0.0.1:8000/api-docs/`.

2. Refer to the API documentation for details on available endpoints, authentication methods, and request/response formats.

### Contribution

I welcome contributions to this project! Please see the CONTRIBUTING.md file for guidelines on how to contribute.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
