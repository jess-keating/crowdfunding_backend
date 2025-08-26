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
1. As a **community organiser**, I want to create a fundraiser so I can gather financial support for my event production needs.  
2. As a **supporter**, I want to pledge to a fundraiser so I can help make a local event happen.  
3. As a **supporter**, I want to choose to pledge anonymously so I can keep my contribution private.  
4. As a **fundraiser owner**, I want to update my campaign details so I can keep supporters informed.  
5. As a **fundraiser owner**, I want to close my campaign when the funding target is met.

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

| URL             | HTTP Method | Purpose                           | Request Body                  | Success Response Code | Authentication/Authorisation |
| --------------- | ----------- | --------------------------------- | ----------------------------- | --------------------- | ---------------------------- |
| /fundraisers/   | GET         | Fetch all the fundraisers         | N/A                           | 200                   | None                         |
| /fundraisers/   | POST        | Create a new fundraiser           | JSON Payload                  | 201                   | Any logged in user           |
| /fundraisers/1/ | GET         | Fetch a single fundraiser by ID   | N/A                           | 200                   | None                         |
| /pledge/        | GET         | Fetch all pledges                 | N/A                           | 200                   | (?)                          |
| /pledges/       | POST        | Create a new pledge               | JSON Payload                  | 201                   | Any logged in user           |
| /pledges/1/     | DELETE      | Delete an existing pledge by ID   | N/A                           | 204                   | Pledge owner or admin        |
| /users/         | POST        | Register a new user               | JSON Payload                  | 201                   | None                         |
| /users/login/   | POST        | Authenticate and log in a user    | JSON Payload (email/password) | 200                   | None                         |
| /users/profile/ | GET         | Retrieve logged-in user's profile | N/A                           | 200                   | Authenticated user only      |
| /users/logout/  | POST        | Log out the current user          | N/A                           | 204                   | Authenticated user only      |

### DB Schema
![](./database.drawio.svg)
