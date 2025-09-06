# Crowdfunding Back End
Jessica Keating

## Planning:
### Concept/Name
**LightUp** is a crowdfunding platform for community groups, schools, theatres, and event organisers to raise funds for lighting, sound, and stage production needs.  
Campaigns are focused, short-term, and tangible. Such as hiring stage lights, microphones, or projectors for a specific event.

### Intended Audience/User Stories
**Intended Audience**
- Community theatre groups needing lighting or sound hire
- School production teams seeking help for AV equipment
- Local event organisers raising funds for staging or effects
- Supporters wanting to directly contribute to creative, local events

**User Stories**
1. As a **visitor**, I want to view open fundraisers so I can discover projects to support.  
2. As a **supporter**, I want to pledge to a fundraiser so I can help make a local event happen.  
3. As a **supporter**, I want to choose to pledge anonymously so I can keep my contribution private.  
4. As a **fundraiser owner**, I want to update my fundraiser details so I can keep supporters informed.  
5. As a **fundraiser owner**, I want to close my fundrasier when the funding target is met.

### Front End Pages/Functionality
- **Home Page**
  - Featured fundraisers
  - Fundraiser search/filter
- **Create New Fundraiser Page**
  - Form with fundraiser details
  - Ability to submit
  - Nice error pages for validation
- **Fundraiser Detail Page**
  - Display full description, target, progress, and pledges
  - Pledge form for logged-in users
  - Show all pledges made so far
- **User Account Pages**
  - Sign up / Log in
  - View user’s own fundraisers and pledges

### API Spec

| URL                | HTTP Method | Purpose                        | Request Body                              | Success Code | Error Codes & Reasons                                                                   | Auth Required        |
| ------------------ | ----------- | ------------------------------ | ----------------------------------------- | ------------ | --------------------------------------------------------------------------------------- | -------------------- |
| /api-token-auth/   | POST        | Obtain authentication token    | username, password                        | 200          | 400 (invalid credentials)                                                               | No                   |
| /users/            | GET         | List all users                 | N/A                                       | 200          | None                                                                                    | No                   |
| /users/            | POST        | Register a new user            | username, email, password                 | 201          | 400 (invalid/missing fields)                                                            | No                   |
| /users/{id}/       | GET         | Retrieve user details by ID    | N/A                                       | 200          | 404 (user not found)                                                                    | No                   |
| /fundraisers/      | GET         | List all fundraisers           | N/A                                       | 200          | None                                                                                    | No                   |
| /fundraisers/      | POST        | Create a new fundraiser        | title, description, goal_amount, image    | 201          | 400 (invalid data), 401 (not logged in)                                                 | Yes (logged in)      |
| /fundraisers/{id}/ | GET         | Retrieve fundraiser details    | N/A                                       | 200          | 404 (fundraiser not found)                                                              | No                   |
| /fundraisers/{id}/ | PUT         | Update fundraiser (owner only) | fields to update                          | 200          | 400 (invalid data), 401 (not logged in), 403 (not owner), 404 (fundraiser not found)    | Yes (owner only)     |
| /pledges/          | GET         | List all pledges               | N/A                                       | 200          | None                                                                                    | No                   |
| /pledges/          | POST        | Create a pledge                | amount, comment, anonymous, fundraiser_id | 201          | 400 (invalid data), 401 (not logged in)                                                 | Yes (logged in)      |
| /pledges/{id}/     | GET         | Retrieve pledge details        | N/A                                       | 200          | 404 (pledge not found)                                                                  | No                   |
| /pledges/{id}/     | PUT         | Update pledge (supporter only) | fields to update                          | 200          | 400 (invalid data), 401 (not logged in), 403 (not pledge owner), 404 (pledge not found) | Yes (supporter only) |

### DB Schema
![](./database.drawio.svg)

### Heroku Deployed: https://lightup-38603a824c6f.herokuapp.com/ 
### Insomnia Request Screenshots

**Successful GET**
![](.//images/GET-Fetch-all-users.png)
![](.//images/GET-Fetch-all-fundraisers.png)
![](.//images/GET-Fetch-all-pledges.png)

**Successful POST**
![](.//images/POST-Create-new-user.png)
![](.//images/POST-Create-new-fundraiser.png)
![](.//images/POST-Create-new-pledge-(not-my-fundraiser).png)

**Returning Auth Token**
![](.//images/POST-Get-auth-token.png)

**Successful PUT**
![](.//images/PUT-Update-fundraiser-(as-owner).png)
![](.//images/PUT-Update-pledge.png) 

