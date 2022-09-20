## APIs
**The complete project is deployed on https://companymanagement.mr-palindrome.tech/**

</br>

### Start

The complete project is dockerized.

Run the below commands to run docker image and start the project on local machine

```
docker-compose build
docker-compose up
```
### .env
First create a .env file inside the project directory.
and add your secret key by using following lines of code:
```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
This will generate a secret_key.
<br>
Or else add following in the .env file:
```
SECRET_KEY=2ns&e7w-89&=7^^v(mnzfqqx=i(^ytw20_327l3&^v*w1_^sju
```


## Available endpoints to hit
**All the APIs are documented at https://localhost:8000/**
- <code><span class="text-uppercase">POST</span> /api/auth/generate-token/</code>  -> Takes a set of user credentials and returns an access and refresh JSON web
token pair to prove the authentication of those credentials.
JSON body:
    ```
    {
        "username":"admin",
        "password":"admin"
    }
    ```
    This returns new refersh and access token.

- <code><span class="text-uppercase">POST</span> /api/auth/refresh-token/</code>  -> Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid. JSON body:
    ```
    {
    "refresh": "old refresh_token"
    }
    ```
    This returns new refersh and access token.

- <code><span class="text-uppercase">POST</span> /api/auth/verify-token/</code>  -> Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular use. JSON body:
    ```
    {
    "token": "token"
    }
    ```
**All the APIs below can only be accessible using JWT token.**
**To use them use the /api/auth/generate-token/ endpoint.**
**And while calling these APIs use Header Authorization: JWT {{access_token}}**
- <code><span class="text-uppercase">GET</span> /api/comapny/</code>  -> To fetch all the available companies. Can only work if the user is admin. It returns list of company objects. This endpoint requires admin permissions.

- <code><span class="text-uppercase">POST</span> /api/company/</code>  -> To create a new company. Can only be work if the user is admin. This endpoint requires admin permissions. JSON body:
    ```
    {
        "company_name": "Techwondow-NZ",
        "company_ceo": "Jaskaran Singh",
        "company_address": "NZ",
        "inception_Date": "2020-06-03"
    }
    ```


- <code><span class="text-uppercase">GET</span> /api/company/{id}/</code>  -> To retrieve a single company using its unique company id. This returns a complete object of the company with the company id. This endpoint requires admin permissions.


- <code><span class="text-uppercase">PUT</span> /api/company/{id}/</code>  -> To completely update the company object with the given id. This endpoint requires admin permissions. JSON body:
    ```
    {
        "company_name": "Google",
        "company_ceo": "Sundar Pichai",
        "company_address": "USA",
        "inception_Date": "2002-06-03"
    }
    ```

- <code><span class="text-uppercase">PATCH</span> /api/company/{id}/</code>  -> To partially update the company object with given comapny id. This endpoint requires admin permissions.

- <code><span class="text-uppercase">DELETE</span> /api/company/{id}/</code>  -> To delete the company object with the given company id. This endpoint requires admin permissions.

- <code><span class="text-uppercase">GET</span> /api/get-company-details/{id}/</code>  -> To get all the details of a company with given company id.

- <code><span class="text-uppercase">GET</span> /api/get-company/</code>  -> To get all the available company details.

- <code><span class="text-uppercase">GET</span> /api/get-company/{name}/</code>  -> To get company details by company name.

- <code><span class="text-uppercase">GET</span> /api/get-team/</code>  -> To get all teams available.

- <code><span class="text-uppercase">POST</span> /api/create-team/{id}/</code>  -> To create new team for the company with given company id. JSON body:
    ```
    {
        "team_lead_name":"Nayan Das"
    }
    ```

- <code><span class="text-uppercase">GET</span> /api/team/</code>  -> To get all team available. This requires admin permission.

- <code><span class="text-uppercase">POST</span> /api/team/</code>  -> To create a new team. This requires admin permission. JSON body:
    ```
    {
        "team_lead_name": "Mohammad Sageer",
        "company": "181d4ba0-7a97-493a-807f-8afe39224200"
    }
    ```

- <code><span class="text-uppercase">GET</span> /api/team/{id}/</code>  -> To retrieve a single team with the given team id. This requires admin permission.

- <code><span class="text-uppercase">PUT</span> /api/team/{id}/</code>  -> To completely update the team details with given id.

- <code><span class="text-uppercase">PATCH</span> /api/team/{id}/</code>  -> To partially update any field of the team with given team id.

- <code><span class="text-uppercase">DELETE</span> /api/team/{id}/</code>  -> To delete the team with given team id.



### All these APIs are also accessible using the Postman Collection availabele in the code directory or import the below JSON link: https://www.getpostman.com/collections/37d3e71f0f12b094e0ea