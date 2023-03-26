# RoleStore
Discord Role and Nickname Storage
https://discord.com/api/oauth2/authorize?client_id=1089343293126615070&permissions=8&scope=bot

This bot is very simple and sits in the background, it will store UserIds, nicknames and roles in a data base, and re-assigns said roles if a user leaves and re-joins a server for any reason. 

## How to Run
1. Ensure you have docker installed on the host machine 
2. Pull the repo ```git clone https://github.com/sambarrett23072/RoleStore``` Note: it will create it's own directory called RoleStore
3. Create a .env file, and insert the following ```DISCORD_TOKEN={TOKEN}```
4. Build the docker container with the command ```docker build -t role-store .``` Note: may require sudo
5. Run the docker container with the command ```docker run -d --restart unless-stopped role-store``` Note: may require sudo

Feauture Roadmap 
https://github.com/sambarrett23072/RoleStore/milestones
