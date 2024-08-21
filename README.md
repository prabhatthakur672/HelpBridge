# HelpBridge
HelpBridge is a community-driven web application built with Django that facilitates mutual assistance among people. Users can create profiles, request help, offer assistance, and manage their requests, fostering a collaborative and supportive community.

## Aim
The aim of HelpBridge is to connect individuals who need help with those who can provide it. The platform supports various types of assistance including financial support, resource fulfillment (like food and clothing), and more.

## Features
- **User Profiles**: Users can create and manage their profiles.
- **Request Help**: Users can create posts to request assistance for various needs.
- **Offer Help**: Users can offer help in response to requests.
- **Manage Requests**: Users can edit or delete their help requests.
- **Request Status**: Users can view the status of their requests to see if they have been fulfilled or not.


# Getting Started
Follow these steps to clone and set up the HelpBridge project on your local machine:

## 1.Clone the Repository
To clone the repository, use the following commands:

<pre>
  <code id="clone-command">git clone https://github.com/prabhatthakur672/HelpBridge.git
  cd community_support_app</code>
</pre>
<button onclick="copyToClipboard('#clone-command')"></button>

## 2.Install Dependencies
Ensure you have Python and pip installed. Install the required packages using the `requirements.txt` file:

<pre>
  <code id="clone-command">pip install -r requirements.txt</code>
</pre>
<button onclick="copyToClipboard('#clone-command')"></button>

## 3.Set Up Environment Variables
Create a `.env` file in the root directory of the project and add your database credentials:
<pre>
<code id="clone-command">DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port
</code>
</pre>
<button onclick="copyToClipboard('#clone-command')"></button>

## 4.Apply Migrations
Run the following command to apply the database migrations:

<pre>
  <code id="clone-command">python manage.py migrate</code>
</pre>
<button onclick="copyToClipboard('#clone-command')"></button>

## 5.Run the Development Server
Start the Django development server:

<pre>
  <code id="clone-command">python manage.py runserver</code>
</pre>
<button onclick="copyToClipboard('#clone-command')"></button>
You can now access the application at `http://127.0.0.1:8000/`.

# Project Screenshots

![image](https://github.com/user-attachments/assets/a13d224c-8795-4a08-818d-d46fa44918ef)

![image](https://github.com/user-attachments/assets/a81d0e9b-8baf-40e9-9652-b6e6b282ccc5)

![image](https://github.com/user-attachments/assets/2aa28879-a561-431a-97ab-9cf23aef8b33)

![image](https://github.com/user-attachments/assets/db3ac960-989b-48e7-a783-f66e19181e91)

![image](https://github.com/user-attachments/assets/1589f3ac-cfd6-455f-8fee-cb66313ac62d)

![image](https://github.com/user-attachments/assets/9f157242-e70c-4514-a700-9b6ac68c82a2)


## License
This project is licensed under the MIT License - see the [LICENSE file](https://github.com/prabhatthakur672/HelpBridge/blob/main/LICENSE.txt) for details.

## Contact
For any questions or feedback, please reach out to prabhatthakur672@gmail.com.

